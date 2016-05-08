"""hg to git migration tool."""

import argparse
import contextlib
import datetime
import os
import logging
import shlex
import shutil
import sys
import subprocess

from functools import wraps
from subprocess import PIPE, run

logfile_time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")

logging.basicConfig(
        format='%(asctime)s %(message)s',
        filename='log-{timestamp}.log'.format(timestamp=logfile_time),
        level=logging.DEBUG)


def log(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        logging.info("[function] {0}".format(func.__name__))
        return func(*args, **kwargs)
    return with_logging


def fail(msg):
    print(msg)
    sys.exit(-1)


def print_result(cmd, result):
    assert isinstance(result, subprocess.CompletedProcess)
    print("Failed: '{command}' [retcode: {retcode}].".format(command=cmd, retcode=result.returncode))
    print("STDOUT:\n{stdout}\nSTDERR:\n{stderr}".format(stdout=result.stdout, stderr=result.stderr))


def execute_process(cmd):
    return run(shlex.split(cmd), stdout=PIPE, stderr=PIPE, universal_newlines=True)


def safe_execute(cmd):
    result = execute_process(cmd)
    if 0 != result.returncode:
        print_result(cmd, result)
    return result


def strict_execute(cmd):
    result = execute_process(cmd)
    if 0 != result.returncode:
        print_result(cmd, result)
        sys.exit(-1)
    return result


@contextlib.contextmanager
def pushd(dir):
    cwd = os.getcwd()
    try:
        path = os.path.abspath(dir)
        os.chdir(path)
        yield
    except OSError:
        pass
    finally:
        os.chdir(cwd)


def execute_with_dir_context(dir, cmd, no_fail=False):
    logging.debug("[command] {cmd}".format(cmd=cmd))
    if not os.path.exists(dir):
        fail("{dir} does not exists.".format(dir=dir))

    with pushd(dir):
        if no_fail:
            return safe_execute(cmd)
        return strict_execute(cmd)


def execute_with_dir_context_with_progress(dir, cmd):
    logging.debug("[command] {cmd}".format(cmd=cmd))
    if not os.path.exists(dir):
        fail("{dir} does not exists.".format(dir=dir))
    with pushd(dir):
        run_command(cmd)


def run_command(cmd):
    cmd = shlex.split(cmd)
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    while True:
        out = process.stdout.read(1)
        if out == b'' and process.poll() is not None:
            break
        if out != b'':
            sys.stdout.write(out.decode("utf-8"))
        sys.stdout.flush()


@log
def get_dir_and_base(path):
    return os.path.basename(path), os.path.basename(path)


@log
def git_initialize_local_repo(git_repo_abspath):
    execute_with_dir_context(git_repo_abspath, "git init --bare .")


@log
def git_gc_local_repo(git_repo_abspath):
    execute_with_dir_context(git_repo_abspath, "git gc --aggressive")


@log
def migrate_hg_to_git(hg_repo_abspath, git_repo_abspath):
    execute_with_dir_context_with_progress(
            hg_repo_abspath,
            "hg --config extensions.hgext.bookmarks= --config extensions.hggit=  push {local_git_repo}".format(
                    local_git_repo=git_repo_abspath))


@log
def migrate(hg_repo_abspath, git_repo_abspath, delete_existing=False):
    if delete_existing and os.path.exists(git_repo_abspath):
        shutil.rmtree(git_repo_abspath)

    os.makedirs(git_repo_abspath)
    git_initialize_local_repo(git_repo_abspath)
    hg_branch_to_bookmark(hg_repo_abspath)
    migrate_hg_to_git(hg_repo_abspath, git_repo_abspath)
    git_gc_local_repo(git_repo_abspath)


@log
def hg_branch_to_bookmark(hg_repo_abspath):
    result = execute_with_dir_context(hg_repo_abspath, "hg branches")
    branches = [branch_line.split()[0] for branch_line in result.stdout.splitlines()]
    for branch in branches:
        if branch == "default":
            bookmark = "master"
        else:
            bookmark = "py-{branch}".format(branch=branch)
        execute_with_dir_context(
                hg_repo_abspath,
                "hg bookmark -r {branch} {bookmark} -f".format(branch=branch, bookmark=bookmark))


@log
def git_normalize_branches(git_repo_abspath):
    normalized = []
    result = execute_with_dir_context(git_repo_abspath, "git for-each-ref --format='%(refname:short)' refs/heads/")
    branches = result.stdout.splitlines()
    for branch in branches:
        newname = branch
        if branch.startswith("py-"):
            newname = branch.strip("py-")
            execute_with_dir_context(git_repo_abspath, "git branch -m {oldname} {newname}".format(
                    oldname=branch,
                    newname=newname))

        normalized.append(newname)

    return normalized


@log
def git_add_origin(git_repo_abspath, github_url):
    execute_with_dir_context(git_repo_abspath, "git remote add origin {github_url}".format(github_url=github_url))


@log
def git_push_remote(git_repo_abspath, git_branches):
    for branch in git_branches:
      execute_with_dir_context(git_repo_abspath, "git push origin {branch}".format(branch=branch))

@log
def git_push_tags(git_repo_abspath):
    execute_with_dir_context(git_repo_abspath, "git push origin --tags")


def check_prerequisites():
    for command in ["git", "hg"]:
        strict_execute("command -v {cmd}".format(cmd=command))
    result = execute_process("hg --config extensions.hgext.bookmarks= --config extensions.hggit=  push /tmp/bar")
    if "failed to import extension" in result.stderr:
        print("Pre-Requisite Failure. Please install hg-git (http://hg-git.github.io/) extension for mercurial.")
        sys.exit(-1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("hg_repo", help="location of mercurial repository in the filesystem.")
    parser.add_argument("github_url", help="git url to migrate the mercurial repository.")
    args = parser.parse_args()
    hg_repo_abspath = os.path.abspath(args.hg_repo)
    git_repo_abspath = os.path.abspath(
            os.path.join(os.path.dirname(hg_repo_abspath), 'git-repo', os.path.basename(hg_repo_abspath)))

    check_prerequisites()

    migrate(hg_repo_abspath, git_repo_abspath, delete_existing=True)

    git_branches = git_normalize_branches(git_repo_abspath)
    git_add_origin(git_repo_abspath, args.github_url)
    git_push_remote(git_repo_abspath, git_branches)
    git_push_tags(git_repo_abspath)

    print("Migration completed to git_repo: {git_url}".format(git_url=args.github_url))

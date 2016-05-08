import hg_git_migrator


def check_commit_count(hg_path, git_path):
    with hg_git_migrator.pushd(hg_path):
        hg_results = hg_git_migrator.strict_execute('hg id --num --rev tip')
    hg_count = int(hg_results.stdout) + 1
    with hg_git_migrator.pushd(git_path):
        git_results = hg_git_migrator.strict_execute('git log --pretty=oneline')
    git_count = len(git_results.stdout.splitlines())
    if hg_count != git_count:
        raise ValueError('hg commit count != git commit count '
                         '({} != {})'.format(hg_count, git_count))



if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("hg_repo", help="location of mercurial repository in the filesystem.")
    parser.add_argument("git_repo", help="location of git repository in the filesystem.")
    args = parser.parse_args()

    hg_git_migrator.check_prerequisites(hg_git_ext=False)

    check_commit_count(args.hg_repo, args.git_repo)

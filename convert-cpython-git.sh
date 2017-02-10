#!/bin/bash

NOW=$(date +"%F-%H-%M")
LOGFILE="logfile-$NOW.log"

CPYTHON_REPO=$HOME/cpython/cpython

function setupGit() {
    echo -e "$(date +"%F-%H-%M-%S") setting up git" >> $LOGFILE
    mkdir -p $HOME/git-repo/cpython
    git init --bare $HOME/git-repo/cpython
    echo -e "$(date +"%F-%H-%M-%S") finished setting up git" >> $LOGFILE
}

function branchesToBookmarks() {
	echo -e "$(date +"%F-%H-%M-%S") renaming branches" >> $LOGFILE
	cd $CPYTHON_REPO
	hg bookmark -r default master -f
	hg bookmark -r 2.7 py-2.7 -f
	hg bookmark -r 3.3 py-3.3 -f
	hg bookmark -r 3.5 py-3.5 -f
	hg bookmark -r 3.4 py-3.4 -f
	hg bookmark -r 3.6 py-3.6 -f
	hg bookmark -r 3.2 py-3.2 -f
	hg bookmark -r 2.6 py-2.6 -f
	hg bookmark -r 3.1 py-3.1 -f
	hg bookmark -r 2.5 py-2.5 -f
	hg bookmark -r 3.0 py-3.0 -f
	hg bookmark -r legacy-trunk py-legacy-trunk -f
	hg bookmark -r 2.4 py-2.4 -f
	hg bookmark -r 2.3 py-2.3 -f
	hg bookmark -r 2.2 py-2.2 -f
	hg bookmark -r 2.1 py-2.1 -f
	hg bookmark -r 2.0 py-2.0 -f
	echo -e "$(date +"%F-%H-%M-%S") renaming branches complete" >> $LOGFILE
}


function migrate() {
	echo -e "$(date +"%F-%H-%M-%S") started migration" >> $LOGFILE
	cd $CPYTHON_REPO
	hg --config extensions.hgext.bookmarks= --config extensions.hggit=  push $HOME/git-repo/cpython
	echo -e "$(date +"%F-%H-%M-%S") finished migration" >> $LOGFILE
}

function gc() {
	echo -e "$(date +"%F-%H-%M-%S") started gc" >> $LOGFILE
	cd $HOME/git-repo/cpython
	git gc --aggressive
	echo -e "$(date +"%F-%H-%M-%S") completed gc" >> $LOGFILE
}

function branchRename() {
	echo -e "$(date +"%F-%H-%M-%S") renaming branches" >> $LOGFILE
	cd $HOME/git-repo/cpython
	git branch -m py-2.0 2.0
	git branch -m py-2.1 2.1
	git branch -m py-2.2 2.2
	git branch -m py-2.3 2.3
	git branch -m py-2.4 2.4
	git branch -m py-2.5 2.5
	git branch -m py-2.6 2.6
	git branch -m py-2.7 2.7
	git branch -m py-3.0 3.0
	git branch -m py-3.1 3.1
	git branch -m py-3.2 3.2
	git branch -m py-3.3 3.3
	git branch -m py-3.4 3.4
	git branch -m py-3.5 3.5
	git branch -m py-3.6 3.6
	git branch -m py-legacy-trunk legacy-trunk
	echo -e "$(date +"%F-%H-%M-%S") finished renaming branches" >> $LOGFILE
}

function pushRemote() {
	echo -e "$(date +"%F-%H-%M-%S") pushing to remote" >> $LOGFILE
	cd $HOME/git-repo/cpython
	git remote add origin git@github.com:orsenthil/orsenthil-cpython.git
	git push -u origin master
	git push -u origin --all
	git push origin --tags
	echo -e "$(date +"%F-%H-%M-%S") remote push complete" >> $LOGFILE
}


setupGit
branchesToBookmarks
migrate
gc
branchRename
pushRemote

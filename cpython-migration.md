#### Preparation

##### Clone the cpython mercurial repo

```
    hg clone https://hg.python.org/cpython/ cpython
```

#####  Create the local bare git repo

```
    mkdir -p git-repo/cpython
    git init --bare git-repo/cpython
```

##### Mark all mercurial branches as bookmarks

*hg branches -c* will list all the branches including the closed ones.

```
    cd cpython
    hg branches -c
```

##### branches to bookmarks

We name *default* branch as *master* bookmark and  suffix other branches with name "py-" in the bookmark because a
branch and a bookmark cannot have a same name.

```
    hg bookmark -r default master -f
    hg bookmark -r 2.7 py-2.7 -f
    hg bookmark -r 3.3 py-3.3 -f
    hg bookmark -r 3.5 py-3.5 -f
    hg bookmark -r 3.4 py-3.4 -f
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
```

#### Migrate hg to git

Using [hg-git](http://hg-git.github.io/) extension, migrate the hg repo to the local git repo.

#####  Push to local git repository

```
hg --config extensions.hgext.bookmarks= --config extensions.hggit=  push ../git-repo/cpython
```

This will push all mercurial commits to git repository.

> pushing to ../git-repo/cpython
> searching for changes
> adding objects
> added 101242 commits with 316708 trees and 203513 blobs


##### Clean-up and garbage collect local git repo

```
cd ../git-repo/cpython
git gc --aggressive
```

>Counting objects: 621463, done.
>Compressing objects: 100% (619266/619266), done.
>Writing objects: 100% (621463/621463), done.
>Total 621463 (delta 508795), reused 112668 (delta 0)
>Checking connectivity: 621463, done.

##### Verify Git branches and rename them back to original hg branch names.

```
git branch
```

>* master
> py-2.0
> py-2.1
> py-2.2
> py-2.3
> py-2.4
> py-2.5
> py-2.6
> py-2.7
> py-3.0
> py-3.1
> py-3.2
> py-3.3
> py-3.4
> py-3.5
> py-legacy-trunk

##### Rename the branches

```
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
git branch -m py-legacy-trunk legacy-trunk
```

#### Push git branches to remote.

##### add remote origin

```
git remote add origin git@github.com:orsenthil/cpython3.git
```

#####  git push master

```
git push -u origin master
```

>Counting objects: 581571, done.
>Compressing objects: 100% (108549/108549), done.
>Writing objects: 100% (581571/581571), 136.18 MiB | 7.24 MiB/s, done.
>Total 581571 (delta 475276), reused 576226 (delta 470933)
>To git@github.com:orsenthil/cpython3.git
> * [new branch]      master -> master
>Branch master set up to track remote branch master from origin.

#####  git push all branches

```
git push -u origin --all
```

>Counting objects: 53135, done.
>Compressing objects: 100% (12482/12482), done.
>Writing objects: 100% (43327/43327), 15.22 MiB | 4.96 MiB/s, done.
>Total 43327 (delta 35200), reused 37884 (delta 30712)
>To git@github.com:orsenthil/cpython3.git
> * [new branch]      2.0 -> 2.0
> * [new branch]      2.1 -> 2.1
> * [new branch]      2.2 -> 2.2
> * [new branch]      2.3 -> 2.3
> * [new branch]      2.4 -> 2.4
> * [new branch]      2.5 -> 2.5
> * [new branch]      2.6 -> 2.6
> * [new branch]      2.7 -> 2.7
> * [new branch]      3.0 -> 3.0
> * [new branch]      3.1 -> 3.1
> * [new branch]      3.2 -> 3.2
> * [new branch]      3.3 -> 3.3
> * [new branch]      3.4 -> 3.4
> * [new branch]      3.5 -> 3.5
> * [new branch]      legacy-trunk -> legacy-trunk
>Branch master set up to track remote branch master from origin.
>Branch 2.0 set up to track remote branch 2.0 from origin.
>Branch 2.1 set up to track remote branch 2.1 from origin.
>Branch 2.2 set up to track remote branch 2.2 from origin.
>Branch 2.3 set up to track remote branch 2.3 from origin.
>Branch 2.4 set up to track remote branch 2.4 from origin.
>Branch 2.5 set up to track remote branch 2.5 from origin.
>Branch 2.6 set up to track remote branch 2.6 from origin.
>Branch 2.7 set up to track remote branch 2.7 from origin.
>Branch 3.0 set up to track remote branch 3.0 from origin.
>Branch 3.1 set up to track remote branch 3.1 from origin.
>Branch 3.2 set up to track remote branch 3.2 from origin.
>Branch 3.3 set up to track remote branch 3.3 from origin.
>Branch 3.4 set up to track remote branch 3.4 from origin.
>Branch 3.5 set up to track remote branch 3.5 from origin.
>Branch legacy-trunk set up to track remote branch legacy-trunk from origin.

##### Done

* For e.g, https://github.com/orsenthil/cpython3

If you see any scope for improvement in the tool, please suggest them me. Thank you!

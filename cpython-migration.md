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

```
pushing to ../git-repo/cpython
searching for changes
adding objects
added 101242 commits with 316708 trees and 203513 blobs
```


##### Clean-up and garbage collect local git repo

```
cd ../git-repo/cpython
git gc --aggressive
```

```
Counting objects: 621463, done.
Compressing objects: 100% (619266/619266), done.
Writing objects: 100% (621463/621463), done.
Total 621463 (delta 508795), reused 112668 (delta 0)
Checking connectivity: 621463, done.
```

##### Verify Git branches and rename them back to original hg branch names.

```
git branch
```

```
* master
py-2.0
py-2.1
py-2.2
py-2.3
py-2.4
py-2.5
py-2.6
py-2.7
py-3.0
py-3.1
py-3.2
py-3.3
py-3.4
py-3.5
py-legacy-trunk
```

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

```
Counting objects: 581571, done.
Compressing objects: 100% (108549/108549), done.
Writing objects: 100% (581571/581571), 136.18 MiB | 7.24 MiB/s, done.
Total 581571 (delta 475276), reused 576226 (delta 470933)
To git@github.com:orsenthil/cpython3.git
 * [new branch]      master -> master
Branch master set up to track remote branch master from origin.
```

#####  git push all branches

```
git push -u origin --all
```

```
Counting objects: 53135, done.
Compressing objects: 100% (12482/12482), done.
Writing objects: 100% (43327/43327), 15.22 MiB | 4.96 MiB/s, done.
Total 43327 (delta 35200), reused 37884 (delta 30712)
To git@github.com:orsenthil/cpython3.git
 * [new branch]      2.0 -> 2.0
 * [new branch]      2.1 -> 2.1
 * [new branch]      2.2 -> 2.2
 * [new branch]      2.3 -> 2.3
 * [new branch]      2.4 -> 2.4
 * [new branch]      2.5 -> 2.5
 * [new branch]      2.6 -> 2.6
 * [new branch]      2.7 -> 2.7
 * [new branch]      3.0 -> 3.0
 * [new branch]      3.1 -> 3.1
 * [new branch]      3.2 -> 3.2
 * [new branch]      3.3 -> 3.3
 * [new branch]      3.4 -> 3.4
 * [new branch]      3.5 -> 3.5
 * [new branch]      legacy-trunk -> legacy-trunk
Branch master set up to track remote branch master from origin.
Branch 2.0 set up to track remote branch 2.0 from origin.
Branch 2.1 set up to track remote branch 2.1 from origin.
Branch 2.2 set up to track remote branch 2.2 from origin.
Branch 2.3 set up to track remote branch 2.3 from origin.
Branch 2.4 set up to track remote branch 2.4 from origin.
Branch 2.5 set up to track remote branch 2.5 from origin.
Branch 2.6 set up to track remote branch 2.6 from origin.
Branch 2.7 set up to track remote branch 2.7 from origin.
Branch 3.0 set up to track remote branch 3.0 from origin.
Branch 3.1 set up to track remote branch 3.1 from origin.
Branch 3.2 set up to track remote branch 3.2 from origin.
Branch 3.3 set up to track remote branch 3.3 from origin.
Branch 3.4 set up to track remote branch 3.4 from origin.
Branch 3.5 set up to track remote branch 3.5 from origin.
Branch legacy-trunk set up to track remote branch legacy-trunk from origin.
```

##### Push the tags

```
git push origin --tags
```

```
Counting objects: 39313, done.
Compressing objects: 100% (11575/11575), done.
Writing objects: 100% (37937/37937), 16.87 MiB | 4.55 MiB/s, done.
Total 37937 (delta 29843), reused 32899 (delta 26242)
To git@github.com:orsenthil/cpython2.git
 * [new tag]         v0.9.8 -> v0.9.8
 * [new tag]         v0.9.9 -> v0.9.9
 * [new tag]         v1.0.1 -> v1.0.1
 * [new tag]         v1.0.2 -> v1.0.2
 * [new tag]         v1.1 -> v1.1
 * [new tag]         v1.1.1 -> v1.1.1
 * [new tag]         v1.2 -> v1.2
 * [new tag]         v1.2b1 -> v1.2b1
 * [new tag]         v1.2b2 -> v1.2b2
 * [new tag]         v1.2b3 -> v1.2b3
 * [new tag]         v1.2b4 -> v1.2b4
 * [new tag]         v1.3 -> v1.3
 * [new tag]         v1.3b1 -> v1.3b1
 * [new tag]         v1.4 -> v1.4
 * [new tag]         v1.4b1 -> v1.4b1
 * [new tag]         v1.4b2 -> v1.4b2
 * [new tag]         v1.4b3 -> v1.4b3
 * [new tag]         v1.5 -> v1.5
 * [new tag]         v1.5.1 -> v1.5.1
 * [new tag]         v1.5.2 -> v1.5.2
 * [new tag]         v1.5.2a1 -> v1.5.2a1
 * [new tag]         v1.5.2a2 -> v1.5.2a2
 * [new tag]         v1.5.2b1 -> v1.5.2b1
 * [new tag]         v1.5.2b2 -> v1.5.2b2
 * [new tag]         v1.5.2c1 -> v1.5.2c1
 * [new tag]         v1.5a1 -> v1.5a1
 * [new tag]         v1.5a2 -> v1.5a2
 * [new tag]         v1.5a3 -> v1.5a3
 * [new tag]         v1.5a4 -> v1.5a4
 * [new tag]         v1.5b1 -> v1.5b1
 * [new tag]         v1.5b2 -> v1.5b2
 * [new tag]         v1.6a1 -> v1.6a1
 * [new tag]         v1.6a2 -> v1.6a2
 * [new tag]         v2.0 -> v2.0
 * [new tag]         v2.0.1 -> v2.0.1
 * [new tag]         v2.0.1c1 -> v2.0.1c1
 * [new tag]         v2.0b1 -> v2.0b1
 * [new tag]         v2.0b2 -> v2.0b2
 * [new tag]         v2.0c1 -> v2.0c1
 * [new tag]         v2.1 -> v2.1
 * [new tag]         v2.1.1 -> v2.1.1
 * [new tag]         v2.1.1c1 -> v2.1.1c1
 * [new tag]         v2.1.2 -> v2.1.2
 * [new tag]         v2.1.2c1 -> v2.1.2c1
 * [new tag]         v2.1.3 -> v2.1.3
 * [new tag]         v2.1a1 -> v2.1a1
 * [new tag]         v2.1a2 -> v2.1a2
 * [new tag]         v2.1b1 -> v2.1b1
 * [new tag]         v2.1b2 -> v2.1b2
 * [new tag]         v2.1c1 -> v2.1c1
 * [new tag]         v2.1c2 -> v2.1c2
 * [new tag]         v2.2 -> v2.2
 * [new tag]         v2.2.1 -> v2.2.1
 * [new tag]         v2.2.1c1 -> v2.2.1c1
 * [new tag]         v2.2.1c2 -> v2.2.1c2
 * [new tag]         v2.2.2 -> v2.2.2
 * [new tag]         v2.2.2b1 -> v2.2.2b1
 * [new tag]         v2.2.3 -> v2.2.3
 * [new tag]         v2.2.3c1 -> v2.2.3c1
 * [new tag]         v2.2a3 -> v2.2a3
 * [new tag]         v2.3.1 -> v2.3.1
 * [new tag]         v2.3.2 -> v2.3.2
 * [new tag]         v2.3.2c1 -> v2.3.2c1
 * [new tag]         v2.3.3 -> v2.3.3
 * [new tag]         v2.3.3c1 -> v2.3.3c1
 * [new tag]         v2.3.4 -> v2.3.4
 * [new tag]         v2.3.4c1 -> v2.3.4c1
 * [new tag]         v2.3.5 -> v2.3.5
 * [new tag]         v2.3.5c1 -> v2.3.5c1
 * [new tag]         v2.3.6 -> v2.3.6
 * [new tag]         v2.3.6c1 -> v2.3.6c1
 * [new tag]         v2.3.7 -> v2.3.7
 * [new tag]         v2.3.7c1 -> v2.3.7c1
 * [new tag]         v2.3c1 -> v2.3c1
 * [new tag]         v2.3c2 -> v2.3c2
 * [new tag]         v2.4 -> v2.4
 * [new tag]         v2.4.1 -> v2.4.1
 * [new tag]         v2.4.1c1 -> v2.4.1c1
 * [new tag]         v2.4.1c2 -> v2.4.1c2
 * [new tag]         v2.4.2 -> v2.4.2
 * [new tag]         v2.4.2c1 -> v2.4.2c1
 * [new tag]         v2.4.3 -> v2.4.3
 * [new tag]         v2.4.3c1 -> v2.4.3c1
 * [new tag]         v2.4.4 -> v2.4.4
 * [new tag]         v2.4.4c1 -> v2.4.4c1
 * [new tag]         v2.4.5 -> v2.4.5
 * [new tag]         v2.4.5c1 -> v2.4.5c1
 * [new tag]         v2.4.6 -> v2.4.6
 * [new tag]         v2.4.6c1 -> v2.4.6c1
 * [new tag]         v2.4a1 -> v2.4a1
 * [new tag]         v2.4a2 -> v2.4a2
 * [new tag]         v2.4a3 -> v2.4a3
 * [new tag]         v2.4b1 -> v2.4b1
 * [new tag]         v2.4b2 -> v2.4b2
 * [new tag]         v2.4c1 -> v2.4c1
 * [new tag]         v2.5 -> v2.5
 * [new tag]         v2.5.1 -> v2.5.1
 * [new tag]         v2.5.1c1 -> v2.5.1c1
 * [new tag]         v2.5.2 -> v2.5.2
 * [new tag]         v2.5.2c1 -> v2.5.2c1
 * [new tag]         v2.5.3 -> v2.5.3
 * [new tag]         v2.5.3c1 -> v2.5.3c1
 * [new tag]         v2.5.4 -> v2.5.4
 * [new tag]         v2.5.5 -> v2.5.5
 * [new tag]         v2.5.5c1 -> v2.5.5c1
 * [new tag]         v2.5.5c2 -> v2.5.5c2
 * [new tag]         v2.5.6 -> v2.5.6
 * [new tag]         v2.5.6c1 -> v2.5.6c1
 * [new tag]         v2.5a0 -> v2.5a0
 * [new tag]         v2.5a1 -> v2.5a1
 * [new tag]         v2.5a2 -> v2.5a2
 * [new tag]         v2.5b1 -> v2.5b1
 * [new tag]         v2.5b2 -> v2.5b2
 * [new tag]         v2.5b3 -> v2.5b3
 * [new tag]         v2.5c1 -> v2.5c1
 * [new tag]         v2.5c2 -> v2.5c2
 * [new tag]         v2.6 -> v2.6
 * [new tag]         v2.6.1 -> v2.6.1
 * [new tag]         v2.6.2 -> v2.6.2
 * [new tag]         v2.6.2c1 -> v2.6.2c1
 * [new tag]         v2.6.3 -> v2.6.3
 * [new tag]         v2.6.3rc1 -> v2.6.3rc1
 * [new tag]         v2.6.4 -> v2.6.4
 * [new tag]         v2.6.4rc1 -> v2.6.4rc1
 * [new tag]         v2.6.4rc2 -> v2.6.4rc2
 * [new tag]         v2.6.5 -> v2.6.5
 * [new tag]         v2.6.5rc1 -> v2.6.5rc1
 * [new tag]         v2.6.5rc2 -> v2.6.5rc2
 * [new tag]         v2.6.6 -> v2.6.6
 * [new tag]         v2.6.6rc1 -> v2.6.6rc1
 * [new tag]         v2.6.6rc2 -> v2.6.6rc2
 * [new tag]         v2.6.7 -> v2.6.7
 * [new tag]         v2.6.8 -> v2.6.8
 * [new tag]         v2.6.8rc1 -> v2.6.8rc1
 * [new tag]         v2.6.8rc2 -> v2.6.8rc2
 * [new tag]         v2.6.9 -> v2.6.9
 * [new tag]         v2.6.9rc1 -> v2.6.9rc1
 * [new tag]         v2.6a1 -> v2.6a1
 * [new tag]         v2.6a2 -> v2.6a2
 * [new tag]         v2.6a3 -> v2.6a3
 * [new tag]         v2.6b1 -> v2.6b1
 * [new tag]         v2.6b2 -> v2.6b2
 * [new tag]         v2.6b3 -> v2.6b3
 * [new tag]         v2.6rc1 -> v2.6rc1
 * [new tag]         v2.6rc2 -> v2.6rc2
 * [new tag]         v2.7 -> v2.7
 * [new tag]         v2.7.1 -> v2.7.1
 * [new tag]         v2.7.10 -> v2.7.10
 * [new tag]         v2.7.10rc1 -> v2.7.10rc1
 * [new tag]         v2.7.11 -> v2.7.11
 * [new tag]         v2.7.11rc1 -> v2.7.11rc1
 * [new tag]         v2.7.1rc1 -> v2.7.1rc1
 * [new tag]         v2.7.2 -> v2.7.2
 * [new tag]         v2.7.2rc1 -> v2.7.2rc1
 * [new tag]         v2.7.3 -> v2.7.3
 * [new tag]         v2.7.3rc1 -> v2.7.3rc1
 * [new tag]         v2.7.3rc2 -> v2.7.3rc2
 * [new tag]         v2.7.4 -> v2.7.4
 * [new tag]         v2.7.4rc1 -> v2.7.4rc1
 * [new tag]         v2.7.5 -> v2.7.5
 * [new tag]         v2.7.6 -> v2.7.6
 * [new tag]         v2.7.6rc1 -> v2.7.6rc1
 * [new tag]         v2.7.7 -> v2.7.7
 * [new tag]         v2.7.7rc1 -> v2.7.7rc1
 * [new tag]         v2.7.8 -> v2.7.8
 * [new tag]         v2.7.9 -> v2.7.9
 * [new tag]         v2.7.9rc1 -> v2.7.9rc1
 * [new tag]         v2.7a1 -> v2.7a1
 * [new tag]         v2.7a2 -> v2.7a2
 * [new tag]         v2.7a3 -> v2.7a3
 * [new tag]         v2.7a4 -> v2.7a4
 * [new tag]         v2.7b1 -> v2.7b1
 * [new tag]         v2.7b2 -> v2.7b2
 * [new tag]         v2.7rc1 -> v2.7rc1
 * [new tag]         v2.7rc2 -> v2.7rc2
 * [new tag]         v3.0 -> v3.0
 * [new tag]         v3.0.1 -> v3.0.1
 * [new tag]         v3.0a1 -> v3.0a1
 * [new tag]         v3.0a2 -> v3.0a2
 * [new tag]         v3.0a3 -> v3.0a3
 * [new tag]         v3.0a4 -> v3.0a4
 * [new tag]         v3.0a5 -> v3.0a5
 * [new tag]         v3.0b1 -> v3.0b1
 * [new tag]         v3.0b2 -> v3.0b2
 * [new tag]         v3.0b3 -> v3.0b3
 * [new tag]         v3.0rc1 -> v3.0rc1
 * [new tag]         v3.0rc2 -> v3.0rc2
 * [new tag]         v3.0rc3 -> v3.0rc3
 * [new tag]         v3.1 -> v3.1
 * [new tag]         v3.1.1 -> v3.1.1
 * [new tag]         v3.1.1rc1 -> v3.1.1rc1
 * [new tag]         v3.1.2 -> v3.1.2
 * [new tag]         v3.1.2rc1 -> v3.1.2rc1
 * [new tag]         v3.1.3 -> v3.1.3
 * [new tag]         v3.1.3rc1 -> v3.1.3rc1
 * [new tag]         v3.1.4 -> v3.1.4
 * [new tag]         v3.1.4rc1 -> v3.1.4rc1
 * [new tag]         v3.1.5 -> v3.1.5
 * [new tag]         v3.1.5rc1 -> v3.1.5rc1
 * [new tag]         v3.1.5rc2 -> v3.1.5rc2
 * [new tag]         v3.1a1 -> v3.1a1
 * [new tag]         v3.1a2 -> v3.1a2
 * [new tag]         v3.1b1 -> v3.1b1
 * [new tag]         v3.1rc1 -> v3.1rc1
 * [new tag]         v3.1rc2 -> v3.1rc2
 * [new tag]         v3.2 -> v3.2
 * [new tag]         v3.2.1 -> v3.2.1
 * [new tag]         v3.2.1b1 -> v3.2.1b1
 * [new tag]         v3.2.1rc1 -> v3.2.1rc1
 * [new tag]         v3.2.1rc2 -> v3.2.1rc2
 * [new tag]         v3.2.2 -> v3.2.2
 * [new tag]         v3.2.2rc1 -> v3.2.2rc1
 * [new tag]         v3.2.3 -> v3.2.3
 * [new tag]         v3.2.3rc1 -> v3.2.3rc1
 * [new tag]         v3.2.3rc2 -> v3.2.3rc2
 * [new tag]         v3.2.4 -> v3.2.4
 * [new tag]         v3.2.4rc1 -> v3.2.4rc1
 * [new tag]         v3.2.5 -> v3.2.5
 * [new tag]         v3.2.6 -> v3.2.6
 * [new tag]         v3.2.6rc1 -> v3.2.6rc1
 * [new tag]         v3.2a1 -> v3.2a1
 * [new tag]         v3.2a2 -> v3.2a2
 * [new tag]         v3.2a3 -> v3.2a3
 * [new tag]         v3.2a4 -> v3.2a4
 * [new tag]         v3.2b1 -> v3.2b1
 * [new tag]         v3.2b2 -> v3.2b2
 * [new tag]         v3.2rc1 -> v3.2rc1
 * [new tag]         v3.2rc2 -> v3.2rc2
 * [new tag]         v3.2rc3 -> v3.2rc3
 * [new tag]         v3.3.0 -> v3.3.0
 * [new tag]         v3.3.0a1 -> v3.3.0a1
 * [new tag]         v3.3.0a2 -> v3.3.0a2
 * [new tag]         v3.3.0a3 -> v3.3.0a3
 * [new tag]         v3.3.0a4 -> v3.3.0a4
 * [new tag]         v3.3.0b1 -> v3.3.0b1
 * [new tag]         v3.3.0b2 -> v3.3.0b2
 * [new tag]         v3.3.0rc1 -> v3.3.0rc1
 * [new tag]         v3.3.0rc2 -> v3.3.0rc2
 * [new tag]         v3.3.0rc3 -> v3.3.0rc3
 * [new tag]         v3.3.1 -> v3.3.1
 * [new tag]         v3.3.1rc1 -> v3.3.1rc1
 * [new tag]         v3.3.2 -> v3.3.2
 * [new tag]         v3.3.3 -> v3.3.3
 * [new tag]         v3.3.3rc1 -> v3.3.3rc1
 * [new tag]         v3.3.3rc2 -> v3.3.3rc2
 * [new tag]         v3.3.4 -> v3.3.4
 * [new tag]         v3.3.4rc1 -> v3.3.4rc1
 * [new tag]         v3.3.5 -> v3.3.5
 * [new tag]         v3.3.5rc1 -> v3.3.5rc1
 * [new tag]         v3.3.5rc2 -> v3.3.5rc2
 * [new tag]         v3.3.6 -> v3.3.6
 * [new tag]         v3.3.6rc1 -> v3.3.6rc1
 * [new tag]         v3.4.0 -> v3.4.0
 * [new tag]         v3.4.0a1 -> v3.4.0a1
 * [new tag]         v3.4.0a2 -> v3.4.0a2
 * [new tag]         v3.4.0a3 -> v3.4.0a3
 * [new tag]         v3.4.0a4 -> v3.4.0a4
 * [new tag]         v3.4.0b1 -> v3.4.0b1
 * [new tag]         v3.4.0b2 -> v3.4.0b2
 * [new tag]         v3.4.0b3 -> v3.4.0b3
 * [new tag]         v3.4.0rc1 -> v3.4.0rc1
 * [new tag]         v3.4.0rc2 -> v3.4.0rc2
 * [new tag]         v3.4.0rc3 -> v3.4.0rc3
 * [new tag]         v3.4.1 -> v3.4.1
 * [new tag]         v3.4.1rc1 -> v3.4.1rc1
 * [new tag]         v3.4.2 -> v3.4.2
 * [new tag]         v3.4.2rc1 -> v3.4.2rc1
 * [new tag]         v3.4.3 -> v3.4.3
 * [new tag]         v3.4.3rc1 -> v3.4.3rc1
 * [new tag]         v3.4.4 -> v3.4.4
 * [new tag]         v3.4.4rc1 -> v3.4.4rc1
 * [new tag]         v3.5.0 -> v3.5.0
 * [new tag]         v3.5.0a1 -> v3.5.0a1
 * [new tag]         v3.5.0a2 -> v3.5.0a2
 * [new tag]         v3.5.0a3 -> v3.5.0a3
 * [new tag]         v3.5.0a4 -> v3.5.0a4
 * [new tag]         v3.5.0b1 -> v3.5.0b1
 * [new tag]         v3.5.0b2 -> v3.5.0b2
 * [new tag]         v3.5.0b3 -> v3.5.0b3
 * [new tag]         v3.5.0b4 -> v3.5.0b4
 * [new tag]         v3.5.0rc1 -> v3.5.0rc1
 * [new tag]         v3.5.0rc2 -> v3.5.0rc2
 * [new tag]         v3.5.0rc3 -> v3.5.0rc3
 * [new tag]         v3.5.0rc4 -> v3.5.0rc4
 * [new tag]         v3.5.1 -> v3.5.1
 * [new tag]         v3.5.1rc1 -> v3.5.1rc1
```

##### Done

* For e.g, https://github.com/orsenthil/cpython3

If you see any scope for improvement in the tool, please suggest them me. Thank you!

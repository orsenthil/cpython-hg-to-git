### hg to git migration

This repository provides the tool and documents the process involved in migrating the cpython mercurial repository
to git repo.

##### hg_git_migrator.py

[hg_git_migrator.py] is a simple tool that can help with migrating any mercurial repository to github. It uses
mercurial's [hg-git](hg-git.github.io) and automates some steps for easy of use and consistency.

```
python3.6 hg-git-migrator.py local-mercurial-repository empty-github-url
```

>$ python hg-git-migrator.py ~/hg-migration-trials/peps git@github.com:orsenthil/peps.git
>pushing to /Users/senthilkumaran/hg-migration-trials/git-repo/peps
>searching for changes
>adding objects
>added 6299 commits with 6356 trees and 7459 blobs
>Migration completed to git_repo: git@github.com:orsenthil/peps.git

For a large repo like cpython, the migration took **multiple hours** on a fast machine. It is easier and faster to run
migration commands directly for a large repo.

##### cpython migration.

[cpython migration document] enlists the steps required to migrate the repo. These are the commands that
[hg-git-migrator.py] script does it for you.


[hg-git-migrator.py]: https://github.com/orsenthil/cpython-hg-to-git/blob/master/hg_git_migrator.py
[cpython migration document]: https://github.com/orsenthil/cpython-hg-to-git/blob/master/cpython-migration.md

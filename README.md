Task
====

* Evaluate various hg to git repository conversion options and find out the optimal way to convert Cpython hg repository
  at http://hg.python.org to a git repository suitable to be hosted at github.

Constraints
===========

* [PEP-0512](https://www.python.org/dev/peps/pep-0512) defines the various characteristics of the desirable outcome.
* We will want to use an external, well tested tool used by other projects for similar conversion.


Tools
=====

* fast-export

Nicolás Alvarez shared that The fast-export tool started at about 500 revs/sec but progressively slowed down. [1]

* git-remote-hg transport

Oleg Broytman tried this and shared git-remote-hg provides bidirectional transport. You can continue pulling from
Mercurial repository(ies) and you can commit and push back to Mercurial repository(ies).

* hg-git

Ryan Gonzalez tried and shared, hg-git might not work. He cloned the CPython repo and then ran `hg gexport`, which
converts the repository to Git. Took three hours, but it worked!
                                     
However, actually attempted to push the result to a Git repo failed miserably.
After five hours, Mercurial ran out of memory in the "adding objects" stage on a machine with 6GB Ram.

* https://import.github.com/

This tool was introduced by Github. I evaluated this tool to do the migration of http://hg.python.org/cpython repo to gihub.
Unfortunately, it failed at 78% migration. Multiple attempts did not help.  I have raised a ticket with github.com citing unsuccessful migration using their tool.

* [hg-git](http://hg-git.github.io/)

Pierre-Yves David shared that hg-git was used in real world on large sized repositories and works perfectly fine. This led me research this option further.

Migrating using hg-git was successful. Some care was required while navigating this territory and for the initial setup.

  * Hit https://bitbucket.org/durin42/hg-git/issues/93/pushing-to-empty-repository-on-github
    * hg-git migration on empty / initialized repository failed.
    * hg-git migration on local bare git repository was successful
  
  * After migrating to bare git repository, I had to do piecemeal pushes of the initial git repository to github.
  
* Pushing the completely repository fails.

```  
$ git push github master
Counting objects: 574454, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (572378/572378), done.
remote: fatal: pack exceeds maximum allowed size
error: pack-objects died of signal 13
error: failed to push some refs to 'git@github.com:orsenthil/cpython-hg-git-test-4.git'
```

* This was resolved by pushing few commits at a time.

```
$ git push github master~55000:refs/heads/master
$ git push github master~45000:refs/heads/master
$ git push github master~35000:refs/heads/master
$ git push github master~25000:refs/heads/master
$ git push github master~10000:refs/heads/master
$ git push github master~5000:refs/heads/master
$ git push github master:master
$ git push --all github
```



Workflow Suggestions

* http://www.catb.org/esr/reposurgeon/


References
==========

[1]: https://mail.python.org/pipermail/core-workflow/2016-February/000468.html 



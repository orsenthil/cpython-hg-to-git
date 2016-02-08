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


Workflow Suggestions

* http://www.catb.org/esr/reposurgeon/


References
==========

[1]: https://mail.python.org/pipermail/core-workflow/2016-February/000468.html 



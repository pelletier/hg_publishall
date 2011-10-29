Hg-publishall
=============

Hg-publishall is a [mercurial](http://mercurial.selenic.com/) extension which
allows you to push simultaneously to multiple repositories, in a single
command.

Installation
------------

First, clone the repository, let's say in your home directory:

    hg clone ssh://hg@bitbucket.org/Kizlum/hg-publishall ~/hg-publishall

Then add the following to your .hgrc file in order to activate the extension:

    [extensions]
    publishall = /Users/thomas/code/hg-publishall/hg-publishall/publishall.py

And voilà!

Usage
-----

Add as many paths as you want to your repository/.hg/hgrc file, and when you
want to push, use one of the following:

    hg pushall
    hg pusha

Options
-------

As of [r10](https://bitbucket.org/pelletier/hg-publishall/changeset/03300c2a1121)
you can now pass `--new-branch` to the command in order to create remote
branches.

    hg init base
    hg init target1
    hg init target2
    echo -e "[paths]\ntarget1=../target1\ntarget2=../target2" > base/.hg/hgrc
    cd base
    touch bar
    hg commit -A -m "first commit on default"
    hg pushall
    hg branch newbranch
    touch foo
    hg commit -A -m "create a new branch"
    hg pushall # This fails
    hg pushall --new-branch

Tips
----

* Hg-publish plays great with [hg-git](http://hg-git.github.com/).

Get involved
------------

Hg-publishall is licensed under MIT license, so feel free to hack as much as
you wish.

The official repository is on
[Bitbucket](http://bitbucket.org/pelletier/hg-publishall/), but a mirror is
available on [GitHub](http://github.com/pelletier/hg_publishall/).

Finally, if you find a bug, have a feature request or want to submit a patch,
just fill a ticket on the [issues
tracker](http://bitbucket.org/pelletier/hg-publishall/issues).

Contributors
------------

In order of appearance,

* Thomas Pelletier <https://bitbucket.org/pelletier>
* Rémy Hubscher <https://bitbucket.org/natim>
* Thomas R. <https://bitbucket.org/glglgl>
* Bruno Bord <https://bitbucket.org/brunobord>

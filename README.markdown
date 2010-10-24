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

Get involved
------------

Hg-publishall is licensed under MIT license, so feel free to hack as much as
you which.

The official repository is on
[Bitbucket](http://bitbucket.org/Kizlum/hg-publishall/), but a mirror is
available on [GitHub](http://github.com/pelletier/hg_publishall/).

Finally, if you find a bug, have a feature request or want to submit a patch,
just fill a ticket on the [issues
tracker](http://bitbucket.org/Kizlum/hg-publishall/issues).

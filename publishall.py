#!/usr/bin/env python

"""allows you to publish on all your repositories.

Requirements:
mercurial
iniparse: http://iniparse.googlecode.com/files/iniparse-0.3.1.tar.gz

Use:
hg pusha
You can also use hg pushall

Installation:
Add the following entry to the [extensions] bloc of your .hg/hgrc config.
publishall = /path/to/publishall.py
"""

from mercurial.i18n import _
from mercurial import commands, cmdutil, exntesions, hg, util
import ConfigParser, os

def pushall(ui, repo):
    """The Publishall core function. Makes your life easier."""
    userrc = os.sep.join([repo.root, '.hg', 'hgrc'])
    ini = ConfigParser.RawConfigParser()
    ini.read(userrc)
    repos = None
    if not os.path.exists(userrc):
        ui.warn("Unable to find your hgrc file for the current repository.")
        return 1
    try:
        repos = ini.items('paths')
    except KeyError:
        ui.warn("No paths defined in your hgrc. Pushall aborded.")
    ui.status("%s paths found" % len(repos))
    for path in repos:
        ui.status("Pushing to %s" % path[0])
        commands.push(ui, repo, path[1])
    return 0

cmdtable = {
    'pusha': (
        pushall,
        [],
        _("Push to all your repositories."),
    ),

    'pushall': (
        pushall,
        [],
        _("Push to all your repositories (the same as pusha).")
    )
}
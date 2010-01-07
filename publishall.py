#!/usr/bin/env python

"""allows you to publish on all your repositories.

Requirements:
mercurial

Use:
hg pusha
You can also use hg pushall

Installation:
Add the following entry to the [extensions] bloc of your .hg/hgrc config.
publishall = /path/to/publishall.py
"""

from mercurial.i18n import _
from mercurial import commands, cmdutil, extensions, hg, util
import ConfigParser, os

def pushall(ui, repo, **opts):
    """The Publishall core function. Makes your life easier."""
    userrc = os.sep.join([repo.root, '.hg', 'hgrc'])
    ini = ConfigParser.RawConfigParser()
    ini.read(userrc)
    repos = None
    if not os.path.exists(userrc):
        ui.warn("Unable to find your hgrc file for the current repository.\n")
        return 1
    try:
        repos = ini.items('paths')
    except KeyError:
        ui.warn("No paths defined in your hgrc. Pushall aborded.\n")
    ui.status("%s paths found\n" % len(repos))
    for path in repos:
        ui.status("* pushing to %s\n" % path[0])
        try:
            commands.push(ui, repo, path[1], **opts)
        except Exception, e:
            print e
    return 0

aliases = ('pusha','pushall')

command = (
    pushall,
    [],
    _("Push to all your repositories.\n"),
)

cmdtable = {}

# Because I'm SO lazy
for item in aliases:
    cmdtable[item] = command

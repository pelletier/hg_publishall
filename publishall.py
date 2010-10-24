#!/usr/bin/env python

"""Allows you to publish on all your repositories.

Requirements:
    mercurial

Use:
    hg pusha
    You can also use hg pushall

Installation:
    Add the following entry to the [extensions] part of your .hg/hgrc config:
        publishall = /path/to/publishall.py

License:
    MIT (see LICENSE).

For more information, please read the README.markdown file.
"""

from mercurial.i18n import _
from mercurial import commands, cmdutil, extensions, hg, util
import ConfigParser, os

def pushall(ui, repo, **opts):
    """The Publishall core function. Makes your life easier."""
    repos = ui.configitems('paths')
    if not repos:
        ui.warn("No paths defined in your hgrc. Pushall aborted.\n")
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

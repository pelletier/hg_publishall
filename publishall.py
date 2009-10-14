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
from mercurial import commands
import ConfigParser, os

def pushall(hg_ui, repo):
    """The Publishall core function. Makes your life easier."""
    userrc = os.sep.join([repo.root, '.hg', 'hgrc'])
    ini = ConfigParser.RawConfigParser()
    ini.read(userrc)
    repos = None
    if not os.path.exists(userrc):
        hg_ui.warn("Unable to find your hgrc file for the current repository.")
        return 1
    try:
        repos = ini.items('paths')
    except KeyError:
        hg_ui.warn("No paths defined in your hgrc. Pushall aborded.")
    hg_ui.status("%s paths found" % len(repos))
    for path in repos:
        hg_ui.status("Pushing to %s" % path[0])
        commands.push(hg_ui, repo, path[1])
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
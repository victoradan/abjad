# -*- encoding: utf-8 -*-
import os
import sys


def run_abjad():
    r'''Runs Abjad.

    Returns none.
    '''
    from abjad.tools import systemtools
    try:
        file = sys.argv[1]
    except IndexError:
        file = ''
    commands = (
        "from abjad import *;",
        "print abjad_configuration.get_abjad_startup_string();",
        )
    command = r'''python -i {} -c "{}"'''.format(file, ' '.join(commands))
    systemtools.IOManager.spawn_subprocess(command)
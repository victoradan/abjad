# -*- encoding: utf-8 -*-
from abjad import *
import pytest


def test_marktools_LilyPondCommand___init___01():
    r'''Initialize LilyPond command mark from command name.
    '''

    staff = Staff("c'8 d'8 e'8 f'8")
    slur = Slur()
    attach(slur, staff.select_leaves())
    command = marktools.LilyPondCommand(r'slurDotted')
    attach(command, staff[0])

    assert systemtools.TestManager.compare(
        staff,
        r'''
        \new Staff {
            \slurDotted
            c'8 (
            d'8
            e'8
            f'8 )
        }
        '''
        )

    assert inspect(staff).is_well_formed()


def test_marktools_LilyPondCommand___init___02():
    r'''Set LilyPond command mark from command name.
    '''

    staff = Staff("c'8 d'8 e'8 f'8")
    slur = Slur()
    attach(slur, staff.select_leaves())
    command = marktools.LilyPondCommand(r'slurUp')
    attach(command, staff[0])

    assert systemtools.TestManager.compare(
        staff,
        r'''
        \new Staff {
            \slurUp
            c'8 (
            d'8
            e'8
            f'8 )
        }
        '''
        )

    assert inspect(staff).is_well_formed()


def test_marktools_LilyPondCommand___init___03():
    r'''Initialize LilyPond command mark from string and format slot.
    '''

    command = marktools.LilyPondCommand('break', 'closing')
    assert isinstance(command, marktools.LilyPondCommand)


def test_marktools_LilyPondCommand___init___04():
    r'''Initialize LilyPondCommand mark from other LilyPond command mark.
    '''

    command_1 = marktools.LilyPondCommand('break', 'closing')
    command_2 = marktools.LilyPondCommand(command_1)

    assert isinstance(command_1, marktools.LilyPondCommand)
    assert isinstance(command_2, marktools.LilyPondCommand)
    assert command_1 == command_2
    assert command_1 is not command_2
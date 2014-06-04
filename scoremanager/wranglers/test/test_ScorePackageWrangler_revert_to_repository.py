# -*- encoding: utf-8 -*-
from abjad import *
import scoremanager


def test_ScorePackageWrangler_revert_to_repository_01():
    r'''Flow control reaches revert.
    '''

    score_manager = scoremanager.core.AbjadIDE(is_test=True)
    score_manager._session._is_repository_test = True
    input_ = 'rrv <return> q'
    score_manager._run(input_=input_)
    assert score_manager._session._attempted_to_revert_to_repository
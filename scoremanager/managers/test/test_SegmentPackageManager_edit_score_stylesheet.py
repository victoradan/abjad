# -*- encoding: utf-8 -*-
from abjad import *
import scoremanager
score_manager = scoremanager.core.AbjadIDE(is_test=True)


def test_SegmentPackageManager_edit_score_stylesheet_01():

    input_ = 'red~example~score g A sse q'
    score_manager._run(input_=input_)

    assert score_manager._session._attempted_to_open_file
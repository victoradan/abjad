# -*- encoding: utf-8 -*-
from abjad import *
import scoremanager
score_manager = scoremanager.core.AbjadIDE(is_test=True)


def test_ScorePackageManager_rewrite_metadata_py_01():

    input_ = 'red~example~score mdw <return> q'
    score_manager._run(input_=input_)
    contents = score_manager._transcript.contents

    assert 'Will rewrite' in contents
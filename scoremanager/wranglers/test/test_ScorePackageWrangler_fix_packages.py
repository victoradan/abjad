# -*- encoding: utf-8 -*-
from abjad import *
import scoremanager
score_manager = scoremanager.core.AbjadIDE(is_test=True)


def test_ScorePackageWrangler_fix_packages_01():

    input_ = 'fix* q'
    score_manager._run(input_=input_)
    contents = score_manager._transcript.contents

    assert 'No fixes required.' in contents
from experimental import *


def test_UserInputGetter_home_01():

    score_manager = scoremanagertools.scoremanager.ScoreManager()
    score_manager._run(user_input='example~score~i setup performers move home q')
    assert score_manager._session.transcript.signature == (11, (0, 9))

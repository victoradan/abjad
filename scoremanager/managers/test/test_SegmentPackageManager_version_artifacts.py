# -*- encoding: utf-8 -*-
import os
from abjad import *
import scoremanager
score_manager = scoremanager.core.ScoreManager(is_test=True)


def test_SegmentPackageManager_version_artifacts_01():
    
    versions_directory = os.path.join(
        score_manager._configuration.example_score_packages_directory_path,
        'red_example_score',
        'segments',
        'segment_01',
        'versions',
        )
    file_names = (
        '0001.ly',
        '0001.pdf',
        '0001.py',
        )
    paths = []
    for file_name in file_names:
        path = os.path.join(versions_directory, file_name)
        paths.append(path)

    assert not any(os.path.exists(_) for _ in paths)

    try:
        input_ = 'red~example~score g segment~01 ver y q'
        score_manager._run(pending_user_input=input_)
        assert all(os.path.isfile(_) for _ in paths)
    finally:
        for path in paths:
            if os.path.exists(path):
                os.remove(path)

    assert not any(os.path.exists(_) for _ in paths)
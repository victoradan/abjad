# -*- encoding: utf-8 -*-
import os
from abjad import *
import scoremanager


def test_MaterialPackageWrangler_get_available_path_01():

    wrangler = scoremanager.wranglers.MaterialPackageWrangler()
    result = wrangler.get_available_path(pending_user_input='foo')
    path = os.path.join(
        wrangler._configuration.abjad_material_packages_directory_path,
        'foo',
        )
    assert result == path

    result = wrangler.get_available_path(pending_user_input='example~notes q')
    assert result is None


def test_MaterialPackageWrangler_get_available_path_02():

    wrangler = scoremanager.wranglers.MaterialPackageWrangler()
    wrangler._session._current_score_snake_case_name = 'red_example_score'
    result = wrangler.get_available_path(pending_user_input='foo')
    path = os.path.join(
        wrangler._configuration.abjad_score_packages_directory_path,
        'red_example_score',
        'materials',
        'foo',
        )

    assert result == path


def test_MaterialPackageWrangler_get_available_path_03():

    wrangler = scoremanager.wranglers.MaterialPackageWrangler()

    result = wrangler.get_available_path(pending_user_input='q')
    assert result is None

    result = wrangler.get_available_path(pending_user_input='b')
    assert result is None

    result = wrangler.get_available_path(pending_user_input='h')
    assert result is None

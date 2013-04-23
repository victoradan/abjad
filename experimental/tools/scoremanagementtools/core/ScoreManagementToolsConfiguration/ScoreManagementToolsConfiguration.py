import os
from abjad.tools.configurationtools.Configuration import Configuration


class ScoreManagementToolsConfiguration(Configuration):
    '''Score management tools configuration.
    '''

    ### READ-ONLY PRIVATE PROPERTIES ###

    @property
    def _initial_comment(self):
        return []

    @property
    def _option_definitions(self):
        return []

    ### READ-ONLY PUBLIC PROPERTIES ###

    @property
    def CONFIG_DIRECTORY_PATH(self):
        return os.environ.get('SCORE_MANAGEMENT_TOOLS_PATH')

    @property
    def CONFIG_FILE_NAME(self):
        return 'config.py'

    @property
    def boilerplate_directory_name(self):
        return os.path.join(self.score_management_tools_package_path_name, 'boilerplate')

    @property
    def editors_package_importable_name(self):
        return self.dot_join(['scoremanagementtools', 'editors'])

    @property
    def editors_package_path_name(self):
        return os.path.join(os.environ.get('SCORE_MANAGEMENT_TOOLS_PATH'), 'editors')

    @property
    def makers_directory_name(self):
        return os.path.join(self.score_management_tools_package_path_name, 'makers')

    @property
    def makers_package_importable_name(self):
        return self.dot_join([self.score_management_tools_package_importable_name, 'makers'])

    @property
    def score_external_chunks_package_importable_name(self):
        return os.path.basename(os.environ.get('SCORE_MANAGEMENT_TOOLS_CHUNKS_PATH'))

    @property
    def score_external_chunks_package_path_name(self):
        return os.environ.get('SCORE_MANAGEMENT_TOOLS_CHUNKS_PATH')

    @property
    def score_external_materials_package_importable_name(self):
        return os.path.basename(os.environ.get('SCORE_MANAGEMENT_TOOLS_MATERIALS_PATH'))

    @property
    def score_external_materials_package_path_name(self):
        return os.environ.get('SCORE_MANAGEMENT_TOOLS_MATERIALS_PATH')

    @property
    def score_external_package_importable_names(self):
        return (
            self.score_external_chunks_package_importable_name,
            self.score_external_materials_package_importable_name,
            self.score_external_specifiers_package_importable_name,
            )

    @property
    def score_external_package_path_names(self):
        return (
            self.score_external_chunks_package_path_name,
            self.score_external_materials_package_path_name,
            self.score_external_specifiers_package_path_name,
            )

    @property
    def score_external_specifiers_package_importable_name(self):
        return os.path.basename(os.environ.get('SCORE_MANAGEMENT_TOOLS_SPECIFIERS_PATH'))

    @property
    def score_external_specifiers_package_path_name(self):
        return os.environ.get('SCORE_MANAGEMENT_TOOLS_SPECIFIERS_PATH')

    @property
    def score_internal_chunks_package_importable_name_infix(self):
        return 'mus.chunks'

    @property
    def score_internal_materials_package_importable_name_infix(self):
        return 'mus.materials'

    @property
    def score_internal_specifiers_package_importable_name_infix(self):
        return 'mus.specifiers'

    @property
    def score_management_tools_fully_qualified_package_name(self):
        return 'experimental.tools.scoremanagementtools'

    @property
    def score_management_tools_package_importable_name(self):
        return os.path.basename(os.environ.get('SCORE_MANAGEMENT_TOOLS_PATH'))

    @property
    def score_management_tools_package_path_name(self):
        return os.environ.get('SCORE_MANAGEMENT_TOOLS_PATH')

    ### PUBLIC METHODS ###

    def dot_join(self, expr):
        return '.'.join(expr)

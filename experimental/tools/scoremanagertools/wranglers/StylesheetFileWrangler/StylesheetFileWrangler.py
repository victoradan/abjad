import os
from abjad.tools import stringtools
from experimental.tools.scoremanagertools.wranglers.FileWrangler import FileWrangler


class StylesheetFileWrangler(FileWrangler):

    ### INITIALIZER ###

    def __init__(self, session=None):
        FileWrangler.__init__(self,
            system_asset_container_directory_paths=[self.configuration.system_stylesheets_directory_path],
            session=session)

    ### READ-ONLY PRIVATE PROPERTIES ###

    @property
    def _temporary_asset_name(self):
        return '__temporary_stylesheet.ly'

    ### READ-ONLY PUBLIC PROPERTIES ###

    @property
    def asset_class(self):
        from experimental.tools import scoremanagertools
        return scoremanagertools.proxies.StylesheetFileProxy

    @property
    def breadcrumb(self):
        return 'stylesheets'

    # TODO: write test
    @property
    def stylesheet_file_names(self):
        result = []
        for directory_entry in os.listdir(self.configuration.system_stylesheets_directory_path):
            if directory_entry.endswith('.ly'):
                result.append(directory_name)
        return result

    ### PUBLIC METHODS ###

    def handle_main_menu_result(self, result):
        from experimental.tools import scoremanagertools
        if result == 'new':
            self.make_asset_interactively()
        else:
            stylesheet_file_name = os.path.join(self.configuration.system_stylesheets_directory_path, result)
            stylesheet_proxy = scoremanagertools.proxies.StylesheetFileProxy(
                stylesheet_file_name, session=self.session)
            stylesheet_proxy.run()

    # TODO: write test
    def make_asset_interactively(self):
        from experimental.tools import scoremanagertools
        getter = self.io.make_getter(where=self.where())
        getter.append_string('stylesheet name')
        stylesheet_file_name = getter.run()
        if self.session.backtrack():
            return
        stylesheet_file_name = stringtools.string_to_accent_free_underscored_delimited_lowercase(
            stylesheet_file_name)
        if not stylesheet_file_name.endswith('.ly'):
            stylesheet_file_name = stylesheet_file_name + '.ly'
        stylesheet_file_name = os.path.join(
            self.configuration.system_stylesheets_directory_path, stylesheet_file_name)
        stylesheet_proxy = scoremanagertools.proxies.StylesheetFileProxy(
            stylesheet_file_name, session=self.session)
        stylesheet_proxy.edit()

    def make_main_menu(self):
        menu, section = self.io.make_menu(where=self.where(), is_parenthetically_numbered=True)
        section.tokens = self.stylesheet_file_names
        section = menu.make_section()
        section.append(('new', 'new stylesheet'))
        return menu

    # TODO: write test
    def select_stylesheet_file_name_interactively(self, clear=True, cache=False):
        self.session.cache_breadcrumbs(cache=cache)
        menu, section = self.io.make_menu(where=self.where(), is_parenthetically_numbered=True)
        section.tokens = self.stylesheet_file_names
        while True:
            self.session.push_breadcrumb('select stylesheet')
            result = menu.run(clear=clear)
            if self.session.backtrack():
                break
            elif not result:
                self.session.pop_breadcrumb()
                continue
            else:
                break
        self.session.pop_breadcrumb()
        self.session.restore_breadcrumbs(cache=cache)
        result = os.path.join(self.configuration.system_stylesheets_directory_path, result)
        return result

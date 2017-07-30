#!/usr/bin/env python3


class ManageSettings:
    '''
    Settings manager.
    Allows to change main program settings.
    '''

    def __init__(self, **kwargs):
        '''
        Transfer settings into the object.

        Args:
            always_on_top: bool - decides if the window stays always on top of another windows.
                default value: False
            default_screen_resolution: list - default screen resolution.
                default value: [1366, 768]
            screen_horizontal_margin: int - horizontal margin of drawing the window size.
                default value: 15
            screen_vertical_margin: int - vertical margin of drawing the window size.
                default value: 100
            set_screen_resolution: list - set screen resolution by the user.
                default value: [1366, 768]
            window_is_resizable: bool - decides if the window can be resize manually.
                default value: False
        '''

        self.always_on_top = kwargs.get('always_on_top', False)
        self.default_screen_resolution = kwargs.get('default_screen_resolution', [1366, 768])
        self.screen_horizontal_margin = kwargs.get('screen_horizontal_margin', 15)
        self.screen_vertical_margin = kwargs.get('screen_vertical_margin', 100)
        self.set_screen_resolution = kwargs.get('set_screen_resolution', [1366, 768])
        self.window_is_resizable = kwargs.get('window_is_resizable', False)

        self.calculate_additional_settings()

    def calculate_additional_settings(self):
        '''
        Calculates additional settings using provided main settings values.
        '''

        self.screen_width = self.set_screen_resolution[0]
        self.screen_height = self.set_screen_resolution[1]
        self.adjusted_screen_width = self.screen_width - self.screen_horizontal_margin
        self.adjusted_screen_height = self.screen_height - self.screen_vertical_margin

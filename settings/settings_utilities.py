#!/usr/bin/env python3


import os


class SettingsUtilities:

    @staticmethod
    def load_settings_file(settings_path):
        '''
        Load settings file from the directory and read into dictionary.

        Args:
            settings_path: path - absolute path to the folder containing settings file.

        Return:
            dict - containing all the settings.
        '''

        settings_path = settings_path
        settings_full_path = os.path.join(settings_path, 'settings.txt').replace('\\', '/')

        settings = {}

        with open(settings_full_path, 'r') as file_to_read:
            raw_settings = [x.replace('\n', '') for x in file_to_read.readlines()]

        for element in raw_settings:
            key, value = element.split('=')

            if key == 'default_screen_resolution' or key == 'set_screen_resolution':
                settings[key] = [int(y) for y in value.split('x')]

            elif key == 'screen_horizontal_margin' or key == 'screen_vertical_margin':
                settings[key] = int(value)

            elif key == 'always_on_top' or key == 'window_is_resizable':
                if value == 'True':
                    settings[key] = True
                elif value == 'False':
                    settings[key] = False

        return settings

    @staticmethod
    def save_settings_file(settings_path, settings):
        '''
        Gathers all settings and writes the setting files.

        Args:
            settings_path: string - path to the settings file.
            settings: instance - class ManageSettings.

        Return:
            No return in method.
        '''

        settings_path = settings_path
        settings = settings

        settings_to_write = {}
        settings_full_path = os.path.join(settings_path, 'settings.txt').replace('\\', '/')
        redundant_settings = ['screen_width', 'screen_height', 'adjusted_screen_width', 'adjusted_screen_height']

        for key, value in vars(settings).items():
            if key not in redundant_settings:
                settings_to_write[key] = value

        with open(settings_full_path, 'w') as file_to_write:
            for key, value in sorted(settings_to_write.items(), key=str):
                if isinstance(value, list):
                    temp = '{}={}x{}\n'.format(key, value[0], value[1])
                else:
                    temp = '{}={}\n'.format(key, value)

                file_to_write.write(temp)

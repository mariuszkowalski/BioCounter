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
            k, v = element.split('=')

            if k == 'default_screen_resolution' or k == 'set_screen_resolution':
                settings[k] = [int(y) for y in v.split('x')]

            elif k == 'screen_horizontal_margin' or k == 'screen_vertical_margin':
                settings[k] = int(v)

            elif k == 'always_on_top' or k == 'window_is_resizable':
                if v == 'True':
                    settings[k] = True
                elif v == 'False':
                    settings[k] = False

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

        for k, v in vars(settings).items():
            if k not in redundant_settings:
                settings_to_write[k] = v

        with open(settings_full_path, 'w') as file_to_write:
            for k, v in sorted(settings_to_write.items(), key=str):
                if isinstance(v, list):
                    temp = '{}={}x{}\n'.format(k, v[0], v[1])
                else:
                    temp = '{}={}\n'.format(k, v)

                file_to_write.write(temp)


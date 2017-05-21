#!/usr/bin/env python3


class Samples:

    def __init__(self):
        '''
        Holds names for the samples and qualifiers.
        '''
        self.max_button_chars = 3
        self.jpg_quality = 95
        self.png_quality = 7
        self.tif_compression = 'None'

        self.names = {
            1: 'Sample 1',
            2: 'Sample 2',
            3: 'Sample 3',
            4: 'Sample 4',
            5: 'Sample 5',
            6: 'Sample 6',
            7: 'Sample 7',
            8: 'Sample 8'
        }

        self.qualifiers = {
            1: 'X',
            2: 'Y',
            3: 'Z',
            4: 'Q'
        }

        self.qualifiers_button_texts = {}
        for k, v in self.qualifiers.items():
            if len(v) > 3:
                self.qualifiers_button_texts[k] = '{}.'.format(v[:self.max_button_chars])
            else:
                self.qualifiers_button_texts[k] = '{}'.format(v)

        self.colors = {
            1: '#{:02X}{:02X}{:02X}'.format(255, 100, 100),
            2: '#{:02X}{:02X}{:02X}'.format(100, 255, 100),
            3: '#{:02X}{:02X}{:02X}'.format(100, 100, 255),
            4: '#{:02X}{:02X}{:02X}'.format(255, 255, 100),
            5: '#{:02X}{:02X}{:02X}'.format(100, 255, 255),
            6: '#{:02X}{:02X}{:02X}'.format(255, 150, 100),
            7: '#{:02X}{:02X}{:02X}'.format(150, 255, 100),
            8: '#{:02X}{:02X}{:02X}'.format(255, 200, 50)
        }

        self.activated_marker = None

        self.placed_markers = []

    def update_qualifiers(self, temp, qualifier):
        '''
        Update texts of qualifiers and qualifiers_button_texts

        Args:
            temp: dictionary - dictionary with new names
            qualifier: int - key for the dictionary of qualifiers and qualifiers_button_texts
        '''

        base = {
            1: 'X',
            2: 'Y',
            3: 'Z',
            4: 'Q'
        }

        if len(temp[qualifier].strip()) == 0:
            temp[qualifier] = base[qualifier]

        self.qualifiers[qualifier] = temp[qualifier].strip()
        temp[qualifier] = temp[qualifier].strip()

        if len(temp[qualifier]) > self.max_button_chars:
            self.qualifiers_button_texts[qualifier] = '{}.'.format(temp[qualifier][:self.max_button_chars])
        else:
            self.qualifiers_button_texts[qualifier] = '{}'.format(temp[qualifier])

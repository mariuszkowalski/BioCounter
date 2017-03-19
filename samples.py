#!/usr/bin/env python3


class Samples:

    def __init__(self):
        '''
        Holds names for the samples and qualifiers.
        '''

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

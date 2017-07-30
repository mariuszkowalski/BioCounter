#!/usr/bin/env python3


class Statistics:
    '''
    Class used for holding the created in
    software statistics.
    '''

    def __init__(self):
        '''
        Container for all information corresponding to the statistics.
        '''

        self.stats = {
            1: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0
            },
            2: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0
            },
            3: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0
            },
            4: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0
            },
            5: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0
            },
            6: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0
            },
            7: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0
            },
            8: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0
            }
        }

        self.percents = {
            1: {
                1: 0,
                2: 0,
                3: 0,
                4: 0
            },
            2: {
                1: 0,
                2: 0,
                3: 0,
                4: 0
            },
            3: {
                1: 0,
                2: 0,
                3: 0,
                4: 0
            },
            4: {
                1: 0,
                2: 0,
                3: 0,
                4: 0
            },
            5: {
                1: 0,
                2: 0,
                3: 0,
                4: 0
            },
            6: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
            },
            7: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
            },
            8: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
            }
        }

    def change_stat(self, mode, qualifier, increase=True):
        '''
        Method used for registering any change in statistics

        Args:
            mode: int - mode of the marker activated.
                integer in range 1-8
            qualifier: int - qualifier of the marker activated.
                integer in range 1-4
            increase: bool - qualifies if the number statistic
                increases or decreases.
                default: True.
        '''

        if increase:
            self.stats[mode][qualifier] += 1 * 1
        else:
            self.stats[mode][qualifier] += 1 * -1

        self.calculate_all()

    def calculate_all(self):
        '''
        Calculates all the statistics.
        '''

        for k_1 in self.stats.keys():
            # Reset sum value
            self.stats[k_1][5] = 0

            for k_2 in self.stats[k_1].keys():
                if k_2 != 5:
                    self.stats[k_1][5] += self.stats[k_1][k_2]

        for k_1 in self.percents.keys():

            for k_2 in self.percents[k_1].keys():
                if self.stats[k_1][5] > 0:
                    self.percents[k_1][k_2] = round((int(self.stats[k_1][k_2]) / int(self.stats[k_1][5]) * 100), 2)

    def clear_all(self):
        '''
        Clears all the statistics.
        '''

        for k_1 in self.stats.keys():
            for k_2 in self.stats[k_1].keys():
                self.stats[k_1][k_2] = 0

        for k_1 in self.percents.keys():
            for k_2 in self.percents[k_1].keys():
                self.percents[k_1][k_2] = 0

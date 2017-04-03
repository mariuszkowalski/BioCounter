#!/usr/bin/env python3


class Statistics:

    def __init__(self):
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

    def calculate_all(self):
        for k_1 in self.stats.keys():
            # Reset sum value
            self.stats[k_1][5] = 0

            for k_2, v_2 in self.stats[k_1].items():
                if k_2 != 5:
                    self.stats[k_2][5] += v_2

        for k_1 in self.percents.keys():

            for k_2, v_2 in self.percents[k_1].items():
                self.percents[k_1][k_2] = round(int(self.stats[k_1][k_2]) / int(self.stats[k_1][5]), 2)

    def clear_all(self):
        for k_1 in self.stats.keys():
            for k_2 in self.stats[k_1].keys():
                self.stats[k_1][k_2] = 0

        for k_1 in self.percents.keys():
            for k_2 in self.percents[k_1].keys():
                self.percents[k_1][k_2] = 0

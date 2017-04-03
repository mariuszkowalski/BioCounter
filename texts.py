#!/usr/bin/env python3


from tkinter import *


class Texts:
    
    def __init__(self, samples, statistics, widget_geometries):
        self.samples = samples[0]
        self.statistics = statistics[0]
        self.widget_geometries = widget_geometries[0]

        self.marker_size = StringVar()
        self.marker_size.set(self.widget_geometries.marker_size)

        self.sample_1_name = StringVar()
        self.sample_2_name = StringVar()
        self.sample_3_name = StringVar()
        self.sample_4_name = StringVar()
        self.sample_5_name = StringVar()
        self.sample_6_name = StringVar()
        self.sample_7_name = StringVar()
        self.sample_8_name = StringVar()

        self.sample_1_name.set(self.samples.names[1])
        self.sample_2_name.set(self.samples.names[2])
        self.sample_3_name.set(self.samples.names[3])
        self.sample_4_name.set(self.samples.names[4])
        self.sample_5_name.set(self.samples.names[5])
        self.sample_6_name.set(self.samples.names[6])
        self.sample_7_name.set(self.samples.names[7])
        self.sample_8_name.set(self.samples.names[8])

        self.qualifier_1 = StringVar()
        self.qualifier_2 = StringVar()
        self.qualifier_3 = StringVar()
        self.qualifier_4 = StringVar()

        self.qualifier_1.set(self.samples.qualifiers[1])
        self.qualifier_2.set(self.samples.qualifiers[2])
        self.qualifier_3.set(self.samples.qualifiers[3])
        self.qualifier_4.set(self.samples.qualifiers[4])

        self.qualifier_1_button_text = StringVar()
        self.qualifier_2_button_text = StringVar()
        self.qualifier_3_button_text = StringVar()
        self.qualifier_4_button_text = StringVar()

        self.qualifier_1_button_text.set(self.samples.qualifiers_button_texts[1])
        self.qualifier_2_button_text.set(self.samples.qualifiers_button_texts[2])
        self.qualifier_3_button_text.set(self.samples.qualifiers_button_texts[3])
        self.qualifier_4_button_text.set(self.samples.qualifiers_button_texts[4])

        #
        # Statistics tab
        #
        self.quantity_sample_1_qualifier_1 = StringVar()
        self.quantity_sample_1_qualifier_2 = StringVar()
        self.quantity_sample_1_qualifier_3 = StringVar()
        self.quantity_sample_1_qualifier_4 = StringVar()
        self.quantity_sample_1_qualifier_sum = StringVar()

        self.quantity_sample_2_qualifier_1 = StringVar()
        self.quantity_sample_2_qualifier_2 = StringVar()
        self.quantity_sample_2_qualifier_3 = StringVar()
        self.quantity_sample_2_qualifier_4 = StringVar()
        self.quantity_sample_2_qualifier_sum = StringVar()

        self.quantity_sample_3_qualifier_1 = StringVar()
        self.quantity_sample_3_qualifier_2 = StringVar()
        self.quantity_sample_3_qualifier_3 = StringVar()
        self.quantity_sample_3_qualifier_4 = StringVar()
        self.quantity_sample_3_qualifier_sum = StringVar()

        self.quantity_sample_4_qualifier_1 = StringVar()
        self.quantity_sample_4_qualifier_2 = StringVar()
        self.quantity_sample_4_qualifier_3 = StringVar()
        self.quantity_sample_4_qualifier_4 = StringVar()
        self.quantity_sample_4_qualifier_sum = StringVar()

        self.quantity_sample_5_qualifier_1 = StringVar()
        self.quantity_sample_5_qualifier_2 = StringVar()
        self.quantity_sample_5_qualifier_3 = StringVar()
        self.quantity_sample_5_qualifier_4 = StringVar()
        self.quantity_sample_5_qualifier_sum = StringVar()

        self.quantity_sample_6_qualifier_1 = StringVar()
        self.quantity_sample_6_qualifier_2 = StringVar()
        self.quantity_sample_6_qualifier_3 = StringVar()
        self.quantity_sample_6_qualifier_4 = StringVar()
        self.quantity_sample_6_qualifier_sum = StringVar()

        self.quantity_sample_7_qualifier_1 = StringVar()
        self.quantity_sample_7_qualifier_2 = StringVar()
        self.quantity_sample_7_qualifier_3 = StringVar()
        self.quantity_sample_7_qualifier_4 = StringVar()
        self.quantity_sample_7_qualifier_sum = StringVar()

        self.quantity_sample_8_qualifier_1 = StringVar()
        self.quantity_sample_8_qualifier_2 = StringVar()
        self.quantity_sample_8_qualifier_3 = StringVar()
        self.quantity_sample_8_qualifier_4 = StringVar()
        self.quantity_sample_8_qualifier_sum = StringVar()

        self.quantity_sample_1_qualifier_1.set(self.statistics.stats[1][1])
        self.quantity_sample_1_qualifier_2.set(self.statistics.stats[1][2])
        self.quantity_sample_1_qualifier_3.set(self.statistics.stats[1][3])
        self.quantity_sample_1_qualifier_4.set(self.statistics.stats[1][4])
        self.quantity_sample_1_qualifier_sum.set(self.statistics.stats[1][5])

        self.quantity_sample_2_qualifier_1.set(self.statistics.stats[2][1])
        self.quantity_sample_2_qualifier_2.set(self.statistics.stats[2][2])
        self.quantity_sample_2_qualifier_3.set(self.statistics.stats[2][3])
        self.quantity_sample_2_qualifier_4.set(self.statistics.stats[2][4])
        self.quantity_sample_2_qualifier_sum.set(self.statistics.stats[2][5])

        self.quantity_sample_3_qualifier_1.set(self.statistics.stats[3][1])
        self.quantity_sample_3_qualifier_2.set(self.statistics.stats[3][2])
        self.quantity_sample_3_qualifier_3.set(self.statistics.stats[3][3])
        self.quantity_sample_3_qualifier_4.set(self.statistics.stats[3][4])
        self.quantity_sample_3_qualifier_sum.set(self.statistics.stats[3][5])

        self.quantity_sample_4_qualifier_1.set(self.statistics.stats[4][1])
        self.quantity_sample_4_qualifier_2.set(self.statistics.stats[4][2])
        self.quantity_sample_4_qualifier_3.set(self.statistics.stats[4][3])
        self.quantity_sample_4_qualifier_4.set(self.statistics.stats[4][4])
        self.quantity_sample_4_qualifier_sum.set(self.statistics.stats[4][5])

        self.quantity_sample_5_qualifier_1.set(self.statistics.stats[5][1])
        self.quantity_sample_5_qualifier_2.set(self.statistics.stats[5][2])
        self.quantity_sample_5_qualifier_3.set(self.statistics.stats[5][3])
        self.quantity_sample_5_qualifier_4.set(self.statistics.stats[5][4])
        self.quantity_sample_5_qualifier_sum.set(self.statistics.stats[5][5])

        self.quantity_sample_6_qualifier_1.set(self.statistics.stats[6][1])
        self.quantity_sample_6_qualifier_2.set(self.statistics.stats[6][2])
        self.quantity_sample_6_qualifier_3.set(self.statistics.stats[6][3])
        self.quantity_sample_6_qualifier_4.set(self.statistics.stats[6][4])
        self.quantity_sample_6_qualifier_sum.set(self.statistics.stats[6][5])

        self.quantity_sample_7_qualifier_1.set(self.statistics.stats[7][1])
        self.quantity_sample_7_qualifier_2.set(self.statistics.stats[7][2])
        self.quantity_sample_7_qualifier_3.set(self.statistics.stats[7][3])
        self.quantity_sample_7_qualifier_4.set(self.statistics.stats[7][4])
        self.quantity_sample_7_qualifier_sum.set(self.statistics.stats[7][5])

        self.quantity_sample_8_qualifier_1.set(self.statistics.stats[8][1])
        self.quantity_sample_8_qualifier_2.set(self.statistics.stats[8][2])
        self.quantity_sample_8_qualifier_3.set(self.statistics.stats[8][3])
        self.quantity_sample_8_qualifier_4.set(self.statistics.stats[8][4])
        self.quantity_sample_8_qualifier_sum.set(self.statistics.stats[8][5])

        self.quantity_sample_1_qualifier_1_percent = StringVar()
        self.quantity_sample_1_qualifier_2_percent = StringVar()
        self.quantity_sample_1_qualifier_3_percent = StringVar()
        self.quantity_sample_1_qualifier_4_percent = StringVar()

        self.quantity_sample_2_qualifier_1_percent = StringVar()
        self.quantity_sample_2_qualifier_2_percent = StringVar()
        self.quantity_sample_2_qualifier_3_percent = StringVar()
        self.quantity_sample_2_qualifier_4_percent = StringVar()

        self.quantity_sample_3_qualifier_1_percent = StringVar()
        self.quantity_sample_3_qualifier_2_percent = StringVar()
        self.quantity_sample_3_qualifier_3_percent = StringVar()
        self.quantity_sample_3_qualifier_4_percent = StringVar()

        self.quantity_sample_4_qualifier_1_percent = StringVar()
        self.quantity_sample_4_qualifier_2_percent = StringVar()
        self.quantity_sample_4_qualifier_3_percent = StringVar()
        self.quantity_sample_4_qualifier_4_percent = StringVar()

        self.quantity_sample_5_qualifier_1_percent = StringVar()
        self.quantity_sample_5_qualifier_2_percent = StringVar()
        self.quantity_sample_5_qualifier_3_percent = StringVar()
        self.quantity_sample_5_qualifier_4_percent = StringVar()

        self.quantity_sample_6_qualifier_1_percent = StringVar()
        self.quantity_sample_6_qualifier_2_percent = StringVar()
        self.quantity_sample_6_qualifier_3_percent = StringVar()
        self.quantity_sample_6_qualifier_4_percent = StringVar()

        self.quantity_sample_7_qualifier_1_percent = StringVar()
        self.quantity_sample_7_qualifier_2_percent = StringVar()
        self.quantity_sample_7_qualifier_3_percent = StringVar()
        self.quantity_sample_7_qualifier_4_percent = StringVar()

        self.quantity_sample_8_qualifier_1_percent = StringVar()
        self.quantity_sample_8_qualifier_2_percent = StringVar()
        self.quantity_sample_8_qualifier_3_percent = StringVar()
        self.quantity_sample_8_qualifier_4_percent = StringVar()

        self.quantity_sample_1_qualifier_1_percent.set(self.statistics.percents[1][1])
        self.quantity_sample_1_qualifier_2_percent.set(self.statistics.percents[1][2])
        self.quantity_sample_1_qualifier_3_percent.set(self.statistics.percents[1][3])
        self.quantity_sample_1_qualifier_4_percent.set(self.statistics.percents[1][4])

        self.quantity_sample_2_qualifier_1_percent.set(self.statistics.percents[2][1])
        self.quantity_sample_2_qualifier_2_percent.set(self.statistics.percents[2][2])
        self.quantity_sample_2_qualifier_3_percent.set(self.statistics.percents[2][3])
        self.quantity_sample_2_qualifier_4_percent.set(self.statistics.percents[2][4])

        self.quantity_sample_3_qualifier_1_percent.set(self.statistics.percents[3][1])
        self.quantity_sample_3_qualifier_2_percent.set(self.statistics.percents[3][2])
        self.quantity_sample_3_qualifier_3_percent.set(self.statistics.percents[3][3])
        self.quantity_sample_3_qualifier_4_percent.set(self.statistics.percents[3][4])

        self.quantity_sample_4_qualifier_1_percent.set(self.statistics.percents[4][1])
        self.quantity_sample_4_qualifier_2_percent.set(self.statistics.percents[4][2])
        self.quantity_sample_4_qualifier_3_percent.set(self.statistics.percents[4][3])
        self.quantity_sample_4_qualifier_4_percent.set(self.statistics.percents[4][4])

        self.quantity_sample_5_qualifier_1_percent.set(self.statistics.percents[5][1])
        self.quantity_sample_5_qualifier_2_percent.set(self.statistics.percents[5][2])
        self.quantity_sample_5_qualifier_3_percent.set(self.statistics.percents[5][3])
        self.quantity_sample_5_qualifier_4_percent.set(self.statistics.percents[5][4])

        self.quantity_sample_6_qualifier_1_percent.set(self.statistics.percents[6][1])
        self.quantity_sample_6_qualifier_2_percent.set(self.statistics.percents[6][2])
        self.quantity_sample_6_qualifier_3_percent.set(self.statistics.percents[6][3])
        self.quantity_sample_6_qualifier_4_percent.set(self.statistics.percents[6][4])

        self.quantity_sample_7_qualifier_1_percent.set(self.statistics.percents[7][1])
        self.quantity_sample_7_qualifier_2_percent.set(self.statistics.percents[7][2])
        self.quantity_sample_7_qualifier_3_percent.set(self.statistics.percents[7][3])
        self.quantity_sample_7_qualifier_4_percent.set(self.statistics.percents[7][4])

        self.quantity_sample_8_qualifier_1_percent.set(self.statistics.percents[8][1])
        self.quantity_sample_8_qualifier_2_percent.set(self.statistics.percents[8][2])
        self.quantity_sample_8_qualifier_3_percent.set(self.statistics.percents[8][3])
        self.quantity_sample_8_qualifier_4_percent.set(self.statistics.percents[8][4])

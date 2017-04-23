#!/usr/bin/env python3


from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.filedialog import asksaveasfilename
from analysis.export_statistics import ExportStatistics


class Statistics_gui:

    def __init__(self, statistics_tab, widget_geometries, samples, statistics, texts):
        '''
        Building all elements of the analysis menu.

        Args:
            statistics_tab: instance - module Tkinter class ttk.Frame.
            widget_geometries: instance - class Widget_geometries.
            samples: instance - class Samples.
            statistics: instance - class Statistics.
            texts: instance - class Texts.
        '''

        self.statistics_tab = statistics_tab
        self.widget_geometries = widget_geometries[0]
        self.samples = samples[0]
        self.statistics = statistics[0]
        self.texts = texts[0]

        self.filename_to_export = None

        self.statistic_qualifier_sum_text = StringVar()
        self.statistic_qualifier_sum_text.set('Sum')

        #
        # Header
        #
        self.statistics_header_frame = ttk.Frame(
            self.statistics_tab,
            width=self.widget_geometries.sample_frame_width,
            height=30)
        self.statistics_header_frame.place(x=0, y=0)

        self.statistic_qualifier_1 = ttk.Entry(
            self.statistics_header_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.qualifier_1_button_text)
        self.statistic_qualifier_1.place(x=1 * self.widget_geometries.statistics_column_offset, y=5)

        self.statistic_qualifier_2 = ttk.Entry(
            self.statistics_header_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.qualifier_2_button_text)
        self.statistic_qualifier_2.place(x=2 * self.widget_geometries.statistics_column_offset, y=5)

        self.statistic_qualifier_3 = ttk.Entry(
            self.statistics_header_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.qualifier_3_button_text)
        self.statistic_qualifier_3.place(x=3 * self.widget_geometries.statistics_column_offset, y=5)

        self.statistic_qualifier_4 = ttk.Entry(
            self.statistics_header_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.qualifier_4_button_text)
        self.statistic_qualifier_4.place(x=4 * self.widget_geometries.statistics_column_offset, y=5)

        self.statistic_qualifier_sum = ttk.Entry(
            self.statistics_header_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.statistic_qualifier_sum_text)
        self.statistic_qualifier_sum.place(x=5 * self.widget_geometries.statistics_column_offset, y=5)

        #
        # Sample 1
        #
        self.statistics_1_frame = ttk.Frame(
            self.statistics_tab,
            relief=GROOVE,
            width=self.widget_geometries.sample_frame_width,
            height=self.widget_geometries.sample_frame_height)
        self.statistics_1_frame.place(x=0, y=self.widget_geometries.sample_frame_height * 0 + 30)

        self.statistics_1_label = ttk.Label(self.statistics_1_frame, text='S1:')
        self.statistics_1_label.place(
            x=self.widget_geometries.statistics_label_x,
            y=self.widget_geometries.statistics_label_y)

        self.statistics_1_qualifier_1 = ttk.Entry(
            self.statistics_1_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_1_qualifier_1)
        self.statistics_1_qualifier_1.place(
            x=1 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_sample_row_offset)

        self.statistics_1_qualifier_2 = ttk.Entry(
            self.statistics_1_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_1_qualifier_2)
        self.statistics_1_qualifier_2.place(
            x=2 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_sample_row_offset)

        self.statistics_1_qualifier_3 = ttk.Entry(
            self.statistics_1_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_1_qualifier_3)
        self.statistics_1_qualifier_3.place(
            x=3 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_sample_row_offset)

        self.statistics_1_qualifier_4 = ttk.Entry(
            self.statistics_1_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_1_qualifier_4)
        self.statistics_1_qualifier_4.place(
            x=4 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_sample_row_offset)

        self.statistics_1_qualifier_sum = ttk.Entry(
            self.statistics_1_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_1_qualifier_sum)
        self.statistics_1_qualifier_sum.place(
            x=5 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_sample_row_offset)
        #
        self.statistics_1_percent_label = ttk.Label(self.statistics_1_frame, text='%:')
        self.statistics_1_percent_label.place(
            x=self.widget_geometries.statistics_label_x,
            y=self.widget_geometries.statistics_percent_label_y)

        self.statistics_1_qualifier_1_percent = ttk.Entry(
            self.statistics_1_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_1_qualifier_1_percent)
        self.statistics_1_qualifier_1_percent.place(
            x=1 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_percent_row_offset)

        self.statistics_1_qualifier_2_percent = ttk.Entry(
            self.statistics_1_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_1_qualifier_2_percent)
        self.statistics_1_qualifier_2_percent.place(
            x=2 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_percent_row_offset)

        self.statistics_1_qualifier_3_percent = ttk.Entry(
            self.statistics_1_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_1_qualifier_3_percent)
        self.statistics_1_qualifier_3_percent.place(
            x=3 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_percent_row_offset)

        self.statistics_1_qualifier_4_percent = ttk.Entry(
            self.statistics_1_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_1_qualifier_4_percent)
        self.statistics_1_qualifier_4_percent.place(
            x=4 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_percent_row_offset)

        #
        # Sample 2
        #
        self.statistics_2_frame = ttk.Frame(
            self.statistics_tab,
            relief=GROOVE,
            width=self.widget_geometries.sample_frame_width,
            height=self.widget_geometries.sample_frame_height)
        self.statistics_2_frame.place(x=0, y=self.widget_geometries.sample_frame_height * 1 + 30)

        self.statistics_2_label = ttk.Label(self.statistics_2_frame, text='S2:')
        self.statistics_2_label.place(
            x=self.widget_geometries.statistics_label_x,
            y=self.widget_geometries.statistics_label_y)

        self.statistics_2_qualifier_1 = ttk.Entry(
            self.statistics_2_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_2_qualifier_1)
        self.statistics_2_qualifier_1.place(
            x=1 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_sample_row_offset)

        self.statistics_2_qualifier_2 = ttk.Entry(
            self.statistics_2_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_2_qualifier_2)
        self.statistics_2_qualifier_2.place(
            x=2 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_sample_row_offset)

        self.statistics_2_qualifier_3 = ttk.Entry(
            self.statistics_2_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_2_qualifier_3)
        self.statistics_2_qualifier_3.place(
            x=3 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_sample_row_offset)

        self.statistics_2_qualifier_4 = ttk.Entry(
            self.statistics_2_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_2_qualifier_4)
        self.statistics_2_qualifier_4.place(
            x=4 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_sample_row_offset)

        self.statistics_2_qualifier_sum = ttk.Entry(
            self.statistics_2_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_2_qualifier_sum)
        self.statistics_2_qualifier_sum.place(
            x=5 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_sample_row_offset)

        #
        self.statistics_2_percent_label = ttk.Label(self.statistics_2_frame, text='%:')
        self.statistics_2_percent_label.place(
            x=self.widget_geometries.statistics_label_x,
          y=self.widget_geometries.statistics_percent_label_y)

        self.statistics_2_qualifier_1_percent= ttk.Entry(
            self.statistics_2_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_2_qualifier_1_percent)
        self.statistics_2_qualifier_1_percent.place(
            x=1 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_percent_row_offset)

        self.statistics_2_qualifier_2_percent = ttk.Entry(
            self.statistics_2_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_2_qualifier_2_percent)
        self.statistics_2_qualifier_2_percent.place(
            x=2 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_percent_row_offset)

        self.statistics_2_qualifier_3_percent = ttk.Entry(
            self.statistics_2_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_2_qualifier_3_percent)
        self.statistics_2_qualifier_3_percent.place(
            x=3 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_percent_row_offset)

        self.statistics_2_qualifier_4_percent = ttk.Entry(
            self.statistics_2_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_2_qualifier_4_percent)
        self.statistics_2_qualifier_4_percent.place(
            x=4 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_percent_row_offset)

        #
        # Sample 3
        #
        self.statistics_3_frame = ttk.Frame(
            self.statistics_tab,
            relief=GROOVE,
            width=self.widget_geometries.sample_frame_width,
            height=self.widget_geometries.sample_frame_height)
        self.statistics_3_frame.place(x=0, y=self.widget_geometries.sample_frame_height * 2 + 30)

        self.statistics_3_label = ttk.Label(self.statistics_3_frame, text='S3:')
        self.statistics_3_label.place(
            x=self.widget_geometries.statistics_label_x,
            y=self.widget_geometries.statistics_label_y)

        self.statistics_3_qualifier_1 = ttk.Entry(
            self.statistics_3_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_3_qualifier_1)
        self.statistics_3_qualifier_1.place(
            x=1 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_sample_row_offset)

        self.statistics_3_qualifier_2 = ttk.Entry(
            self.statistics_3_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_3_qualifier_2)
        self.statistics_3_qualifier_2.place(
            x=2 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_sample_row_offset)

        self.statistics_3_qualifier_3 = ttk.Entry(
            self.statistics_3_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_3_qualifier_3)
        self.statistics_3_qualifier_3.place(
            x=3 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_sample_row_offset)

        self.statistics_3_qualifier_4 = ttk.Entry(
            self.statistics_3_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_3_qualifier_4)
        self.statistics_3_qualifier_4.place(
            x=4 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_sample_row_offset)

        self.statistics_3_qualifier_sum = ttk.Entry(
            self.statistics_3_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_3_qualifier_sum)
        self.statistics_3_qualifier_sum.place(
            x=5 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_sample_row_offset)

        #
        self.statistics_3_percent_label = ttk.Label(self.statistics_3_frame, text='%:')
        self.statistics_3_percent_label.place(
            x=self.widget_geometries.statistics_label_x,
          y=self.widget_geometries.statistics_percent_label_y)

        self.statistics_3_qualifier_1_percent= ttk.Entry(
            self.statistics_3_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_3_qualifier_1_percent)
        self.statistics_3_qualifier_1_percent.place(
            x=1 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_percent_row_offset)

        self.statistics_3_qualifier_2_percent = ttk.Entry(
            self.statistics_3_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_3_qualifier_2_percent)
        self.statistics_3_qualifier_2_percent.place(
            x=2 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_percent_row_offset)

        self.statistics_3_qualifier_3_percent = ttk.Entry(
            self.statistics_3_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_3_qualifier_3_percent)
        self.statistics_3_qualifier_3_percent.place(
            x=3 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_percent_row_offset)

        self.statistics_3_qualifier_4_percent = ttk.Entry(
            self.statistics_3_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_3_qualifier_4_percent)
        self.statistics_3_qualifier_4_percent.place(
            x=4 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_percent_row_offset)

        #
        # Sample 4
        #
        self.statistics_4_frame = ttk.Frame(
            self.statistics_tab,
            relief=GROOVE,
            width=self.widget_geometries.sample_frame_width,
            height=self.widget_geometries.sample_frame_height)
        self.statistics_4_frame.place(x=0, y=self.widget_geometries.sample_frame_height * 3 + 30)

        self.statistics_4_label = ttk.Label(self.statistics_4_frame, text='S4:')
        self.statistics_4_label.place(
            x=self.widget_geometries.statistics_label_x,
            y=self.widget_geometries.statistics_label_y)

        self.statistics_4_qualifier_1 = ttk.Entry(
            self.statistics_4_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_4_qualifier_1)
        self.statistics_4_qualifier_1.place(
            x=1 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_sample_row_offset)

        self.statistics_4_qualifier_2 = ttk.Entry(
            self.statistics_4_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_4_qualifier_2)
        self.statistics_4_qualifier_2.place(
            x=2 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_sample_row_offset)

        self.statistics_4_qualifier_3 = ttk.Entry(
            self.statistics_4_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_4_qualifier_3)
        self.statistics_4_qualifier_3.place(
            x=3 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_sample_row_offset)

        self.statistics_4_qualifier_4 = ttk.Entry(
            self.statistics_4_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_4_qualifier_4)
        self.statistics_4_qualifier_4.place(
            x=4 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_sample_row_offset)

        self.statistics_4_qualifier_sum = ttk.Entry(
            self.statistics_4_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_4_qualifier_sum)
        self.statistics_4_qualifier_sum.place(
            x=5 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_sample_row_offset)

        #
        self.statistics_4_percent_label = ttk.Label(self.statistics_4_frame, text='%:')
        self.statistics_4_percent_label.place(
            x=self.widget_geometries.statistics_label_x,
            y=self.widget_geometries.statistics_percent_label_y)

        self.statistics_4_qualifier_1_percent= ttk.Entry(
            self.statistics_4_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_4_qualifier_1_percent)
        self.statistics_4_qualifier_1_percent.place(
            x=1 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_percent_row_offset)

        self.statistics_4_qualifier_2_percent = ttk.Entry(
            self.statistics_4_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_4_qualifier_2_percent)
        self.statistics_4_qualifier_2_percent.place(
            x=2 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_percent_row_offset)

        self.statistics_4_qualifier_3_percent = ttk.Entry(
            self.statistics_4_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_4_qualifier_3_percent)
        self.statistics_4_qualifier_3_percent.place(
            x=3 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_percent_row_offset)

        self.statistics_4_qualifier_4_percent = ttk.Entry(
            self.statistics_4_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_4_qualifier_4_percent)
        self.statistics_4_qualifier_4_percent.place(
            x=4 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_percent_row_offset)

        #
        # Sample 5
        #
        self.statistics_5_frame = ttk.Frame(
            self.statistics_tab,
            relief=GROOVE,
            width=self.widget_geometries.sample_frame_width,
            height=self.widget_geometries.sample_frame_height)
        self.statistics_5_frame.place(x=0, y=self.widget_geometries.sample_frame_height * 4 + 30)

        self.statistics_5_label = ttk.Label(self.statistics_5_frame, text='S5:')
        self.statistics_5_label.place(x=self.widget_geometries.statistics_label_x,
                                      y=self.widget_geometries.statistics_label_y)

        self.statistics_5_qualifier_1 = ttk.Entry(
            self.statistics_5_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_5_qualifier_1)
        self.statistics_5_qualifier_1.place(
            x=1 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_sample_row_offset)

        self.statistics_5_qualifier_2 = ttk.Entry(
            self.statistics_5_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_5_qualifier_2)
        self.statistics_5_qualifier_2.place(
            x=2 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_sample_row_offset)

        self.statistics_5_qualifier_3 = ttk.Entry(
            self.statistics_5_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_5_qualifier_3)
        self.statistics_5_qualifier_3.place(
            x=3 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_sample_row_offset)

        self.statistics_5_qualifier_4 = ttk.Entry(
            self.statistics_5_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_5_qualifier_4)
        self.statistics_5_qualifier_4.place(
            x=4 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_sample_row_offset)

        self.statistics_5_qualifier_sum = ttk.Entry(
            self.statistics_5_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_5_qualifier_sum)
        self.statistics_5_qualifier_sum.place(
            x=5 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_sample_row_offset)

        #
        self.statistics_5_percent_label = ttk.Label(self.statistics_5_frame, text='%:')
        self.statistics_5_percent_label.place(
            x=self.widget_geometries.statistics_label_x,
            y=self.widget_geometries.statistics_percent_label_y)

        self.statistics_5_qualifier_1_percent= ttk.Entry(
            self.statistics_5_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_5_qualifier_1_percent)
        self.statistics_5_qualifier_1_percent.place(
            x=1 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_percent_row_offset)

        self.statistics_5_qualifier_2_percent = ttk.Entry(
            self.statistics_5_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_5_qualifier_2_percent)
        self.statistics_5_qualifier_2_percent.place(
            x=2 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_percent_row_offset)

        self.statistics_5_qualifier_3_percent = ttk.Entry(
            self.statistics_5_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_5_qualifier_3_percent)
        self.statistics_5_qualifier_3_percent.place(
            x=3 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_percent_row_offset)

        self.statistics_5_qualifier_4_percent = ttk.Entry(
            self.statistics_5_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_5_qualifier_4_percent)
        self.statistics_5_qualifier_4_percent.place(
            x=4 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_percent_row_offset)

        #
        # Sample 6
        #
        self.statistics_6_frame = ttk.Frame(
            self.statistics_tab,
            relief=GROOVE,
            width=self.widget_geometries.sample_frame_width,
            height=self.widget_geometries.sample_frame_height)
        self.statistics_6_frame.place(x=0, y=self.widget_geometries.sample_frame_height * 5 + 30)

        self.statistics_6_label = ttk.Label(self.statistics_6_frame, text='S6:')
        self.statistics_6_label.place(
            x=self.widget_geometries.statistics_label_x,
            y=self.widget_geometries.statistics_label_y)

        self.statistics_6_qualifier_1 = ttk.Entry(
            self.statistics_6_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_6_qualifier_1)
        self.statistics_6_qualifier_1.place(
            x=1 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_sample_row_offset)

        self.statistics_6_qualifier_2 = ttk.Entry(
            self.statistics_6_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_6_qualifier_2)
        self.statistics_6_qualifier_2.place(
            x=2 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_sample_row_offset)

        self.statistics_6_qualifier_3 = ttk.Entry(
            self.statistics_6_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_6_qualifier_3)
        self.statistics_6_qualifier_3.place(
            x=3 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_sample_row_offset)

        self.statistics_6_qualifier_4 = ttk.Entry(
            self.statistics_6_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_6_qualifier_4)
        self.statistics_6_qualifier_4.place(
            x=4 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_sample_row_offset)

        self.statistics_6_qualifier_sum = ttk.Entry(
            self.statistics_6_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_6_qualifier_sum)
        self.statistics_6_qualifier_sum.place(
            x=5 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_sample_row_offset)

        #
        self.statistics_6_percent_label = ttk.Label(self.statistics_6_frame, text='%:')
        self.statistics_6_percent_label.place(
            x=self.widget_geometries.statistics_label_x,
            y=self.widget_geometries.statistics_percent_label_y)

        self.statistics_6_qualifier_1_percent= ttk.Entry(
            self.statistics_6_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_6_qualifier_1_percent)
        self.statistics_6_qualifier_1_percent.place(
            x=1 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_percent_row_offset)

        self.statistics_6_qualifier_2_percent = ttk.Entry(
            self.statistics_6_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_6_qualifier_2_percent)
        self.statistics_6_qualifier_2_percent.place(
            x=2 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_percent_row_offset)

        self.statistics_6_qualifier_3_percent = ttk.Entry(
            self.statistics_6_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_6_qualifier_3_percent)
        self.statistics_6_qualifier_3_percent.place(
            x=3 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_percent_row_offset)

        self.statistics_6_qualifier_4_percent = ttk.Entry(
            self.statistics_6_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_6_qualifier_4_percent)
        self.statistics_6_qualifier_4_percent.place(
            x=4 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_percent_row_offset)

        #
        # Sample 7
        #
        self.statistics_7_frame = ttk.Frame(
            self.statistics_tab,
            relief=GROOVE,
            width=self.widget_geometries.sample_frame_width,
            height=self.widget_geometries.sample_frame_height)
        self.statistics_7_frame.place(x=0, y=self.widget_geometries.sample_frame_height * 6 + 30)

        self.statistics_7_label = ttk.Label(self.statistics_7_frame, text='S7:')
        self.statistics_7_label.place(
            x=self.widget_geometries.statistics_label_x,
            y=self.widget_geometries.statistics_label_y)

        self.statistics_7_qualifier_1 = ttk.Entry(
            self.statistics_7_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_7_qualifier_1)
        self.statistics_7_qualifier_1.place(
            x=1 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_sample_row_offset)

        self.statistics_7_qualifier_2 = ttk.Entry(
            self.statistics_7_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_7_qualifier_2)
        self.statistics_7_qualifier_2.place(
            x=2 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_sample_row_offset)

        self.statistics_7_qualifier_3 = ttk.Entry(
            self.statistics_7_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_7_qualifier_3)
        self.statistics_7_qualifier_3.place(
            x=3 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_sample_row_offset)

        self.statistics_7_qualifier_4 = ttk.Entry(
            self.statistics_7_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_7_qualifier_4)
        self.statistics_7_qualifier_4.place(
            x=4 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_sample_row_offset)

        self.statistics_7_qualifier_sum = ttk.Entry(
            self.statistics_7_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_7_qualifier_sum)
        self.statistics_7_qualifier_sum.place(
            x=5 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_sample_row_offset)

        #
        self.statistics_7_percent_label = ttk.Label(self.statistics_7_frame, text='%:')
        self.statistics_7_percent_label.place(
            x=self.widget_geometries.statistics_label_x,
            y=self.widget_geometries.statistics_percent_label_y)

        self.statistics_7_qualifier_1_percent= ttk.Entry(
            self.statistics_7_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_7_qualifier_1_percent)
        self.statistics_7_qualifier_1_percent.place(
            x=1 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_percent_row_offset)

        self.statistics_7_qualifier_2_percent = ttk.Entry(
            self.statistics_7_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_7_qualifier_2_percent)
        self.statistics_7_qualifier_2_percent.place(
            x=2 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_percent_row_offset)

        self.statistics_7_qualifier_3_percent = ttk.Entry(
            self.statistics_7_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_7_qualifier_3_percent)
        self.statistics_7_qualifier_3_percent.place(
            x=3 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_percent_row_offset)

        self.statistics_7_qualifier_4_percent = ttk.Entry(
            self.statistics_7_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_7_qualifier_4_percent)
        self.statistics_7_qualifier_4_percent.place(
            x=4 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_percent_row_offset)

        #
        # Sample 8
        #
        self.statistics_8_frame = ttk.Frame(
            self.statistics_tab,
            relief=GROOVE,
            width=self.widget_geometries.sample_frame_width,
            height=self.widget_geometries.sample_frame_height)
        self.statistics_8_frame.place(x=0, y=self.widget_geometries.sample_frame_height * 7 + 30)

        self.statistics_8_label = ttk.Label(self.statistics_8_frame, text='S8:')
        self.statistics_8_label.place(
            x=self.widget_geometries.statistics_label_x,
            y=self.widget_geometries.statistics_label_y)

        self.statistics_8_qualifier_1 = ttk.Entry(
            self.statistics_8_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_8_qualifier_1)
        self.statistics_8_qualifier_1.place(
            x=1 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_sample_row_offset)

        self.statistics_8_qualifier_2 = ttk.Entry(
            self.statistics_8_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_8_qualifier_2)
        self.statistics_8_qualifier_2.place(
            x=2 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_sample_row_offset)

        self.statistics_8_qualifier_3 = ttk.Entry(
            self.statistics_8_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_8_qualifier_3)
        self.statistics_8_qualifier_3.place(
            x=3 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_sample_row_offset)

        self.statistics_8_qualifier_4 = ttk.Entry(
            self.statistics_8_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_8_qualifier_4)
        self.statistics_8_qualifier_4.place(
            x=4 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_sample_row_offset)

        self.statistics_8_qualifier_sum = ttk.Entry(
            self.statistics_8_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_8_qualifier_sum)
        self.statistics_8_qualifier_sum.place(
            x=5 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_sample_row_offset)

        #
        self.statistics_8_percent_label = ttk.Label(self.statistics_8_frame, text='%:')
        self.statistics_8_percent_label.place(
            x=self.widget_geometries.statistics_label_x,
            y=self.widget_geometries.statistics_percent_label_y)

        self.statistics_8_qualifier_1_percent= ttk.Entry(
            self.statistics_8_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_8_qualifier_1_percent)
        self.statistics_8_qualifier_1_percent.place(
            x=1 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_percent_row_offset)

        self.statistics_8_qualifier_2_percent = ttk.Entry(
            self.statistics_8_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_8_qualifier_2_percent)
        self.statistics_8_qualifier_2_percent.place(
            x=2 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_percent_row_offset)

        self.statistics_8_qualifier_3_percent = ttk.Entry(
            self.statistics_8_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_8_qualifier_3_percent)
        self.statistics_8_qualifier_3_percent.place(
            x=3 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_percent_row_offset)

        self.statistics_8_qualifier_4_percent = ttk.Entry(
            self.statistics_8_frame,
            width=5,
            justify=CENTER,
            state='readonly',
            textvariable=self.texts.quantity_sample_8_qualifier_4_percent)
        self.statistics_8_qualifier_4_percent.place(
            x=4 * self.widget_geometries.statistics_column_offset,
            y=self.widget_geometries.statistics_percent_row_offset)

        #
        # Export statistics
        #
        self.export_statistics_frame = ttk.LabelFrame(
            self.statistics_tab,
            relief=GROOVE,
            width=self.widget_geometries.markers_options_frame_width,
            height=self.widget_geometries.markers_options_frame_height,
            text='Export statistics')
        self.export_statistics_frame.place(x=5, y=self.widget_geometries.sample_frame_height * 8 + 30)

        self.decrease_marker_size_button = ttk.Button(
            self.export_statistics_frame,
            width=14,
            text='Export as *.csv')
        self.decrease_marker_size_button.place(x=5, y=0)
        self.decrease_marker_size_button.bind('<Button-1>', self.export_statistics_file)

    def export_statistics_file(self, event):
        allowed_file_types = ['.csv', '.CSV']
        self.filename_to_export = asksaveasfilename(
            defaultextension='.csv',
            filetypes=(('Coma Separated Values', '*.csv *.CSV'), ('All files', '*.*')))

        try:
            if len(self.filename_to_export) > 0 and self.filename_to_export[-4:] not in allowed_file_types:
                raise AttributeError
            elif len(self.filename_to_export) == 0:
                raise OSError

        except AttributeError:
            messagebox.showinfo(message='Not supported file type')

        except OSError:
            messagebox.showinfo(message='Export file not selected')

        else:
            #If everything ok, process with files.
            ExportStatistics.export_to_csv(self.filename_to_export, self.samples, self.statistics)
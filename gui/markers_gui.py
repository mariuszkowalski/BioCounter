#!/usr/bin/env python3


from tkinter import *
from tkinter import ttk
from tkinter.colorchooser import askcolor
from gui.main_gui import Main_gui

class Markers_gui:

    def __init__(self, main_gui, markers_tab, widget_geometries, samples, statistics, texts):
        '''
        Building all elements of the markers menu.

        Args:
            main_gui: instance - class Main_gui from gui.
            markers_tab: instance - module Tkinter class ttk.Frame.
            widget_geometries instance - class Widget_geometries.
            samples: instance - class Samples.
            statistics: instance - class Statistics.
            texts: instance - class Texts.
        '''

        self.main_gui = main_gui
        self.markers_tab = markers_tab
        self.widget_geometries = widget_geometries[0]
        self.samples = samples[0]
        self.statistics = statistics[0]
        self.texts = texts[0]

        #
        # Sample 1
        #
        self.sample_1_frame = ttk.Frame(
            self.markers_tab,
            width=self.widget_geometries.sample_frame_width,
            height=self.widget_geometries.sample_frame_height)
        self.sample_1_frame.place(x=0, y=self.widget_geometries.sample_frame_height * 0)

        self.sample_1_entry = ttk.Entry(
            self.sample_1_frame,
            width=38,
            justify=CENTER,
            textvariable=self.texts.sample_1_name)
        self.sample_1_entry.place(x=5, y=5)
        self.sample_1_entry.bind('<Return>', self.update_samples_names)
        self.sample_1_entry.bind('<FocusOut>', self.update_samples_names)

        self.sample_1_marker_1_button = ttk.Button(
            self.sample_1_frame,
            width=5,
            textvariable=self.texts.qualifier_1_button_text)
        self.sample_1_marker_1_button.place(x=5, y=27)
        self.sample_1_marker_1_button.bind('<Button-1>', lambda event, mode=1,
            qualifier=1: self.activate_marker(event, mode, qualifier))

        self.sample_1_marker_2_button = ttk.Button(
            self.sample_1_frame,
            width=5,
            textvariable=self.texts.qualifier_2_button_text)
        self.sample_1_marker_2_button.place(x=47, y=27)
        self.sample_1_marker_2_button.bind('<Button-1>', lambda event, mode=1,
            qualifier=2: self.activate_marker(event, mode, qualifier))

        self.sample_1_marker_3_button = ttk.Button(
            self.sample_1_frame,
            width=5,
            textvariable=self.texts.qualifier_3_button_text)
        self.sample_1_marker_3_button.place(x=89, y=27)
        self.sample_1_marker_3_button.bind('<Button-1>', lambda event, mode=1,
            qualifier=3: self.activate_marker(event, mode, qualifier))

        self.sample_1_marker_4_button = ttk.Button(
            self.sample_1_frame,
            width=5,
            textvariable=self.texts.qualifier_4_button_text)
        self.sample_1_marker_4_button.place(x=131, y=27)
        self.sample_1_marker_4_button.bind('<Button-1>', lambda event, mode=1,
            qualifier=4: self.activate_marker(event, mode, qualifier))

        self.color_1_label = ttk.Label(self.sample_1_frame, text='Color:')
        self.color_1_label.place(x=173, y=30)

        self.sample_1_color = Label(self.sample_1_frame, width=3, bg=self.samples.colors[1])
        self.sample_1_color.place(x=210, y=29)
        self.sample_1_color.bind('<Button-1>', lambda event, mode=1: self.choose_marker_color(event, mode))

        #
        # Sample 2
        #
        self.sample_2_frame = ttk.Frame(
            self.markers_tab,
            width=self.widget_geometries.sample_frame_width,
            height=self.widget_geometries.sample_frame_height)
        self.sample_2_frame.place(x=0, y=self.widget_geometries.sample_frame_height * 1)

        self.sample_2_entry = ttk.Entry(
            self.sample_2_frame,
            width=38,
            justify=CENTER,
            textvariable=self.texts.sample_2_name)
        self.sample_2_entry.place(x=5, y=5)
        self.sample_2_entry.bind('<Return>', self.update_samples_names)
        self.sample_2_entry.bind('<FocusOut>', self.update_samples_names)

        self.sample_2_marker_1_button = ttk.Button(
            self.sample_2_frame,
            width=5,
            textvariable=self.texts.qualifier_1_button_text)
        self.sample_2_marker_1_button.place(x=5, y=27)
        self.sample_2_marker_1_button.bind('<Button-1>', lambda event, mode=2, qualifier=1,
            color=self.samples.colors[2]: self.activate_marker(event, mode, qualifier))

        self.sample_2_marker_2_button = ttk.Button(
            self.sample_2_frame,
            width=5,
            textvariable=self.texts.qualifier_2_button_text)
        self.sample_2_marker_2_button.place(x=47, y=27)
        self.sample_2_marker_2_button.bind('<Button-1>', lambda event, mode=2,
            qualifier=2: self.activate_marker(event, mode, qualifier))

        self.sample_2_marker_3_button = ttk.Button(
            self.sample_2_frame,
            width=5,
            textvariable=self.texts.qualifier_3_button_text)
        self.sample_2_marker_3_button.place(x=89, y=27)
        self.sample_2_marker_3_button.bind('<Button-1>', lambda event, mode=2, qualifier=3,
            color=self.samples.colors[2]: self.activate_marker(event, mode, qualifier))

        self.sample_2_marker_4_button = ttk.Button(
            self.sample_2_frame,
            width=5,
            textvariable=self.texts.qualifier_4_button_text)
        self.sample_2_marker_4_button.place(x=131, y=27)
        self.sample_2_marker_4_button.bind('<Button-1>', lambda event, mode=2,
            qualifier=4: self.activate_marker(event, mode, qualifier))

        self.color_2_label = ttk.Label(self.sample_2_frame, text='Color:')
        self.color_2_label.place(x=173, y=30)

        self.sample_2_color = Label(self.sample_2_frame, width=3, bg=self.samples.colors[2])
        self.sample_2_color.place(x=210, y=29)
        self.sample_2_color.bind('<Button-1>', lambda event, mode=2: self.choose_marker_color(event, mode))

        #
        # Sample 3
        #
        self.sample_3_frame = ttk.Frame(
            self.markers_tab,
            width=self.widget_geometries.sample_frame_width,
            height=self.widget_geometries.sample_frame_height)
        self.sample_3_frame.place(x=0, y=self.widget_geometries.sample_frame_height * 2)

        self.sample_3_entry = ttk.Entry(
            self.sample_3_frame,
            width=38,
            justify=CENTER,
            textvariable=self.texts.sample_3_name)
        self.sample_3_entry.place(x=5, y=5)
        self.sample_3_entry.bind('<Return>', self.update_samples_names)
        self.sample_3_entry.bind('<FocusOut>', self.update_samples_names)

        self.sample_3_marker_1_button = ttk.Button(
            self.sample_3_frame,
            width=5,
            textvariable=self.texts.qualifier_1_button_text)
        self.sample_3_marker_1_button.place(x=5, y=27)
        self.sample_3_marker_1_button.bind('<Button-1>', lambda event, mode=3,
            qualifier=1: self.activate_marker(event, mode, qualifier))

        self.sample_3_marker_2_button = ttk.Button(
            self.sample_3_frame,
            width=5,
            textvariable=self.texts.qualifier_2_button_text)
        self.sample_3_marker_2_button.place(x=47, y=27)
        self.sample_3_marker_2_button.bind('<Button-1>', lambda event, mode=3,
            qualifier=2: self.activate_marker(event, mode, qualifier))


        self.sample_3_marker_3_button = ttk.Button(
            self.sample_3_frame,
            width=5,
            textvariable=self.texts.qualifier_3_button_text)
        self.sample_3_marker_3_button.place(x=89, y=27)
        self.sample_3_marker_3_button.bind('<Button-1>', lambda event, mode=3,
            qualifier=3:self.activate_marker(event, mode, qualifier))

        self.sample_3_marker_4_button = ttk.Button(
            self.sample_3_frame,
            width=5,
            textvariable=self.texts.qualifier_4_button_text)
        self.sample_3_marker_4_button.place(x=131, y=27)
        self.sample_3_marker_4_button.bind('<Button-1>', lambda event, mode=3,
            qualifier=4: self.activate_marker(event, mode, qualifier))

        self.color_3_label = ttk.Label(self.sample_3_frame, text='Color:')
        self.color_3_label.place(x=173, y=30)

        self.sample_3_color = Label(self.sample_3_frame, width=3, bg=self.samples.colors[3])
        self.sample_3_color.place(x=210, y=29)
        self.sample_3_color.bind('<Button-1>', lambda event, mode=3: self.choose_marker_color(event, mode))

        #
        # Sample 4
        #
        self.sample_4_frame = ttk.Frame(
            self.markers_tab,
            width=self.widget_geometries.sample_frame_width,
            height=self.widget_geometries.sample_frame_height)
        self.sample_4_frame.place(x=0, y=self.widget_geometries.sample_frame_height * 3)

        self.sample_4_entry = ttk.Entry(
            self.sample_4_frame,
            width=38,
            justify=CENTER,
            textvariable=self.texts.sample_4_name)
        self.sample_4_entry.place(x=5, y=5)
        self.sample_4_entry.bind('<Return>', self.update_samples_names)
        self.sample_4_entry.bind('<FocusOut>', self.update_samples_names)

        self.sample_4_marker_1_button = ttk.Button(
            self.sample_4_frame,
            width=5,
            textvariable=self.texts.qualifier_1_button_text)
        self.sample_4_marker_1_button.place(x=5, y=27)
        self.sample_4_marker_1_button.bind('<Button-1>', lambda event, mode=4,
            qualifier=1: self.activate_marker(event, mode, qualifier))

        self.sample_4_marker_2_button = ttk.Button(
            self.sample_4_frame,
            width=5,
            textvariable=self.texts.qualifier_2_button_text)
        self.sample_4_marker_2_button.place(x=47, y=27)
        self.sample_4_marker_2_button.bind('<Button-1>', lambda event, mode=4,
            qualifier=2: self.activate_marker(event, mode, qualifier))

        self.sample_4_marker_3_button = ttk.Button(
            self.sample_4_frame,
            width=5,
            textvariable=self.texts.qualifier_3_button_text)
        self.sample_4_marker_3_button.place(x=89, y=27)
        self.sample_4_marker_3_button.bind('<Button-1>', lambda event, mode=4,
            qualifier=3: self.activate_marker(event, mode, qualifier))

        self.sample_4_marker_4_button = ttk.Button(
            self.sample_4_frame,
            width=5,
            textvariable=self.texts.qualifier_4_button_text)
        self.sample_4_marker_4_button.place(x=131, y=27)
        self.sample_4_marker_4_button.bind('<Button-1>', lambda event, mode=4,
            qualifier=4: self.activate_marker(event, mode, qualifier))

        self.color_4_label = ttk.Label(self.sample_4_frame, text='Color:')
        self.color_4_label.place(x=173, y=30)

        self.sample_4_color = Label(self.sample_4_frame, width=3, bg=self.samples.colors[4])
        self.sample_4_color.place(x=210, y=29)
        self.sample_4_color.bind('<Button-1>', lambda event, mode=4: self.choose_marker_color(event, mode))

        #
        # Sample 5
        #
        self.sample_5_frame = ttk.Frame(
            self.markers_tab,
            width=self.widget_geometries.sample_frame_width,
            height=self.widget_geometries.sample_frame_height)
        self.sample_5_frame.place(x=0, y=self.widget_geometries.sample_frame_height * 4)

        self.sample_5_entry = ttk.Entry(
            self.sample_5_frame,
            width=38,
            justify=CENTER,
            textvariable=self.texts.sample_5_name)
        self.sample_5_entry.place(x=5, y=5)
        self.sample_5_entry.bind('<Return>', self.update_samples_names)
        self.sample_5_entry.bind('<FocusOut>', self.update_samples_names)

        self.sample_5_marker_1_button = ttk.Button(
            self.sample_5_frame,
            width=5,
            textvariable=self.texts.qualifier_1_button_text)
        self.sample_5_marker_1_button.place(x=5, y=27)
        self.sample_5_marker_1_button.bind('<Button-1>', lambda event, mode=5,
            qualifier=1: self.activate_marker(event, mode, qualifier))

        self.sample_5_marker_2_button = ttk.Button(
            self.sample_5_frame,
            width=5,
            textvariable=self.texts.qualifier_2_button_text)
        self.sample_5_marker_2_button.place(x=47, y=27)
        self.sample_5_marker_2_button.bind('<Button-1>', lambda event, mode=5,
            qualifier=2: self.activate_marker(event, mode, qualifier))

        self.sample_5_marker_3_button = ttk.Button(
            self.sample_5_frame,
            width=5,
            textvariable=self.texts.qualifier_3_button_text)
        self.sample_5_marker_3_button.place(x=89, y=27)
        self.sample_5_marker_3_button.bind('<Button-1>', lambda event, mode=5,
            qualifier=3: self.activate_marker(event, mode, qualifier))

        self.sample_5_marker_4_button = ttk.Button(
            self.sample_5_frame,
            width=5,
            textvariable=self.texts.qualifier_4_button_text)
        self.sample_5_marker_4_button.place(x=131, y=27)
        self.sample_5_marker_4_button.bind('<Button-1>', lambda event, mode=5,
            qualifier=4: self.activate_marker(event, mode, qualifier))

        self.color_5_label = ttk.Label(self.sample_5_frame, text='Color:')
        self.color_5_label.place(x=173, y=30)

        self.sample_5_color = Label(self.sample_5_frame, width=3, bg=self.samples.colors[5])
        self.sample_5_color.place(x=210, y=29)
        self.sample_5_color.bind('<Button-1>', lambda event, mode=5: self.choose_marker_color(event, mode))

        #
        # Sample 6
        #
        self.sample_6_frame = ttk.Frame(
            self.markers_tab,
            width=self.widget_geometries.sample_frame_width,
            height=self.widget_geometries.sample_frame_height)
        self.sample_6_frame.place(x=0, y=self.widget_geometries.sample_frame_height * 5)

        self.sample_6_entry = ttk.Entry(
            self.sample_6_frame,
            width=38,
            justify=CENTER,
            textvariable=self.texts.sample_6_name)
        self.sample_6_entry.place(x=5, y=5)
        self.sample_6_entry.bind('<Return>', self.update_samples_names)
        self.sample_6_entry.bind('<FocusOut>', self.update_samples_names)

        self.sample_6_marker_1_button = ttk.Button(
            self.sample_6_frame,
            width=5,
            textvariable=self.texts.qualifier_1_button_text)
        self.sample_6_marker_1_button.place(x=5, y=27)
        self.sample_6_marker_1_button.bind('<Button-1>', lambda event, mode=6,
            qualifier=1: self.activate_marker(event, mode, qualifier))

        self.sample_6_marker_2_button = ttk.Button(
            self.sample_6_frame,
            width=5,
            textvariable=self.texts.qualifier_2_button_text)
        self.sample_6_marker_2_button.place(x=47, y=27)
        self.sample_6_marker_2_button.bind('<Button-1>', lambda event, mode=6,
            qualifier=2: self.activate_marker(event, mode, qualifier))

        self.sample_6_marker_3_button = ttk.Button(
            self.sample_6_frame,
            width=5,
            textvariable=self.texts.qualifier_3_button_text)
        self.sample_6_marker_3_button.place(x=89, y=27)
        self.sample_6_marker_3_button.bind('<Button-1>', lambda event, mode=6,
            qualifier=3: self.activate_marker(event, mode, qualifier))

        self.sample_6_marker_4_button = ttk.Button(
            self.sample_6_frame,
            width=5,
            textvariable=self.texts.qualifier_4_button_text)
        self.sample_6_marker_4_button.place(x=131, y=27)
        self.sample_6_marker_4_button.bind('<Button-1>', lambda event, mode=6,
            qualifier=4: self.activate_marker(event, mode, qualifier))

        self.color_6_label = ttk.Label(self.sample_6_frame, text='Color:')
        self.color_6_label.place(x=173, y=30)

        self.sample_6_color = Label(self.sample_6_frame, width=3, bg=self.samples.colors[6])
        self.sample_6_color.place(x=210, y=29)
        self.sample_6_color.bind('<Button-1>', lambda event, mode=6: self.choose_marker_color(event, mode))

        #
        # Sample 7
        #
        self.sample_7_frame = ttk.Frame(
            self.markers_tab,
            width=self.widget_geometries.sample_frame_width,
            height=self.widget_geometries.sample_frame_height)
        self.sample_7_frame.place(x=0, y=self.widget_geometries.sample_frame_height * 6)

        self.sample_7_entry = ttk.Entry(
            self.sample_7_frame,
            width=38,
            justify=CENTER,
            textvariable=self.texts.sample_7_name)
        self.sample_7_entry.place(x=5, y=5)
        self.sample_7_entry.bind('<Return>', self.update_samples_names)
        self.sample_7_entry.bind('<FocusOut>', self.update_samples_names)

        self.sample_7_marker_1_button = ttk.Button(
            self.sample_7_frame,
            width=5,
            textvariable=self.texts.qualifier_1_button_text)
        self.sample_7_marker_1_button.place(x=5, y=27)
        self.sample_7_marker_1_button.bind('<Button-1>', lambda event, mode=7,
            qualifier=1: self.activate_marker(event, mode, qualifier))

        self.sample_7_marker_2_button = ttk.Button(
            self.sample_7_frame,
            width=5,
            textvariable=self.texts.qualifier_2_button_text)
        self.sample_7_marker_2_button.place(x=47, y=27)
        self.sample_7_marker_2_button.bind('<Button-1>', lambda event, mode=7,
            qualifier=2: self.activate_marker(event, mode, qualifier))

        self.sample_7_marker_3_button = ttk.Button(
            self.sample_7_frame,
            width=5,
            textvariable=self.texts.qualifier_3_button_text)
        self.sample_7_marker_3_button.place(x=89, y=27)
        self.sample_7_marker_3_button.bind('<Button-1>', lambda event, mode=7,
            qualifier=3: self.activate_marker(event, mode, qualifier))

        self.sample_7_marker_4_button = ttk.Button(
            self.sample_7_frame,
            width=5,
            textvariable=self.texts.qualifier_4_button_text)
        self.sample_7_marker_4_button.place(x=131, y=27)
        self.sample_7_marker_4_button.bind('<Button-1>', lambda event, mode=7,
            qualifier=4: self.activate_marker(event, mode, qualifier))

        self.color_7_label = ttk.Label(self.sample_7_frame, text='Color:')
        self.color_7_label.place(x=173, y=30)

        self.sample_7_color = Label(self.sample_7_frame, width=3, bg=self.samples.colors[7])
        self.sample_7_color.place(x=210, y=29)
        self.sample_7_color.bind('<Button-1>', lambda event, mode=7: self.choose_marker_color(event, mode))

        #
        # Sample 8
        #
        self.sample_8_frame = ttk.Frame(
            self.markers_tab,
            width=self.widget_geometries.sample_frame_width,
            height=self.widget_geometries.sample_frame_height)
        self.sample_8_frame.place(x=0, y=self.widget_geometries.sample_frame_height * 7)

        self.sample_8_entry = ttk.Entry(
            self.sample_8_frame,
            width=38,
            justify=CENTER,
            textvariable=self.texts.sample_8_name)
        self.sample_8_entry.place(x=5, y=5)
        self.sample_8_entry.bind('<Return>', self.update_samples_names)
        self.sample_8_entry.bind('<FocusOut>', self.update_samples_names)

        self.sample_8_marker_1_button = ttk.Button(
            self.sample_8_frame,
            width=5,
            textvariable=self.texts.qualifier_1_button_text)
        self.sample_8_marker_1_button.place(x=5, y=27)
        self.sample_8_marker_1_button.bind('<Button-1>', lambda event, mode=8,
            qualifier=1: self.activate_marker(event, mode, qualifier))

        self.sample_8_marker_2_button = ttk.Button(
            self.sample_8_frame,
            width=5,
            textvariable=self.texts.qualifier_2_button_text)
        self.sample_8_marker_2_button.place(x=47, y=27)
        self.sample_8_marker_2_button.bind('<Button-1>', lambda event, mode=8,
            qualifier=2: self.activate_marker(event, mode, qualifier))

        self.sample_8_marker_3_button = ttk.Button(
            self.sample_8_frame,
            width=5,
            textvariable=self.texts.qualifier_3_button_text)
        self.sample_8_marker_3_button.place(x=89, y=27)
        self.sample_8_marker_3_button.bind('<Button-1>', lambda event, mode=8,
            qualifier=3: self.activate_marker(event, mode, qualifier))

        self.sample_8_marker_4_button = ttk.Button(
            self.sample_8_frame,
            width=5,
            textvariable=self.texts.qualifier_4_button_text)
        self.sample_8_marker_4_button.place(x=131, y=27)
        self.sample_8_marker_4_button.bind('<Button-1>', lambda event, mode=8,
            qualifier=4: self.activate_marker(event, mode, qualifier))

        self.color_8_label = ttk.Label(self.sample_8_frame, text='Color:')
        self.color_8_label.place(x=173, y=30)

        self.sample_8_color = Label(self.sample_8_frame, width=3, bg=self.samples.colors[8])
        self.sample_8_color.place(x=210, y=29)
        self.sample_8_color.bind('<Button-1>', lambda event, mode=8: self.choose_marker_color(event, mode))

        # Clear markers button
        self.clear_all_markers_frame = ttk.Frame(
            self.markers_tab,
            width=self.widget_geometries.clear_all_markers_frame_width,
            height=self.widget_geometries.clear_all_markers_frame_height)
        self.clear_all_markers_frame.place(x=0, y=(self.widget_geometries.sample_frame_height * 8) + 5)

        self.clear_all_markers_button = ttk.Button(
            self.clear_all_markers_frame,
            width=30,
            text='Clear all markers')
        self.clear_all_markers_button.place(x=24, y=2)
        self.clear_all_markers_button.bind('<Button-1>', self.clear_all_markers)

        # Dictionary of elements.
        self.samples_and_markers_buttons = {
            'sample_1_marker_1_button': self.sample_1_marker_1_button,
            'sample_1_marker_2_button': self.sample_1_marker_2_button,
            'sample_1_marker_3_button': self.sample_1_marker_3_button,
            'sample_1_marker_4_button': self.sample_1_marker_4_button,
            'sample_2_marker_1_button': self.sample_2_marker_1_button,
            'sample_2_marker_2_button': self.sample_2_marker_2_button,
            'sample_2_marker_3_button': self.sample_2_marker_3_button,
            'sample_2_marker_4_button': self.sample_2_marker_4_button,
            'sample_3_marker_1_button': self.sample_3_marker_1_button,
            'sample_3_marker_2_button': self.sample_3_marker_2_button,
            'sample_3_marker_3_button': self.sample_3_marker_3_button,
            'sample_3_marker_4_button': self.sample_3_marker_4_button,
            'sample_4_marker_1_button': self.sample_4_marker_1_button,
            'sample_4_marker_2_button': self.sample_4_marker_2_button,
            'sample_4_marker_3_button': self.sample_4_marker_3_button,
            'sample_4_marker_4_button': self.sample_4_marker_4_button,
            'sample_5_marker_1_button': self.sample_5_marker_1_button,
            'sample_5_marker_2_button': self.sample_5_marker_2_button,
            'sample_5_marker_3_button': self.sample_5_marker_3_button,
            'sample_5_marker_4_button': self.sample_5_marker_4_button,
            'sample_6_marker_1_button': self.sample_6_marker_1_button,
            'sample_6_marker_2_button': self.sample_6_marker_2_button,
            'sample_6_marker_3_button': self.sample_6_marker_3_button,
            'sample_6_marker_4_button': self.sample_6_marker_4_button,
            'sample_7_marker_1_button': self.sample_7_marker_1_button,
            'sample_7_marker_2_button': self.sample_7_marker_2_button,
            'sample_7_marker_3_button': self.sample_7_marker_3_button,
            'sample_7_marker_4_button': self.sample_7_marker_4_button,
            'sample_8_marker_1_button': self.sample_8_marker_1_button,
            'sample_8_marker_2_button': self.sample_8_marker_2_button,
            'sample_8_marker_3_button': self.sample_8_marker_3_button,
            'sample_8_marker_4_button': self.sample_8_marker_4_button
        }

        self.samples_colors = {
            1: self.sample_1_color,
            2: self.sample_2_color,
            3: self.sample_3_color,
            4: self.sample_4_color,
            5: self.sample_5_color,
            6: self.sample_6_color,
            7: self.sample_7_color,
            8: self.sample_8_color
        }

    def activate_marker(self, event, mode, qualifier):
        '''
        Registers which marker button has been pressed and holds information necessary
        to place correct marker in the canvas.

        Args:
            mode: int - mode of the marker activated.
                integer in range 1-8
            qualifier: int - qualifier of the marker activated.
                integer in range 1-4

        Return:
            No return in the method.
        '''

        for k, v in self.samples_and_markers_buttons.items():
            if k == 'sample_{}_marker_{}_button'.format(mode, qualifier):
                v.state(['disabled'])
            else:
                v.state(['!disabled'])

        self.samples.activated_marker = {
            'mode': mode,
            'qualifier': qualifier,
            'color': self.samples.colors[mode]
        }

    def choose_marker_color(self, event, mode):
        '''
        Activates the pick color dialog box and assigns the choose color to
        the given marker. Calls for redraw of all the markers that has been
        assigned the new color.

        Args:
            mode: int - mode of the marker activated.
                integer in range 1-8

        Return:
            No return in the method.
        '''

        new_color = askcolor()[1]

        if new_color:
            self.samples.colors[mode] = new_color

            for k, v in self.samples_colors.items():
                if k == mode:
                    print('Found: {}'.format(mode))
                    v.configure(bg=new_color)

        self.main_gui.replace_markers_of_changed_color(mode)

        # Update color in the activated marker.
        if self.samples.activated_marker and self.samples.activated_marker['mode'] == mode:
            self.samples.activated_marker['color'] = new_color

    def clear_all_markers(self, event):
        '''
        Clears all markers from the canvas and all other elements.
        '''

        self.main_gui.clear_all_markers_from_canvas()

    def update_samples_names(self, event):
        '''
        Updates the samples names assigned in the Entry fields.
        '''

        self.samples.names[1] = self.texts.sample_1_name.get()
        self.samples.names[2] = self.texts.sample_2_name.get()
        self.samples.names[3] = self.texts.sample_3_name.get()
        self.samples.names[4] = self.texts.sample_4_name.get()
        self.samples.names[5] = self.texts.sample_5_name.get()
        self.samples.names[6] = self.texts.sample_6_name.get()
        self.samples.names[7] = self.texts.sample_7_name.get()
        self.samples.names[8] = self.texts.sample_8_name.get()

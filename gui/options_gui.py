#!/usr/bin/env python3


from tkinter import *
from tkinter import ttk


class Options_gui:

    def __init__(self, main_gui, options_tab, widget_geometries, samples, texts):
        '''
        Building all elements of the options menu.

        Args:
            main_gui: instance - class Main_gui from gui.
            options_tab: instance - module Tkinter class ttk.Frame.
            widget_geometries: instance - class Widget_geometries.
            samples: instance - class Samples.
            texts: instance - class Texts.
        '''

        self.main_gui = main_gui
        self.options_tab = options_tab
        self.widget_geometries = widget_geometries[0]
        self.samples = samples[0]
        self.texts = texts[0]

        # Qualifier 1
        self.qualifiers_options_frame = ttk.LabelFrame(
            self.options_tab,
            width=self.widget_geometries.qualifiers_options_frame_width,
            height=self.widget_geometries.qualifiers_options_frame_height,
            text='Change qualifiers')
        self.qualifiers_options_frame.place(x=5, y=5)

        self.qualifier_1_frame = ttk.Frame(
            self.qualifiers_options_frame,
            width=self.widget_geometries.qualifier_single_frame_width,
            height=self.widget_geometries.qualifier_single_frame_height)
        self.qualifier_1_frame.place(x=2, y=2 + 0 * self.widget_geometries.qualifier_single_frame_spacing)

        self.qualifier_1_label = ttk.Label(self.qualifier_1_frame, text='Qualifier 1:')
        self.qualifier_1_label.place(x=5, y=0)

        self.qualifier_1_entry = ttk.Entry(
            self.qualifier_1_frame,
            width=35,
            justify=CENTER,
            textvariable=self.texts.qualifier_1)
        self.qualifier_1_entry.place(x=5, y=20)
        self.qualifier_1_entry.bind('<Return>', lambda event, qualifier=1: self.update_qualifiers(event, qualifier))
        self.qualifier_1_entry.bind('<FocusOut>', lambda event, qualifier=1: self.update_qualifiers(event, qualifier))

        # Qualifier 2
        self.qualifier_2_frame = ttk.Frame(
            self.qualifiers_options_frame,
            width=self.widget_geometries.qualifier_single_frame_width,
            height=self.widget_geometries.qualifier_single_frame_height)
        self.qualifier_2_frame.place(x=2, y=2 + 1 * self.widget_geometries.qualifier_single_frame_spacing)

        self.qualifier_2_label = ttk.Label(self.qualifier_2_frame, text='Qualifier 2:')
        self.qualifier_2_label.place(x=5, y=0)

        self.qualifier_2_entry = ttk.Entry(
            self.qualifier_2_frame,
            width=35,
            justify=CENTER,
            textvariable=self.texts.qualifier_2)
        self.qualifier_2_entry.place(x=5, y=20)
        self.qualifier_2_entry.bind('<Return>', lambda event, qualifier=2: self.update_qualifiers(event, qualifier))
        self.qualifier_2_entry.bind('<FocusOut>', lambda event, qualifier=2: self.update_qualifiers(event, qualifier))

        # Qualifier 3
        self.qualifier_3_frame = ttk.Frame(
            self.qualifiers_options_frame,
            width=self.widget_geometries.qualifier_single_frame_width,
            height=self.widget_geometries.qualifier_single_frame_height)
        self.qualifier_3_frame.place(x=2, y=2 + 2 * self.widget_geometries.qualifier_single_frame_spacing)

        self.qualifier_3_label = ttk.Label(self.qualifier_3_frame, text='Qualifier 3:')
        self.qualifier_3_label.place(x=5, y=0)

        self.qualifier_3_entry = ttk.Entry(
            self.qualifier_3_frame,
            width=35,
            justify=CENTER,
            textvariable=self.texts.qualifier_3)
        self.qualifier_3_entry.place(x=5, y=20)
        self.qualifier_3_entry.bind('<Return>', lambda event, qualifier=3: self.update_qualifiers(event, qualifier))
        self.qualifier_3_entry.bind('<FocusOut>', lambda event, qualifier=3: self.update_qualifiers(event, qualifier))

        # Qualifier 4
        self.qualifier_4_frame = ttk.Frame(
            self.qualifiers_options_frame,
            width=self.widget_geometries.qualifier_single_frame_width,
            height=self.widget_geometries.qualifier_single_frame_height)
        self.qualifier_4_frame.place(x=2, y=2 + 3 * self.widget_geometries.qualifier_single_frame_spacing)

        self.qualifier_4_label = ttk.Label(self.qualifier_4_frame, text='Qualifier 4:')
        self.qualifier_4_label.place(x=5, y=0)

        self.qualifier_4_entry = ttk.Entry(
            self.qualifier_4_frame,
            width=35,
            justify=CENTER,
            textvariable=self.texts.qualifier_4)
        self.qualifier_4_entry.place(x=5, y=20)
        self.qualifier_4_entry.bind('<Return>', lambda event, qualifier=4: self.update_qualifiers(event, qualifier))
        self.qualifier_4_entry.bind('<FocusOut>', lambda event, qualifier=4: self.update_qualifiers(event, qualifier))

        # Preview
        self.qualifier_preview_frame = ttk.Frame(
            self.qualifiers_options_frame,
            width=self.widget_geometries.qualifier_single_frame_width,
            height=50)
        self.qualifier_preview_frame.place(x=2, y=2 + 4 * self.widget_geometries.qualifier_single_frame_spacing)

        self.qualifier_preview_label = ttk.Label(self.qualifier_preview_frame, text='Preview:')
        self.qualifier_preview_label.place(x=5, y=0)

        self.qualifier_1_preview = ttk.Button(
            self.qualifier_preview_frame,
            width=5,
            textvariable=self.texts.qualifier_1_button_text)
        self.qualifier_1_preview.place(x=5, y=21)

        self.qualifier_2_preview = ttk.Button(
            self.qualifier_preview_frame,
            width=5,
            textvariable=self.texts.qualifier_2_button_text)
        self.qualifier_2_preview.place(x=47, y=21)

        self.qualifier_3_preview = ttk.Button(
            self.qualifier_preview_frame,
            width=5,
            textvariable=self.texts.qualifier_3_button_text)
        self.qualifier_3_preview.place(x=89, y=21)

        self.qualifier_4_preview = ttk.Button(
            self.qualifier_preview_frame,
            width=5,
            textvariable=self.texts.qualifier_4_button_text)
        self.qualifier_4_preview.place(x=131, y=21)

        # Change marker size
        self.markers_option_frame = ttk.LabelFrame(
            self.options_tab,
            width=self.widget_geometries.markers_options_frame_width,
            height=self.widget_geometries.markers_options_frame_height,
            text='Change marker size')
        self.markers_option_frame.place(x=5, y=270)

        self.marker_size_label = ttk.Label(
            self.markers_option_frame,
            text='Size of marker:')
        self.marker_size_label.place(x=5, y=2)

        self.marker_size_value_label = Label(
            self.markers_option_frame,
            width=3,
            bg='white',
            textvariable=self.texts.marker_size)
        self.marker_size_value_label.place(x=88, y=2)

        self.decrease_marker_size_button = ttk.Button(
            self.markers_option_frame,
            width=3,
            text='-')
        self.decrease_marker_size_button.place(x=118, y=0)
        self.decrease_marker_size_button.bind('<Button-1>', self.decrease_marker_size)
        self.decrease_marker_size_button.bind('<Control-j>', self.decrease_marker_size)

        self.increase_marker_size_button = ttk.Button(
            self.markers_option_frame,
            width=3,
            text='+')
        self.increase_marker_size_button.place(x=148, y=0)
        self.increase_marker_size_button.bind('<Button-1>', self.increase_marker_size)
        self.increase_marker_size_button.bind('<Control-k>', self.increase_marker_size)

    def update_qualifiers(self, event, qualifier):
        '''
        Updates the text of the qualifier passed through the given Entry.

        Args:
            qualifier: int - qualifier of the marker activated.
                integer in range 1-4

        Return:
            No return in the method.
        '''

        temp = {
            1: self.texts.qualifier_1.get(),
            2: self.texts.qualifier_2.get(),
            3: self.texts.qualifier_3.get(),
            4: self.texts.qualifier_4.get()
        }

        self.samples.update_qualifiers(temp, qualifier)

        if qualifier == 1:
            self.texts.qualifier_1.set(self.samples.qualifiers[1])
            self.texts.qualifier_1_button_text.set(self.samples.qualifiers_button_texts[1])
        elif qualifier == 2:
            self.texts.qualifier_2.set(self.samples.qualifiers[2])
            self.texts.qualifier_2_button_text.set(self.samples.qualifiers_button_texts[2])
        elif qualifier == 3:
            self.texts.qualifier_3.set(self.samples.qualifiers[3])
            self.texts.qualifier_3_button_text.set(self.samples.qualifiers_button_texts[3])
        elif qualifier == 4:
            self.texts.qualifier_4.set(self.samples.qualifiers[4])
            self.texts.qualifier_4_button_text.set(self.samples.qualifiers_button_texts[4])

    def decrease_marker_size(self, event):
        '''
        Decreases the marker size, the 4 is the lowest size possible.
        '''

        if self.widget_geometries.marker_size > self.widget_geometries.min_marker_size:
            self.widget_geometries.marker_size -= 1
            self.texts.marker_size.set(self.widget_geometries.marker_size)
            self.main_gui.redraw_all_markers()

        if self.widget_geometries.marker_size == self.widget_geometries.min_marker_size:
            self.decrease_marker_size_button.state(['disabled'])

        if self.widget_geometries.marker_size < self.widget_geometries.max_marker_size:
            self.increase_marker_size_button.state(['!disabled'])


    def increase_marker_size(self, event):
        '''
        Increases the marker size, the 20 is the biggest size possible.
        '''

        if self.widget_geometries.marker_size < self.widget_geometries.max_marker_size:
            self.widget_geometries.marker_size += 1
            self.texts.marker_size.set(self.widget_geometries.marker_size)
            self.main_gui.redraw_all_markers()

        if self.widget_geometries.marker_size == self.widget_geometries.max_marker_size:
            self.increase_marker_size_button.state(['disabled'])

        if self.widget_geometries.marker_size > self.widget_geometries.min_marker_size:
            self.decrease_marker_size_button.state(['!disabled'])
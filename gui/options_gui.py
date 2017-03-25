#!/usr/bin/env python3


from tkinter import *
from tkinter import ttk


class Options_gui:

    def __init__(self, options_tab, widget_geometries, samples, **kwargs):
        self.options_tab = options_tab
        self.widget_geometries = widget_geometries
        self.samples = samples
        self.qualifier_1 = kwargs['qualifier_1']
        self.qualifier_2 = kwargs['qualifier_2']
        self.qualifier_3 = kwargs['qualifier_3']
        self.qualifier_4 = kwargs['qualifier_4']
        self.qualifier_1_button_text = kwargs['qualifier_1_button_text']
        self.qualifier_2_button_text = kwargs['qualifier_2_button_text']
        self.qualifier_3_button_text = kwargs['qualifier_3_button_text']
        self.qualifier_4_button_text = kwargs['qualifier_4_button_text']

        self.widget_geometries.qualifiers_options_frame_width = 245 - 10
        self.widget_geometries.qualifiers_options_frame_height = 265
        self.widget_geometries.qualifier_single_frame_width = self.widget_geometries.qualifiers_options_frame_width - 8
        self.widget_geometries.qualifier_single_frame_height = 47
        self.widget_geometries.qualifier_single_frame_spacing = 48

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

        self.qualifier_1_entry = ttk.Entry(self.qualifier_1_frame, width=35, justify=CENTER, textvariable=self.qualifier_1)
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

        self.qualifier_2_entry = ttk.Entry(self.qualifier_2_frame, width=35, justify=CENTER, textvariable=self.qualifier_2)
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

        self.qualifier_3_entry = ttk.Entry(self.qualifier_3_frame, width=35, justify=CENTER, textvariable=self.qualifier_3)
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

        self.qualifier_4_entry = ttk.Entry(self.qualifier_4_frame, width=35, justify=CENTER, textvariable=self.qualifier_4)
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

        self.qualifier_1_preview = ttk.Button(self.qualifier_preview_frame, width=5, textvariable=self.qualifier_1_button_text)
        self.qualifier_1_preview.place(x=5, y=21)

        self.qualifier_2_preview = ttk.Button(self.qualifier_preview_frame, width=5, textvariable=self.qualifier_2_button_text)
        self.qualifier_2_preview.place(x=47, y=21)

        self.qualifier_3_preview = ttk.Button(self.qualifier_preview_frame, width=5, textvariable=self.qualifier_3_button_text)
        self.qualifier_3_preview.place(x=89, y=21)

        self.qualifier_4_preview = ttk.Button(self.qualifier_preview_frame, width=5, textvariable=self.qualifier_4_button_text)
        self.qualifier_4_preview.place(x=131, y=21)

    def update_qualifiers(self, event, qualifier):
        temp = {
            1: self.qualifier_1.get(),
            2: self.qualifier_2.get(),
            3: self.qualifier_3.get(),
            4: self.qualifier_4.get()
        }

        self.samples.update_qualifiers(temp, qualifier)

        if qualifier == 1:
            self.qualifier_1.set(self.samples.qualifiers[1])
            self.qualifier_1_button_text.set(self.samples.qualifiers_button_texts[1])
        elif qualifier == 2:
            self.qualifier_2.set(self.samples.qualifiers[2])
            self.qualifier_2_button_text.set(self.samples.qualifiers_button_texts[2])
        elif qualifier == 3:
            self.qualifier_3.set(self.samples.qualifiers[3])
            self.qualifier_3_button_text.set(self.samples.qualifiers_button_texts[3])
        elif qualifier == 4:
            self.qualifier_4.set(self.samples.qualifiers[4])
            self.qualifier_4_button_text.set(self.samples.qualifiers_button_texts[4])
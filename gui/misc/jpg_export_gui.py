#!/usr/bin/env python3


from tkinter import *
from tkinter import ttk


class Jpg_export:

    def __init__(self, widget_geometries, samples, texts):
        self.widget_geometries = widget_geometries[0]
        self.samples = samples[0]
        self.texts = texts[0]

        self.slider_value = IntVar()

        self.top_jpg_export_window = Toplevel()
        self.top_jpg_export_window.focus()
        self.top_jpg_export_window.title('Export jpg')

        window_geometry = '{}x{}+{}+{}'.format(
            self.widget_geometries.jpg_export_window_width,
            self.widget_geometries.jpg_export_window_height,
            self.widget_geometries.jpg_export_window_x,
            self.widget_geometries.jpg_export_window_y)

        self.top_jpg_export_window.geometry(window_geometry)
        self.top_jpg_export_window.resizable(width=0, height=0)

        self.top_jpg_export_main_frame = ttk.Frame(
            self.top_jpg_export_window,
            width=self.widget_geometries.jpg_export_window_width,
            height=self.widget_geometries.jpg_export_window_height)
        self.top_jpg_export_main_frame.place(x=0, y=0)

        self.jpg_quality_label = ttk.Label(
            self.top_jpg_export_main_frame,
            text='Choose a quality of the JPEG file:')
        self.jpg_quality_label.place(x=15, y=10)

        self.quality_min_label = ttk.Label(
            self.top_jpg_export_main_frame,
            text='10')
        self.quality_min_label.place(x=14, y=65)

        self.quality_max_label = ttk.Label(
            self.top_jpg_export_main_frame,
            text='100')
        self.quality_max_label.place(x=197, y=65)

        self.current_quality =Label(
            self.top_jpg_export_main_frame,
            width=3,
            bg='white',
            textvariable=self.texts.jpg_quality_text)
        self.current_quality.place(x=221, y=37)

        self.jpg_quality_slider = ttk.Scale(
            self.top_jpg_export_main_frame,
            length=200,
            from_=10,
            to=100,
            value=self.samples.jpg_quality,
            #variable=self.slider_value,
            command=self.update_jpg_quality)
        self.jpg_quality_slider.place(x=15, y=35)

        self.confirm_quality_button = ttk.Button(
            self.top_jpg_export_main_frame,
            text='OK')
        self.confirm_quality_button.place(x=85, y=87)

    def update_jpg_quality(self, value):
        self.samples.jpg_quality = int(float(value))
        self.texts.jpg_quality_text.set(int(float(value)))

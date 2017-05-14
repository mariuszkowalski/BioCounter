#!/usr/bin/env python3


from tkinter import *
from tkinter import ttk


class Jpg_export(Toplevel):

    def __init__(self, main_widget, widget_geometries, samples, texts):
        Toplevel.__init__(self, main_widget)
        self.widget_geometries = widget_geometries[0]
        self.samples = samples[0]
        self.texts = texts[0]

        self.transient(main_widget)

        self.main_widget = main_widget
        self.previous_quality = self.samples.jpg_quality

        self.title('Export jpg')

        window_geometry = '{}x{}+{}+{}'.format(
            self.widget_geometries.jpg_export_window_width,
            self.widget_geometries.jpg_export_window_height,
            self.widget_geometries.jpg_export_window_x,
            self.widget_geometries.jpg_export_window_y)

        self.geometry(window_geometry)
        self.resizable(width=0, height=0)

        self.top_jpg_export_main_frame = ttk.Frame(
            self,
            width=self.widget_geometries.jpg_export_window_width,
            height=self.widget_geometries.jpg_export_window_height)
        self.top_jpg_export_main_frame.place(x=0, y=0)
        self.initial_focus = self.top_jpg_export_main_frame

        self.build_window_elements()
        self.button_box()
        self.grab_set()

        if not self.initial_focus:
            self.initial_focus = self

        self.protocol('WM_DELETE_WINDOW', self.pressed_cancel)

        self.initial_focus.focus_set()
        self.wait_window(self)

    def build_window_elements(self):

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
            command=self.update_jpg_quality)
        self.jpg_quality_slider.place(x=15, y=35)

    def button_box(self):

        self.confirm_quality_button = ttk.Button(
            self.top_jpg_export_main_frame,
            text='OK',
            default=ACTIVE)
        self.confirm_quality_button.place(x=50, y=87)
        self.confirm_quality_button.bind('<Button-1>', self.pressed_ok)
        self.bind('<Return>', self.pressed_ok)

        self.cancel_quality_button = ttk.Button(
            self.top_jpg_export_main_frame,
            text='Cancel')
        self.cancel_quality_button.place(x=130, y=87)
        self.cancel_quality_button.bind('<Button-1>', self.pressed_cancel_handler)
        self.bind('<Escape>', self.pressed_cancel_handler)

    def update_jpg_quality(self, value):
        self.samples.jpg_quality = int(float(value))
        self.texts.jpg_quality_text.set(int(float(value)))

    def pressed_ok(self, event):
        self.withdraw()
        self.update_idletasks()
        self.destroy()

    def pressed_cancel_handler(self, event):
        self.pressed_cancel()

    def pressed_cancel(self):
        self.samples.jpg_quality = self.previous_quality
        self.texts.jpg_quality_text.set(self.previous_quality)
        self.main_widget.focus_set()
        self.destroy()

#!/usr/bin/env python3


from tkinter import *
from tkinter import ttk


class About_gui:

    def __init__(self, widget_geometries):
        '''
        Creates top level window containing information about BioCounter software.

        Args:
            widget_geometries: instance - class Widget_geometries.
        '''
        self.widget_geometries = widget_geometries[0]

        self.top_about_window = Toplevel()
        self.top_about_window.focus()
        self.top_about_window.title('About BioCounter')

        window_geometry = '{}x{}+{}+{}'.format(
            self.widget_geometries.about_window_width,
            self.widget_geometries.about_window_height,
            self.widget_geometries.about_window_x,
            self.widget_geometries.about_window_y)

        self.top_about_window.geometry(window_geometry)
        self.top_about_window.resizable(width=0, height=0)
        #self.top_about_window.wm_attributes('-topmost', 1)

        self.about_window_main_frame = ttk.Frame(
            self.top_about_window,
            width=self.widget_geometries.about_window_width,
            height=self.widget_geometries.about_window_height)
        self.about_window_main_frame.place(x=0, y=0)
        self.about_window_main_frame.bind('<Button-1>', self.close_window)

        self.info_label_1 = ttk.Label(
            self.about_window_main_frame,
            font=('Helvetica', 20),
            text='BioCounter v.0.1')
        self.info_label_1.place(x=20, y=20)

        self.info_label_2 = ttk.Label(
            self.about_window_main_frame,
            font=('Helvetica', 12),
            text='Load. Count. Export.')
        self.info_label_2.place(x=20, y=50)

        self.info_label_3 = ttk.Label(
            self.about_window_main_frame,
            font=('Helvetica', 10),
            text='Author: Mariusz Kowalski')
        self.info_label_3.place(x=20, y=90)

        self.info_label_4 = ttk.Label(
            self.about_window_main_frame,
            font=('Helvetica', 10),
            text='Created with Python 3.4')
        self.info_label_4.place(x=20, y=105)

    def close_window(self, event):
        self.top_about_window.destroy()
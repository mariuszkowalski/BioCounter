#!/usr/bin/env python3


from tkinter import *
from tkinter import ttk


class About_gui(Toplevel):

    def __init__(self, main_widget, widget_geometries):
        Toplevel.__init__(self, main_widget)
        '''
        Creates top level window containing information about BioCounter software.

        Args:
            widget_geometries: instance - class Widget_geometries.
        '''
        self.widget_geometries = widget_geometries[0]

        self.transient(main_widget)
        self.main_widget = main_widget

        self.title('About BioCounter')

        window_geometry = '{}x{}+{}+{}'.format(
            self.widget_geometries.about_window_width,
            self.widget_geometries.about_window_height,
            self.widget_geometries.about_window_x,
            self.widget_geometries.about_window_y)

        self.geometry(window_geometry)
        self.resizable(width=0, height=0)
        #self.wm_attributes('-topmost', 1)

        self.about_window_main_frame = ttk.Frame(
            self,
            width=self.widget_geometries.about_window_width,
            height=self.widget_geometries.about_window_height)
        self.about_window_main_frame.place(x=0, y=0)
        self.about_window_main_frame.bind('<Button-1>', self.pressed_cancel)
        self.initial_focus = self.about_window_main_frame

        self.build_window_elements()

        self.grab_set()

        if not self.initial_focus:
            self.initial_focus = self

        self.protocol('WM_DELETE_WINDOW', self.pressed_cancel)

        self.initial_focus.focus_set()
        self.wait_window(self)


    def build_window_elements(self):

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

    def pressed_cancel(self, event):
        self.destroy()
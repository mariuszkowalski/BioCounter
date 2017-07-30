#!/usr/bin/env python3


from tkinter import Toplevel, ACTIVE
from tkinter import ttk


class Tif_export(Toplevel):
    '''
    Class creates modal window to save tif file
    about the software.
    '''

    def __init__(self, main_widget, widget_geometries, samples, texts):
        '''
        Creates top level window used for saveing tif file.

        Args:
            main_widget: instance - class Tk
            widget_geometries: instance - class Widget_geometries.
            samples: instance - class Samples
            texts: instance - class Texts
        '''

        Toplevel.__init__(self, main_widget)

        self.widget_geometries = widget_geometries[0]
        self.samples = samples[0]
        self.texts = texts[0]

        self.transient(main_widget)

        self.main_widget = main_widget
        self.previous_compression = self.samples.tif_compression

        self.title('Export tif')

        window_geometry = '{}x{}+{}+{}'.format(
            self.widget_geometries.tif_export_window_width,
            self.widget_geometries.tif_export_window_height,
            self.widget_geometries.tif_export_window_x,
            self.widget_geometries.tif_export_window_y)

        self.geometry(window_geometry)
        self.resizable(width=0, height=0)

        self.top_tif_export_main_frame = ttk.Frame(
            self,
            width=self.widget_geometries.tif_export_window_width,
            height=self.widget_geometries.tif_export_window_height)
        self.top_tif_export_main_frame.place(x=0, y=0)

        self.build_window_elements()
        self.button_box()
        self.grab_set()

        self.protocol('WM_DELETE_WINDOW', self.pressed_cancel)

        self.top_tif_export_main_frame.focus_set()
        self.wait_window(self)

    def build_window_elements(self):
        '''
        Create additional elements used in
        modal window.
        '''

        self.tif_quality_label = ttk.Label(
            self.top_tif_export_main_frame,
            text='Choose a compression of the TIFF file:')
        self.tif_quality_label.place(x=15, y=10)

        self.tif_compression_none = ttk.Radiobutton(
            self.top_tif_export_main_frame,
            text='No compression',
            variable=self.texts.tif_compression_text,
            value='None')
        self.tif_compression_none.place(x=15, y=35)

        self.tif_compression_tiff_deflate = ttk.Radiobutton(
            self.top_tif_export_main_frame,
            text='Tiff deflate',
            variable=self.texts.tif_compression_text,
            value='tiff_deflate')
        self.tif_compression_tiff_deflate.place(x=15, y=60)

        self.tif_compression_tiff_adobe_deflate = ttk.Radiobutton(
            self.top_tif_export_main_frame,
            text='Tiff adobe deflate',
            variable=self.texts.tif_compression_text,
            value='tiff_adobe_deflate')
        self.tif_compression_tiff_adobe_deflate.place(x=15, y=85)

    def button_box(self):
        '''
        Creates button box for the modal window.
        '''

        self.confirm_quality_button = ttk.Button(
            self.top_tif_export_main_frame,
            text='OK',
            default=ACTIVE)
        self.confirm_quality_button.place(x=50, y=117)
        self.confirm_quality_button.bind('<Button-1>', self.pressed_ok)
        self.bind('<Return>', self.pressed_ok)

        self.cancel_quality_button = ttk.Button(
            self.top_tif_export_main_frame,
            text='Cancel')
        self.cancel_quality_button.place(x=130, y=117)
        self.cancel_quality_button.bind('<Button-1>', self.pressed_cancel_handler)
        self.bind('<Escape>', self.pressed_cancel_handler)

    def pressed_ok(self, event):
        '''
        Handles the events after confirmation of
        save parameters.
        '''

        self.samples.export_status = True
        self.samples.tif_compression = self.texts.tif_compression_text.get()
        self.withdraw()
        self.update_idletasks()
        self.destroy()

    def pressed_cancel_handler(self, event):
        '''
        Event handle for pressed cancel method.
        '''

        self.pressed_cancel()

    def pressed_cancel(self):
        '''
        Method used to destroy modal window.
        '''

        self.samples.export_status = False
        self.samples.tif_quality = self.previous_compression
        self.main_widget.focus_set()
        self.destroy()

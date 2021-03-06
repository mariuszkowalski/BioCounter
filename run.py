#!/usr/bin/env python3
'''
Main module of the BioCounter software.
Requires pillow package to run.

author: Mariusz Kowalski
'''

import os
import platform
import sys
from tkinter import Tk, Menu, W, SUNKEN
from tkinter import messagebox
from tkinter import ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename

from PIL import Image

from analysis.statistics import Statistics
from gui.export_canvas_utilities import ExportCanvasUtilities
from gui.main_gui import Main_gui
from gui.markers_gui import Markers_gui
from gui.options_gui import Options_gui
from gui.statistics_gui import Statistics_gui
from gui.statuses import Statuses
from gui.texts import Texts
from gui.widgets_geometries import Widget_geometries

from gui.misc.about_gui import About_gui
from gui.misc.jpg_export_gui import Jpg_export
from gui.misc.png_export_gui import Png_export
from gui.misc.tif_export_gui import Tif_export

from samples import Samples
from settings.manage_settings import ManageSettings
from settings.settings_utilities import SettingsUtilities


__author__ = 'Mariusz Kowalski'

if getattr(sys, 'frozen', False):
    SETTINGS_PATH = os.path.join(os.path.dirname(sys.executable), 'settings').replace('\\', '/')
else:
    SETTINGS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'settings').replace('\\', '/')

DEBUG = 1


class Window:
    '''
    Main class of the software.
    Creates Window interface using Tkinter module.
    '''

    def __init__(self, mainWidget, settings):
        '''
        Main Window of the program.
        Contains all necessary elements to navigate and use all functionalities.

        Args:
            settings: instance - instance of ManageSettings class.
            mainWidget: instance - instance of the Tk() class.
        '''

        self.settings = settings
        self.mainWidget = mainWidget

        self.statistics = [Statistics()]
        self.samples = [Samples()]
        self.widget_geometries = [Widget_geometries(self.settings)]
        self.texts = [Texts(self.samples, self.statistics, self.widget_geometries)]
        self.statuses = [Statuses(self.texts, self.widget_geometries)]

        #Menus
        self.drop_down_menu = Menu(self.mainWidget)
        self.mainWidget.config(menu=self.drop_down_menu)

        #File menu.
        self.file_menu = Menu(self.drop_down_menu, tearoff=0)
        self.drop_down_menu.add_cascade(label='File', menu=self.file_menu)

        self.file_menu.add_command(label='Open file', command=self.open_photo, accelerator='Ctrl+O')
        self.file_menu.add_command(label='Save as', command=self.save_photo, accelerator='Ctrl+S')
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Exit', command=self.mainWidget.quit)

        #Window menu.
        self.window_options_menu = Menu(self.drop_down_menu, tearoff=0)
        self.drop_down_menu.add_cascade(label='Window', menu=self.window_options_menu)

        self.resolution_menu = Menu(self.window_options_menu, tearoff=0)

        self.window_options_menu.add_checkbutton(
            label='Always on top',
            onvalue=True,
            offvalue=False,
            command=self.change_top_mode,
            accelerator='Ctrl+T')
        self.window_options_menu.add_separator()

        self.window_options_menu.add_cascade(label='Change resolution', menu=self.resolution_menu)
        self.resolution_menu.add_command(label='1200x900', command=lambda: self.change_resolution([1200, 900]))
        self.resolution_menu.add_command(label='1600x1200', command=lambda: self.change_resolution([1600, 1200]))
        self.resolution_menu.add_command(label='1280x720', command=lambda: self.change_resolution([1280, 720]))
        self.resolution_menu.add_command(label='1366x768', command=lambda: self.change_resolution([1366, 768]))
        self.resolution_menu.add_command(label='1600x900', command=lambda: self.change_resolution([1600, 900]))
        self.resolution_menu.add_command(label='1920x1080', command=lambda: self.change_resolution([1920, 1080]))

        #About menu.
        self.about_menu = Menu(self.drop_down_menu, tearoff=0)
        self.drop_down_menu.add_cascade(label='About', menu=self.about_menu)

        self.about_menu.add_command(label='Info', command=self.show_about_window)

        #Debug menu.
        if DEBUG:
            self.debug_menu = Menu(self.drop_down_menu, tearoff=0)
            self.drop_down_menu.add_cascade(label='Debug', menu=self.debug_menu)

            self.debug_menu.add_command(label='Debug samples', command=self.debug_samples)
            self.debug_menu.add_command(label='Debug markers', command=self.debug_markers)
            self.debug_menu.add_command(label='Debug analysis', command=self.debug_statistics)

        #Main frame.
        self.main_frame = ttk.Frame(self.mainWidget,
                                    width=self.settings.adjusted_screen_width,
                                    height=self.settings.adjusted_screen_height-20,
                                    padding=(0, 0, 0, 0))
        self.main_frame.place(x=0, y=0)
        self.main_frame.bind_all('<Control-o>', self.open_photo_event_handler)
        self.main_frame.bind_all('<Control-t>', self.change_top_mode_event_handler)
        self.main_frame.bind_all('<Control-s>', self.save_photo_event_handler)

        self.status_bar = ttk.Label(self.mainWidget,
                                    width=self.settings.adjusted_screen_width,
                                    anchor=W,
                                    border=0,
                                    relief=SUNKEN,
                                    textvariable=self.texts[0].status_bar_text)
        self.status_bar.place(x=0, y=self.settings.adjusted_screen_height-19)

        self.mainWidget.update_idletasks()

        self.picture_frame = ttk.Frame(self.main_frame,
                                       width=self.widget_geometries[0].picture_frame_width,
                                       height=self.widget_geometries[0].picture_frame_height)
        self.picture_frame.place(x=0, y=0)

        self.toolbar_frame = ttk.Frame(self.main_frame,
                                       width=self.widget_geometries[0].toolbar_width,
                                       height=self.widget_geometries[0].picture_frame_height)
        self.toolbar_frame.place(x=self.widget_geometries[0].picture_frame_width, y=0)

        self.notebook = ttk.Notebook(self.toolbar_frame)
        self.notebook.place(x=0, y=0)

        self.markers_tab = ttk.Frame(self.notebook,
                                     width=self.widget_geometries[0].notebook_width,
                                     height=self.widget_geometries[0].notebook_height,
                                     takefocus=True)
        self.statistics_tab = ttk.Frame(self.notebook,
                                        width=self.widget_geometries[0].notebook_width,
                                        height=self.widget_geometries[0].notebook_height,
                                        takefocus=True)
        self.options_tab = ttk.Frame(self.notebook,
                                     width=self.widget_geometries[0].notebook_width,
                                     height=self.widget_geometries[0].notebook_height,
                                     takefocus=True)

        self.notebook.add(self.markers_tab, text='Markers')
        self.notebook.add(self.statistics_tab, text='Statistics')
        self.notebook.add(self.options_tab, text='Options')

        #
        #Initialization of main gui.
        #
        self.main_gui = [Main_gui(
            self.picture_frame,
            self.widget_geometries,
            self.samples,
            self.statistics,
            self.texts,
            self.statuses)]

        #
        #Initialization of additional gui parts.
        #
        self.markers_gui = Markers_gui(
            self.main_gui[0],
            self.markers_tab,
            self.widget_geometries,
            self.samples,
            self.statistics,
            self.texts,
            self.statuses
            )

        self.statistics_gui = Statistics_gui(
            self.main_gui[0],
            self.statistics_tab,
            self.widget_geometries,
            self.samples,
            self.statistics,
            self.texts,
            self.statuses
            )

        self.options_gui = Options_gui(
            self.main_gui[0],
            self.options_tab,
            self.widget_geometries,
            self.samples,
            self.texts,
            self.statuses
            )

    def open_photo_event_handler(self, event):
        '''
        Handler for open photo event to allow use of
        keyboard shortcuts.
        '''

        self.open_photo()

    def open_photo(self):
        '''
        Method for openning the photo.
        '''

        allowed_file_types = ['.jpg', '.png', '.tif', '.JPG', '.PNG', '.TIF']
        self.file_name = askopenfilename(filetypes=(('Graphic files', '*.jpg *.png *tif'), ('All files', '*.*')))

        try:
            if len(self.file_name) == 0:
                raise OSError
            elif len(self.file_name) > 0 and self.file_name[-4:] not in allowed_file_types:
                raise AttributeError
            else:
                self.image_object = Image.open(self.file_name)
                self.samples[0].file_format_in_use = self.file_name[-4:]

        except AttributeError:
            messagebox.showinfo(message='Not supported file type')

        except OSError:
            messagebox.showinfo(message='File not selected')

        else:
            # Clear analysis.
            self.statistics[0].clear_all()
            self.texts[0].update_statistic_texts()
            # Clear markers.
            self.samples[0].placed_markers = []
            # Place loaded image on the canvas.
            self.main_gui[0].place_image_on_canvas(self.image_object)

    def save_photo_event_handler(self, event):
        '''
        Handler for close photo event to allow use of
        keyboard shortcuts.
        '''

        self.save_photo()

    def save_photo(self):
        '''
        Method for saveing the photo.
        '''

        extension = None
        name_exists = False

        if self.check_if_image_object_exists():

            allowed_file_types = [
                self.samples[0].file_format_in_use.lower(),
                self.samples[0].file_format_in_use.upper()]
            allowed_file_types_text = ' '.join(allowed_file_types)
            extension = self.samples[0].file_format_in_use.lower()

            raw_file_name_to_save = asksaveasfilename(
                filetypes=(
                    ('Graphic files', allowed_file_types_text), ('All files', '*.*')))

            if len(raw_file_name_to_save) > 0:
                name_exists = True
            else:
                name_exists = False

            self.file_name_to_save = ExportCanvasUtilities.format_export_file_name(raw_file_name_to_save, extension)

        try:
            if name_exists and len(self.file_name_to_save) > 0 and self.check_if_image_object_exists():
                self.samples[0].export_status = False
            else:
                raise OSError

        except AttributeError:
            pass

        except OSError:
            messagebox.showinfo(message='Invalid file name')

        else:
            image_to_save = self.main_gui[0].raw_image_object

            image_ready_to_save = ExportCanvasUtilities.place_elements(
                image_to_save=image_to_save,
                placed_markers=self.samples[0].placed_markers,
                colors=self.samples[0].colors)

            if extension[1:] == 'jpg':
                self.jpg_export = Jpg_export(
                    self.mainWidget,
                    self.widget_geometries,
                    self.samples,
                    self.texts)

                if self.samples[0].export_status:
                    # Compression less than 95 is not recommended.
                    image_ready_to_save.save(
                        self.file_name_to_save,
                        'JPEG',
                        quality=self.samples[0].jpg_quality)
                else:
                    messagebox.showinfo(message='Canceled')

            elif extension[1:] == 'png':
                self.png_export = Png_export(
                    self.mainWidget,
                    self.widget_geometries,
                    self.samples,
                    self.texts)

                if self.samples[0].export_status:
                    # 0 - no compression, 1 - best speed, 9 - best compression.
                    image_ready_to_save.save(
                        self.file_name_to_save,
                        'PNG',
                        compress_level=self.samples[0].png_quality)
                else:
                    messagebox.showinfo(message='Canceled')

            elif extension[1:] == 'tif':
                self.tif_export = Tif_export(
                    self.mainWidget,
                    self.widget_geometries,
                    self.samples,
                    self.texts)

                if self.samples[0].export_status:
                    # Compressions available in pillow - None, tiff_deflate, tiff_adobe_deflate.
                    image_ready_to_save.save(
                        self.file_name_to_save,
                        'TIFF',
                        compression=self.samples[0].tif_compression)
                else:
                    messagebox.showinfo(message='Canceled')


    def check_if_image_object_exists(self):
        '''
        Method checks if the image exists, to prevent
        a save errors.
        '''

        #Attribute self.image_object has to exist first
        try:
            if self.image_object:
                pass

        except AttributeError:
            messagebox.showinfo(message='No file to save')

        else:
            return True

        return False

    def change_top_mode_event_handler(self, event):
        '''
        Handler for always on top mode event to allow use of
        keyboard shortcuts.
        '''
        self.change_top_mode()

    def change_top_mode(self):
        '''
        Change the mode of always on top window option.
        '''

        if self.settings.always_on_top:
            self.mainWidget.wm_attributes('-topmost', 0)
            self.settings.always_on_top = False
        else:
            self.mainWidget.wm_attributes('-topmost', 1)
            self.settings.always_on_top = True

    def change_resolution(self, new_resolution):
        '''
        Change the window resolution.
        After the change happens the settings file is updated.

        args:
            new_resolution; list - a list containing two integers for the new window resolution x and y.
        '''

        if self.settings.set_screen_resolution != new_resolution:
            self.settings.set_screen_resolution = new_resolution
            self.settings.calculate_additional_settings()

            SettingsUtilities.save_settings_file(SETTINGS_PATH, self.settings)
            messagebox.showinfo(message='Please reload the program to apply changes.')

        else:
            messagebox.showinfo(message='This is current resolution.')

    def debug_statistics(self):
        '''
        Method for debugging the statistics.
        '''

        print('Debug analysis pressed.')

        for key, value in self.statistics[0].stats.items():
            print(key, '-->', value)

    def debug_markers(self):
        '''
        Method for debugging the markers.
        '''

        print('Debug markers pressed.')
        if len(self.samples[0].placed_markers) != 0:
            for element in self.samples[0].placed_markers:
                print('X: {}, Y: {}'.format(element.position_x, element.position_y))
        else:
            print('No placed markers')

    def debug_samples(self):
        '''
        Method for debugging the samples.
        '''

        print('---  C L I C K E D    I N    M E N U  [ O N ]  ---')

        for key, value in vars(self.samples[0]).items():
            print(key, '-->', value)

        print('---  C L I C K E D    I N    M E N U  [ O F F ]  ---')

    def show_about_window(self):
        '''
        Method displays modal window containing
        information about the software.
        '''

        self.about_gui = About_gui(
            self.mainWidget,
            self.widget_geometries)


def main():
    '''
    Main function used for software Initialization.
    '''

    raw_settings = SettingsUtilities.load_settings_file(SETTINGS_PATH)
    settings = ManageSettings(**raw_settings)

    root = Tk()

    root.geometry('{}x{}+5+5'.format(settings.adjusted_screen_width, settings.adjusted_screen_height))
    root.title('Bio Counter')


    if settings.always_on_top:
        root.wm_attributes('-topmost', 1)
    else:
        root.wm_attributes('-topmost', 0)

    if settings.window_is_resizable:
        root.resizable(width=1, height=1)
    else:
        root.resizable(width=0, height=0)

    window = Window(root, settings)
    window

    root.mainloop()


if __name__ == '__main__':
    if platform.system() == 'Windows':
        main()

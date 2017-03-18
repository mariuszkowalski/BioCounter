#!/usr/bin/env python3


from manage_settings import ManageSettings
from samples import Samples
from settings_utilities import SettingsUtilities
from screen_utilities import ScreenUtilities
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter import messagebox
import codecs
import os
import platform


__author__ = 'Mariusz Kowalski'


SETTINGS_PATH = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')


class Window:

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

        self.samples = Samples()

        self.status_bar_text = StringVar()
        self.status_bar_text.set('')

        self.sample_1_name = StringVar()
        self.sample_2_name = StringVar()
        self.sample_3_name = StringVar()
        self.sample_4_name = StringVar()
        self.sample_5_name = StringVar()
        self.sample_6_name = StringVar()
        self.sample_7_name = StringVar()
        self.sample_8_name = StringVar()

        self.sample_1_name.set(self.samples.names[1])
        self.sample_2_name.set(self.samples.names[2])
        self.sample_3_name.set(self.samples.names[3])
        self.sample_4_name.set(self.samples.names[4])
        self.sample_5_name.set(self.samples.names[5])
        self.sample_6_name.set(self.samples.names[6])
        self.sample_7_name.set(self.samples.names[7])
        self.sample_8_name.set(self.samples.names[8])

        self.qualifier_1 = StringVar()
        self.qualifier_2 = StringVar()
        self.qualifier_3 = StringVar()
        self.qualifier_4 = StringVar()

        self.qualifier_1.set(self.samples.qualifiers[1])
        self.qualifier_2.set(self.samples.qualifiers[2])
        self.qualifier_3.set(self.samples.qualifiers[3])
        self.qualifier_4.set(self.samples.qualifiers[4])

        #Menus
        self.drop_down_menu = Menu(self.mainWidget)
        self.mainWidget.config(menu=self.drop_down_menu)

        #File menu.
        self.file_menu = Menu(self.drop_down_menu, tearoff=0)
        self.drop_down_menu.add_cascade(label='File', menu=self.file_menu)

        self.file_menu.add_command(label='Open file', command=self.placeholder)
        self.file_menu.add_command(label='Save file', command=self.placeholder)
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Exit', command=self.mainWidget.quit)

        #Window menu.
        self.window_options_menu = Menu(self.drop_down_menu, tearoff=0)
        self.drop_down_menu.add_cascade(label='Window', menu=self.window_options_menu)

        self.resolution_menu = Menu(self.window_options_menu, tearoff=0)

        self.window_options_menu.add_checkbutton(label='Always on top', onvalue=True, offvalue=False, command=self.change_top_mode)
        self.window_options_menu.add_separator()

        self.window_options_menu.add_cascade(label='Change resolution', menu=self.resolution_menu)
        self.resolution_menu.add_command(label='640x480', command=lambda: self.change_resolution([640, 480]))
        self.resolution_menu.add_command(label='800x600', command=lambda: self.change_resolution([800, 600]))
        self.resolution_menu.add_command(label='1200x900', command=lambda: self.change_resolution([1200, 900]))
        self.resolution_menu.add_command(label='1600x1200', command=lambda: self.change_resolution([1600, 1200]))
        self.resolution_menu.add_command(label='1280x720', command=lambda: self.change_resolution([1280, 720]))
        self.resolution_menu.add_command(label='1366x768', command=lambda: self.change_resolution([1366, 768]))
        self.resolution_menu.add_command(label='1600x900', command=lambda: self.change_resolution([1600, 900]))
        self.resolution_menu.add_command(label='1920x1080', command=lambda: self.change_resolution([1920, 1080]))

        #About menu.
        self.about_menu = Menu(self.drop_down_menu, tearoff=0)
        self.drop_down_menu.add_cascade(label='About', menu=self.about_menu)

        self.about_menu.add_command(label='Info', command=self.placeholder)

        #Main frame.
        self.main_frame = ttk.Frame(self.mainWidget,
                                    width=self.settings.adjusted_screen_width,
                                    height=self.settings.adjusted_screen_height-20,
                                    padding=(0, 0, 0, 0))
        self.main_frame.place(x=0, y=0)

        self.status_bar = ttk.Label(self.mainWidget,
                                    width=self.settings.adjusted_screen_width,
                                    anchor=W,
                                    border=0,
                                    relief=SUNKEN,
                                    textvariable=self.status_bar_text)
        self.status_bar.place(x=0, y=self.settings.adjusted_screen_height-19)

        self.mainWidget.update_idletasks()
        self.build_main_gui()
        self.build_markers_gui()

    def build_main_gui(self):
        '''
        Building the picture frame and all it's elements and options frame.
        '''

        toolbar_width = 250
        scrollbar_thickness = 18
        picture_frame_width = self.main_frame.winfo_width() - toolbar_width
        picture_frame_height = self.main_frame.winfo_height()
        canvas_frame_width = picture_frame_width - scrollbar_thickness
        canvas_frame_height = picture_frame_height - scrollbar_thickness
        notebook_width =  toolbar_width - 5
        notebook_height = self.main_frame.winfo_height() - 44

        self.picture_frame = ttk.Frame(self.main_frame, width=picture_frame_width, height=picture_frame_height)
        self.picture_frame.place(x=0, y=0)

        self.canvas_frame = ttk.Frame(self.picture_frame, width=canvas_frame_width, height=canvas_frame_height)
        self.canvas_frame.place(x=0, y=0)

        self.scrollbar_x_frame = ttk.Frame(self.picture_frame, relief=GROOVE, width=canvas_frame_width, height=scrollbar_thickness)
        self.scrollbar_x_frame.place(x=0, y=canvas_frame_height)

        self.scrollbar_y_frame = ttk.Frame(self.picture_frame, relief=GROOVE, width=scrollbar_thickness, height=canvas_frame_height)
        self.scrollbar_y_frame.place(x=canvas_frame_width, y=0)

        self.toolbar_frame = ttk.Frame(self.main_frame, width=toolbar_width, height=picture_frame_height)
        self.toolbar_frame.place(x=picture_frame_width, y=0)

        self.canvas = Canvas(self.canvas_frame,
                             width=canvas_frame_width,
                             height=canvas_frame_height,
                             borderwidth=0,
                             highlightthickness=0)
        self.canvas.place(x=0, y=0)
        self.canvas.bind('<Button-1>', self.place_marker_on_canvas)
        self.canvas.bind('<MouseWheel>', self.use_mousewheel_on_canvas)
        self.canvas.bind('<Shift-MouseWheel>', self.use_mousewheel_and_shift_on_canvas)
        self.canvas.bind('<Control-MouseWheel>', self.use_mousewheel_and_ctrl_on_canvas)

        self.notebook = ttk.Notebook(self.toolbar_frame)
        self.notebook.place(x=0, y=0)

        self.markers_tab = ttk.Frame(self.notebook, width=notebook_width, height=notebook_height)
        self.statistics_tab = ttk.Frame(self.notebook, width=notebook_width, height=notebook_height)
        self.something_tab = ttk.Frame(self.notebook, width=notebook_width, height=notebook_height)

        self.notebook.add(self.markers_tab, text='Markers')
        self.notebook.add(self.statistics_tab, text='Statistics')
        self.notebook.add(self.something_tab, text='Something')

        self.mainWidget.update_idletasks()

    def build_markers_gui(self):
        '''
        Building the all elements of the markers menu.
        '''
        sample_frame_width = self.markers_tab.winfo_width()
        sample_frame_height = 53

        #
        # Sample 1
        #
        self.sample_1_frame = ttk.Frame(self.markers_tab, width=sample_frame_width, height=sample_frame_height)
        self.sample_1_frame.place(x=0, y=sample_frame_height * 0)

        self.sample_1_entry = ttk.Entry(self.sample_1_frame, width=38, justify=CENTER, textvariable=self.sample_1_name)
        self.sample_1_entry.place(x=5, y=5)
        self.sample_1_entry.bind('<Return>', self.update_samples_names)

        self.sample_1_marker_1_button = ttk.Button(self.sample_1_frame, width=5, textvariable=self.qualifier_1)
        self.sample_1_marker_1_button.place(x=5, y=27)

        self.sample_1_marker_2_button = ttk.Button(self.sample_1_frame, width=5, textvariable=self.qualifier_2)
        self.sample_1_marker_2_button.place(x=47, y=27)

        self.sample_1_marker_3_button = ttk.Button(self.sample_1_frame, width=5, textvariable=self.qualifier_3)
        self.sample_1_marker_3_button.place(x=89, y=27)

        self.sample_1_marker_4_button = ttk.Button(self.sample_1_frame, width=5, textvariable=self.qualifier_4)
        self.sample_1_marker_4_button.place(x=131, y=27)

        #
        # Sample 2
        #
        self.sample_2_frame = ttk.Frame(self.markers_tab, width=sample_frame_width, height=sample_frame_height)
        self.sample_2_frame.place(x=0, y=sample_frame_height * 1)

        self.sample_2_entry = ttk.Entry(self.sample_2_frame, width=38, justify=CENTER, textvariable=self.sample_2_name)
        self.sample_2_entry.place(x=5, y=5)
        self.sample_2_entry.bind('<Return>', self.update_samples_names)

        self.sample_2_marker_1_button = ttk.Button(self.sample_2_frame, width=5, textvariable=self.qualifier_1)
        self.sample_2_marker_1_button.place(x=5, y=27)

        self.sample_2_marker_2_button = ttk.Button(self.sample_2_frame, width=5, textvariable=self.qualifier_2)
        self.sample_2_marker_2_button.place(x=47, y=27)

        self.sample_2_marker_3_button = ttk.Button(self.sample_2_frame, width=5, textvariable=self.qualifier_3)
        self.sample_2_marker_3_button.place(x=89, y=27)

        self.sample_2_marker_4_button = ttk.Button(self.sample_2_frame, width=5, textvariable=self.qualifier_4)
        self.sample_2_marker_4_button.place(x=131, y=27)

    def place_marker_on_canvas(self, event):
        print('Marker placed at {},{}'.format(event.x, event.y))

    def use_mousewheel_on_canvas(self, event):
        '''
        Scroll the canvas in vertical direction.
        '''

        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), 'units')
        print('Scroll y.')

    def use_mousewheel_and_shift_on_canvas(self, event):
        '''
        Scroll the canvas in horizontal direction.
        '''

        self.canvas.xview_scroll(int(-1 * (event.delta / 120)), 'units')
        print('Scroll and shift on canvas.')

    def use_mousewheel_and_ctrl_on_canvas(self, event):
        '''
        Zoom in and out the canvas.
        '''

        print('Scroll and ctrl on canvas {}'.format(int(event.delta / 60)))

    def update_samples_names(self, event):
        self.samples.names[1] = self.sample_1_name.get()
        self.samples.names[2] = self.sample_2_name.get()
        self.samples.names[3] = self.sample_3_name.get()
        self.samples.names[4] = self.sample_4_name.get()
        self.samples.names[5] = self.sample_5_name.get()
        self.samples.names[6] = self.sample_6_name.get()
        self.samples.names[7] = self.sample_7_name.get()
        self.samples.names[8] = self.sample_8_name.get()
        print(self.samples.names)

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
            new_resolution; list - a list containing two integers for the new window resolution x and y
        '''
        if self.settings.set_screen_resolution != new_resolution:
            self.settings.set_screen_resolution = new_resolution
            self.settings.calculate_additional_settings()

            SettingsUtilities.save_settings_file(SETTINGS_PATH, self.settings)
            messagebox.showinfo(message='Please reload the program to apply changes.')

        else:
            messagebox.showinfo(message='This is current resolution.')

    def remove_elements(self, elements):
        for element in elements:
            element.destroy()

    def placeholder(self):
        print('This is a simple placeholder message.')


def main():
    raw_settings = SettingsUtilities.load_settings_file(SETTINGS_PATH)
    settings = ManageSettings(**raw_settings)

    root = Tk()

    root.geometry('{}x{}+5+5'.format(settings.adjusted_screen_width, settings.adjusted_screen_height))
    root.title('Bio Counter')


    if settings.always_on_top == True:
        root.wm_attributes('-topmost', 1)
    else:
        root.wm_attributes('-topmost', 0)

    if settings.window_is_resizable == True:
        root.resizable(width=1, height=1)
    else:
        root.resizable(width=0, height=0)

    window = Window(root, settings)
    window

    root.mainloop()


if __name__ == '__main__':
    if platform.system() == 'Windows':
        main()
    else:
        print('Platform not supported.')

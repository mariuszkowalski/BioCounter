#!/usr/bin/env python3


from manage_settings import ManageSettings
from samples import Samples
from settings_utilities import SettingsUtilities
from screen_utilities import ScreenUtilities
from tkinter import *
from tkinter import ttk
from tkinter.colorchooser import askcolor
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
        self.build_options_gui()

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
        self.options_tab = ttk.Frame(self.notebook, width=notebook_width, height=notebook_height)

        self.notebook.add(self.markers_tab, text='Markers')
        self.notebook.add(self.statistics_tab, text='Statistics')
        self.notebook.add(self.options_tab, text='Options')

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
        self.sample_1_entry.bind('<FocusOut>', self.update_samples_names)

        self.sample_1_marker_1_button = ttk.Button(self.sample_1_frame, width=5, textvariable=self.qualifier_1)
        self.sample_1_marker_1_button.place(x=5, y=27)
        self.sample_1_marker_1_button.bind('<Button-1>', lambda event, mode=1, qualifier=1,
            color=self.samples.colors[1]: self.activate_marker(event, mode, qualifier, color))

        self.sample_1_marker_2_button = ttk.Button(self.sample_1_frame, width=5, textvariable=self.qualifier_2)
        self.sample_1_marker_2_button.place(x=47, y=27)
        self.sample_1_marker_2_button.bind('<Button-1>', lambda event, mode=1, qualifier=2,
            color=self.samples.colors[1]: self.activate_marker(event, mode, qualifier, color))

        self.sample_1_marker_3_button = ttk.Button(self.sample_1_frame, width=5, textvariable=self.qualifier_3)
        self.sample_1_marker_3_button.place(x=89, y=27)
        self.sample_1_marker_3_button.bind('<Button-1>', lambda event, mode=1, qualifier=3,
            color=self.samples.colors[1]: self.activate_marker(event, mode, qualifier, color))

        self.sample_1_marker_4_button = ttk.Button(self.sample_1_frame, width=5, textvariable=self.qualifier_4)
        self.sample_1_marker_4_button.place(x=131, y=27)
        self.sample_1_marker_4_button.bind('<Button-1>', lambda event, mode=1, qualifier=4,
            color=self.samples.colors[1]: self.activate_marker(event, mode, qualifier, color))

        self.color_1_label = ttk.Label(self.sample_1_frame, text='Color:')
        self.color_1_label.place(x=173, y=30)

        self.sample_1_color = Label(self.sample_1_frame, width=3, bg=self.samples.colors[1])
        self.sample_1_color.place(x=210, y=29)
        self.sample_1_color.bind('<Button-1>', lambda event, sample_number=1: self.choose_marker_color(event, sample_number))

        #
        # Sample 2
        #
        self.sample_2_frame = ttk.Frame(self.markers_tab, width=sample_frame_width, height=sample_frame_height)
        self.sample_2_frame.place(x=0, y=sample_frame_height * 1)

        self.sample_2_entry = ttk.Entry(self.sample_2_frame, width=38, justify=CENTER, textvariable=self.sample_2_name)
        self.sample_2_entry.place(x=5, y=5)
        self.sample_2_entry.bind('<Return>', self.update_samples_names)
        self.sample_2_entry.bind('<FocusOut>', self.update_samples_names)

        self.sample_2_marker_1_button = ttk.Button(self.sample_2_frame, width=5, textvariable=self.qualifier_1)
        self.sample_2_marker_1_button.place(x=5, y=27)
        self.sample_2_marker_1_button.bind('<Button-1>', lambda event, mode=2, qualifier=1,
            color=self.samples.colors[2]: self.activate_marker(event, mode, qualifier, color))

        self.sample_2_marker_2_button = ttk.Button(self.sample_2_frame, width=5, textvariable=self.qualifier_2)
        self.sample_2_marker_2_button.place(x=47, y=27)
        self.sample_2_marker_2_button.bind('<Button-1>', lambda event, mode=2, qualifier=2,
            color=self.samples.colors[2]: self.activate_marker(event, mode, qualifier, color))

        self.sample_2_marker_3_button = ttk.Button(self.sample_2_frame, width=5, textvariable=self.qualifier_3)
        self.sample_2_marker_3_button.place(x=89, y=27)
        self.sample_2_marker_3_button.bind('<Button-1>', lambda event, mode=2, qualifier=3,
            color=self.samples.colors[2]: self.activate_marker(event, mode, qualifier, color))

        self.sample_2_marker_4_button = ttk.Button(self.sample_2_frame, width=5, textvariable=self.qualifier_4)
        self.sample_2_marker_4_button.place(x=131, y=27)
        self.sample_2_marker_4_button.bind('<Button-1>', lambda event, mode=2, qualifier=4,
            color=self.samples.colors[2]: self.activate_marker(event, mode, qualifier, color))

        self.color_2_label = ttk.Label(self.sample_2_frame, text='Color:')
        self.color_2_label.place(x=173, y=30)

        self.sample_2_color = Label(self.sample_2_frame, width=3, bg=self.samples.colors[2])
        self.sample_2_color.place(x=210, y=29)
        self.sample_2_color.bind('<Button-1>', lambda event, sample_number=2: self.choose_marker_color(event, sample_number))

        #
        # Sample 3
        #
        self.sample_3_frame = ttk.Frame(self.markers_tab, width=sample_frame_width, height=sample_frame_height)
        self.sample_3_frame.place(x=0, y=sample_frame_height * 2)

        self.sample_3_entry = ttk.Entry(self.sample_3_frame, width=38, justify=CENTER, textvariable=self.sample_3_name)
        self.sample_3_entry.place(x=5, y=5)
        self.sample_3_entry.bind('<Return>', self.update_samples_names)
        self.sample_3_entry.bind('<FocusOut>', self.update_samples_names)

        self.sample_3_marker_1_button = ttk.Button(self.sample_3_frame, width=5, textvariable=self.qualifier_1)
        self.sample_3_marker_1_button.place(x=5, y=27)
        self.sample_3_marker_1_button.bind('<Button-1>', lambda event, mode=3, qualifier=1,
            color=self.samples.colors[3]: self.activate_marker(event, mode, qualifier, color))

        self.sample_3_marker_2_button = ttk.Button(self.sample_3_frame, width=5, textvariable=self.qualifier_2)
        self.sample_3_marker_2_button.place(x=47, y=27)
        self.sample_3_marker_2_button.bind('<Button-1>', lambda event, mode=3, qualifier=2,
            color=self.samples.colors[3]: self.activate_marker(event, mode, qualifier, color))

        self.sample_3_marker_3_button = ttk.Button(self.sample_3_frame, width=5, textvariable=self.qualifier_3)
        self.sample_3_marker_3_button.place(x=89, y=27)
        self.sample_3_marker_3_button.bind('<Button-1>', lambda event, mode=3, qualifier=3,
            color=self.samples.colors[3]: self.activate_marker(event, mode, qualifier, color))

        self.sample_3_marker_4_button = ttk.Button(self.sample_3_frame, width=5, textvariable=self.qualifier_4)
        self.sample_3_marker_4_button.place(x=131, y=27)
        self.sample_3_marker_4_button.bind('<Button-1>', lambda event, mode=3, qualifier=4,
            color=self.samples.colors[3]: self.activate_marker(event, mode, qualifier, color))

        self.color_3_label = ttk.Label(self.sample_3_frame, text='Color:')
        self.color_3_label.place(x=173, y=30)

        self.sample_3_color = Label(self.sample_3_frame, width=3, bg=self.samples.colors[3])
        self.sample_3_color.place(x=210, y=29)
        self.sample_3_color.bind('<Button-1>', lambda event, sample_number=3: self.choose_marker_color(event, sample_number))

        #
        # Sample 4
        #
        self.sample_4_frame = ttk.Frame(self.markers_tab, width=sample_frame_width, height=sample_frame_height)
        self.sample_4_frame.place(x=0, y=sample_frame_height * 3)

        self.sample_4_entry = ttk.Entry(self.sample_4_frame, width=38, justify=CENTER, textvariable=self.sample_4_name)
        self.sample_4_entry.place(x=5, y=5)
        self.sample_4_entry.bind('<Return>', self.update_samples_names)
        self.sample_4_entry.bind('<FocusOut>', self.update_samples_names)

        self.sample_4_marker_1_button = ttk.Button(self.sample_4_frame, width=5, textvariable=self.qualifier_1)
        self.sample_4_marker_1_button.place(x=5, y=27)
        self.sample_4_marker_1_button.bind('<Button-1>', lambda event, mode=4, qualifier=1,
            color=self.samples.colors[4]: self.activate_marker(event, mode, qualifier, color))

        self.sample_4_marker_2_button = ttk.Button(self.sample_4_frame, width=5, textvariable=self.qualifier_2)
        self.sample_4_marker_2_button.place(x=47, y=27)
        self.sample_4_marker_2_button.bind('<Button-1>', lambda event, mode=4, qualifier=2,
            color=self.samples.colors[4]: self.activate_marker(event, mode, qualifier, color))

        self.sample_4_marker_3_button = ttk.Button(self.sample_4_frame, width=5, textvariable=self.qualifier_3)
        self.sample_4_marker_3_button.place(x=89, y=27)
        self.sample_4_marker_3_button.bind('<Button-1>', lambda event, mode=4, qualifier=3,
            color=self.samples.colors[4]: self.activate_marker(event, mode, qualifier, color))

        self.sample_4_marker_4_button = ttk.Button(self.sample_4_frame, width=5, textvariable=self.qualifier_4)
        self.sample_4_marker_4_button.place(x=131, y=27)
        self.sample_4_marker_4_button.bind('<Button-1>', lambda event, mode=4, qualifier=4,
            color=self.samples.colors[4]: self.activate_marker(event, mode, qualifier, color))

        self.color_4_label = ttk.Label(self.sample_4_frame, text='Color:')
        self.color_4_label.place(x=173, y=30)

        self.sample_4_color = Label(self.sample_4_frame, width=3, bg=self.samples.colors[4])
        self.sample_4_color.place(x=210, y=29)
        self.sample_4_color.bind('<Button-1>', lambda event, sample_number=4: self.choose_marker_color(event, sample_number))

        #
        # Sample 5
        #
        self.sample_5_frame = ttk.Frame(self.markers_tab, width=sample_frame_width, height=sample_frame_height)
        self.sample_5_frame.place(x=0, y=sample_frame_height * 4)

        self.sample_5_entry = ttk.Entry(self.sample_5_frame, width=38, justify=CENTER, textvariable=self.sample_5_name)
        self.sample_5_entry.place(x=5, y=5)
        self.sample_5_entry.bind('<Return>', self.update_samples_names)
        self.sample_5_entry.bind('<FocusOut>', self.update_samples_names)

        self.sample_5_marker_1_button = ttk.Button(self.sample_5_frame, width=5, textvariable=self.qualifier_1)
        self.sample_5_marker_1_button.place(x=5, y=27)
        self.sample_5_marker_1_button.bind('<Button-1>', lambda event, mode=5, qualifier=1,
            color=self.samples.colors[5]: self.activate_marker(event, mode, qualifier, color))

        self.sample_5_marker_2_button = ttk.Button(self.sample_5_frame, width=5, textvariable=self.qualifier_2)
        self.sample_5_marker_2_button.place(x=47, y=27)
        self.sample_5_marker_2_button.bind('<Button-1>', lambda event, mode=5, qualifier=2,
            color=self.samples.colors[5]: self.activate_marker(event, mode, qualifier, color))

        self.sample_5_marker_3_button = ttk.Button(self.sample_5_frame, width=5, textvariable=self.qualifier_3)
        self.sample_5_marker_3_button.place(x=89, y=27)
        self.sample_5_marker_3_button.bind('<Button-1>', lambda event, mode=5, qualifier=3,
            color=self.samples.colors[5]: self.activate_marker(event, mode, qualifier, color))

        self.sample_5_marker_4_button = ttk.Button(self.sample_5_frame, width=5, textvariable=self.qualifier_4)
        self.sample_5_marker_4_button.place(x=131, y=27)
        self.sample_5_marker_4_button.bind('<Button-1>', lambda event, mode=5, qualifier=4,
            color=self.samples.colors[5]: self.activate_marker(event, mode, qualifier, color))

        self.color_5_label = ttk.Label(self.sample_5_frame, text='Color:')
        self.color_5_label.place(x=173, y=30)

        self.sample_5_color = Label(self.sample_5_frame, width=3, bg=self.samples.colors[5])
        self.sample_5_color.place(x=210, y=29)
        self.sample_5_color.bind('<Button-1>', lambda event, sample_number=5: self.choose_marker_color(event, sample_number))

        #
        # Sample 6
        #
        self.sample_6_frame = ttk.Frame(self.markers_tab, width=sample_frame_width, height=sample_frame_height)
        self.sample_6_frame.place(x=0, y=sample_frame_height * 5)

        self.sample_6_entry = ttk.Entry(self.sample_6_frame, width=38, justify=CENTER, textvariable=self.sample_6_name)
        self.sample_6_entry.place(x=5, y=5)
        self.sample_6_entry.bind('<Return>', self.update_samples_names)
        self.sample_6_entry.bind('<FocusOut>', self.update_samples_names)

        self.sample_6_marker_1_button = ttk.Button(self.sample_6_frame, width=5, textvariable=self.qualifier_1)
        self.sample_6_marker_1_button.place(x=5, y=27)
        self.sample_6_marker_1_button.bind('<Button-1>', lambda event, mode=6, qualifier=1,
            color=self.samples.colors[6]: self.activate_marker(event, mode, qualifier, color))

        self.sample_6_marker_2_button = ttk.Button(self.sample_6_frame, width=5, textvariable=self.qualifier_2)
        self.sample_6_marker_2_button.place(x=47, y=27)
        self.sample_6_marker_2_button.bind('<Button-1>', lambda event, mode=6, qualifier=2,
            color=self.samples.colors[6]: self.activate_marker(event, mode, qualifier, color))

        self.sample_6_marker_3_button = ttk.Button(self.sample_6_frame, width=5, textvariable=self.qualifier_3)
        self.sample_6_marker_3_button.place(x=89, y=27)
        self.sample_6_marker_3_button.bind('<Button-1>', lambda event, mode=6, qualifier=3,
            color=self.samples.colors[6]: self.activate_marker(event, mode, qualifier, color))

        self.sample_6_marker_4_button = ttk.Button(self.sample_6_frame, width=5, textvariable=self.qualifier_4)
        self.sample_6_marker_4_button.place(x=131, y=27)
        self.sample_6_marker_4_button.bind('<Button-1>', lambda event, mode=6, qualifier=4,
            color=self.samples.colors[6]: self.activate_marker(event, mode, qualifier, color))

        self.color_6_label = ttk.Label(self.sample_6_frame, text='Color:')
        self.color_6_label.place(x=173, y=30)

        self.sample_6_color = Label(self.sample_6_frame, width=3, bg=self.samples.colors[6])
        self.sample_6_color.place(x=210, y=29)
        self.sample_6_color.bind('<Button-1>', lambda event, sample_number=6: self.choose_marker_color(event, sample_number))

        #
        # Sample 7
        #
        self.sample_7_frame = ttk.Frame(self.markers_tab, width=sample_frame_width, height=sample_frame_height)
        self.sample_7_frame.place(x=0, y=sample_frame_height * 6)

        self.sample_7_entry = ttk.Entry(self.sample_7_frame, width=38, justify=CENTER, textvariable=self.sample_7_name)
        self.sample_7_entry.place(x=5, y=5)
        self.sample_7_entry.bind('<Return>', self.update_samples_names)
        self.sample_7_entry.bind('<FocusOut>', self.update_samples_names)

        self.sample_7_marker_1_button = ttk.Button(self.sample_7_frame, width=5, textvariable=self.qualifier_1)
        self.sample_7_marker_1_button.place(x=5, y=27)
        self.sample_7_marker_1_button.bind('<Button-1>', lambda event, mode=7, qualifier=1,
            color=self.samples.colors[7]: self.activate_marker(event, mode, qualifier, color))

        self.sample_7_marker_2_button = ttk.Button(self.sample_7_frame, width=5, textvariable=self.qualifier_2)
        self.sample_7_marker_2_button.place(x=47, y=27)
        self.sample_7_marker_2_button.bind('<Button-1>', lambda event, mode=7, qualifier=2,
            color=self.samples.colors[7]: self.activate_marker(event, mode, qualifier, color))

        self.sample_7_marker_3_button = ttk.Button(self.sample_7_frame, width=5, textvariable=self.qualifier_3)
        self.sample_7_marker_3_button.place(x=89, y=27)
        self.sample_7_marker_3_button.bind('<Button-1>', lambda event, mode=7, qualifier=3,
            color=self.samples.colors[7]: self.activate_marker(event, mode, qualifier, color))

        self.sample_7_marker_4_button = ttk.Button(self.sample_7_frame, width=5, textvariable=self.qualifier_4)
        self.sample_7_marker_4_button.place(x=131, y=27)
        self.sample_7_marker_4_button.bind('<Button-1>', lambda event, mode=7, qualifier=4,
            color=self.samples.colors[7]: self.activate_marker(event, mode, qualifier, color))

        self.color_7_label = ttk.Label(self.sample_7_frame, text='Color:')
        self.color_7_label.place(x=173, y=30)

        self.sample_7_color = Label(self.sample_7_frame, width=3, bg=self.samples.colors[7])
        self.sample_7_color.place(x=210, y=29)
        self.sample_7_color.bind('<Button-1>', lambda event, sample_number=7: self.choose_marker_color(event, sample_number))

        #
        # Sample 8
        #
        self.sample_8_frame = ttk.Frame(self.markers_tab, width=sample_frame_width, height=sample_frame_height)
        self.sample_8_frame.place(x=0, y=sample_frame_height * 7)

        self.sample_8_entry = ttk.Entry(self.sample_8_frame, width=38, justify=CENTER, textvariable=self.sample_8_name)
        self.sample_8_entry.place(x=5, y=5)
        self.sample_8_entry.bind('<Return>', self.update_samples_names)
        self.sample_8_entry.bind('<FocusOut>', self.update_samples_names)

        self.sample_8_marker_1_button = ttk.Button(self.sample_8_frame, width=5, textvariable=self.qualifier_1)
        self.sample_8_marker_1_button.place(x=5, y=27)
        self.sample_8_marker_1_button.bind('<Button-1>', lambda event, mode=8, qualifier=1,
            color=self.samples.colors[8]: self.activate_marker(event, mode, qualifier, color))

        self.sample_8_marker_2_button = ttk.Button(self.sample_8_frame, width=5, textvariable=self.qualifier_2)
        self.sample_8_marker_2_button.place(x=47, y=27)
        self.sample_8_marker_2_button.bind('<Button-1>', lambda event, mode=8, qualifier=2,
            color=self.samples.colors[8]: self.activate_marker(event, mode, qualifier, color))

        self.sample_8_marker_3_button = ttk.Button(self.sample_8_frame, width=5, textvariable=self.qualifier_3)
        self.sample_8_marker_3_button.place(x=89, y=27)
        self.sample_8_marker_3_button.bind('<Button-1>', lambda event, mode=8, qualifier=3,
            color=self.samples.colors[8]: self.activate_marker(event, mode, qualifier, color))

        self.sample_8_marker_4_button = ttk.Button(self.sample_8_frame, width=5, textvariable=self.qualifier_4)
        self.sample_8_marker_4_button.place(x=131, y=27)
        self.sample_8_marker_4_button.bind('<Button-1>', lambda event, mode=8, qualifier=4,
            color=self.samples.colors[8]: self.activate_marker(event, mode, qualifier, color))

        self.color_8_label = ttk.Label(self.sample_8_frame, text='Color:')
        self.color_8_label.place(x=173, y=30)

        self.sample_8_color = Label(self.sample_8_frame, width=3, bg=self.samples.colors[8])
        self.sample_8_color.place(x=210, y=29)
        self.sample_8_color.bind('<Button-1>', lambda event, sample_number=8: self.choose_marker_color(event, sample_number))

        #self.mainWidget.update_idletasks()

        #Dictionary of elements.
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

    def build_options_gui(self):
        qualifiers_options_frame_width = self.markers_tab.winfo_width() - 10
        qualifiers_options_frame = 53

        self.qualifiers_options_frame = ttk.LabelFrame(
            self.options_tab,
            width=qualifiers_options_frame_width,
            height=qualifiers_options_frame,
            text='Change qualifiers')
        self.qualifiers_options_frame.place(x=5, y=5)

        #self.mainWidget.update_idletasks()

    def activate_marker(self, event, mode, qualifier, color):
        #print('name:{} mode:{} color:{}'.format(name, mode, color))

        for k, v in self.samples_and_markers_buttons.items():
            if k == 'sample_{}_marker_{}_button'.format(mode, qualifier):
                v.state(['disabled'])
            else:
                v.state(['!disabled'])

    def choose_marker_color(self, event, sample_number):
        new_color = askcolor()[1]

        if new_color:
            self.samples.colors[sample_number] = new_color

            for k, v in self.samples_colors.items():
                if k == sample_number:
                    print('Found: {}'.format(sample_number))
                    v.configure(bg=new_color)

        self.mainWidget.update()

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

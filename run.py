#!/usr/bin/env python3


from manage_settings import ManageSettings
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

    def __init__(self, mainWidget, screen_width, screen_height, settings):
        '''
        Main Window of the program.
        Contains all necessary elements to navigate and use all functionalities.

        Args:
            settings: instance - instance of ManageSettings class.
            mainWidget: instance - instance of the Tk() class.
            screen_width: int - width of the screen.
            screen_height: int - width of the screen.
        '''
        self.settings = settings
        self.mainWidget = mainWidget
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.status_bar_text = StringVar()
        self.status_bar_text.set('')

        #Menus
        self.drop_down_menu = Menu(self.mainWidget)
        self.mainWidget.config(menu=self.drop_down_menu)

        self.file_menu = Menu(self.drop_down_menu, tearoff=0)
        self.drop_down_menu.add_cascade(label='File', menu=self.file_menu)
        self.file_menu.add_command(label='Open file', command=self.placeholder)
        self.file_menu.add_command(label='Save file', command=self.placeholder)
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Exit', command=self.mainWidget.quit)

        self.window_options_menu = Menu(self.drop_down_menu, tearoff=0)
        self.drop_down_menu.add_cascade(label='Window', menu=self.window_options_menu)
        #self.window_options_menu.add_command(label='Always on top', command=self.change_top_mode)
        self.window_options_menu.add_checkbutton(label='Always on top', onvalue=True, offvalue=False, command=self.change_top_mode)


        self.about_menu = Menu(self.drop_down_menu, tearoff=0)
        self.drop_down_menu.add_cascade(label='About', menu=self.about_menu)
        self.about_menu.add_command(label='Info', command=self.placeholder)

        #Main frame.
        self.main_frame = ttk.Frame(self.mainWidget, width=self.screen_width, height=self.screen_height-20, padding=(0, 0, 0, 0))
        self.main_frame.place(x=0, y=0)

        self.status_bar = ttk.Label(self.mainWidget, width=self.screen_width, anchor=W, border=0, relief=SUNKEN, textvariable=self.status_bar_text)
        self.status_bar.place(x=0, y=self.screen_height-19)

        self.mainWidget.update_idletasks()
        self.build_main_gui()

    def build_main_gui(self):
        '''
        Building the picture frame and all it's elements and options frame.
        '''

        toolbar_width = 250
        scrollbar_thickness = 18
        canvas_frame_width = self.main_frame.winfo_width() - toolbar_width - scrollbar_thickness
        canvas_frame_height = self.main_frame.winfo_height() - scrollbar_thickness
        notebook_width =  toolbar_width - 5
        notebook_height = self.main_frame.winfo_height() - 46

        self.picture_frame = ttk.Frame(self.main_frame, width=self.screen_width-toolbar_width, height=self.screen_height-20)
        self.picture_frame.place(x=0, y=0)

        self.canvas_frame = ttk.Frame(self.picture_frame, relief=GROOVE, width=canvas_frame_width, height=canvas_frame_height)
        self.canvas_frame.place(x=0, y=0)

        self.scrollbar_x_frame = ttk.Frame(self.picture_frame, relief=GROOVE, width=canvas_frame_width, height=scrollbar_thickness)
        self.scrollbar_x_frame.place(x=0, y=canvas_frame_height)

        self.scrollbar_y_frame = ttk.Frame(self.picture_frame, relief=GROOVE, width=scrollbar_thickness, height=canvas_frame_height)
        self.scrollbar_y_frame.place(x=canvas_frame_width, y=0)

        self.toolbar_frame = ttk.Frame(self.main_frame, width=toolbar_width, height=self.screen_height-20)
        self.toolbar_frame.place(x=self.screen_width-toolbar_width, y=0)

        self.notebook = ttk.Notebook(self.toolbar_frame)
        self.notebook.place(x=0, y=0)


        self.tab_1 = ttk.Frame(self.notebook, width=notebook_width, height=notebook_height)
        self.tab_2 = ttk.Frame(self.notebook, width=notebook_width, height=notebook_height)
        self.tab_3 = ttk.Frame(self.notebook, width=notebook_width, height=notebook_height)

        self.notebook.add(self.tab_1, text='Markers')
        self.notebook.add(self.tab_2, text='Statistics')
        self.notebook.add(self.tab_3, text='Something')

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

    def remove_elements(self, elements):
        for element in elements:
            element.destroy()

    def placeholder(self):
        print('This is a simple placeholder message.')


def main():
    raw_settings = SettingsUtilities.load_settings_file(SETTINGS_PATH)
    settings = ManageSettings(**raw_settings)

    root = Tk()
    screen_width, screen_height = settings.set_screen_resolution
    screen_width -= settings.screen_horizontal_margin
    screen_height -= settings.screen_vertical_margin

    root.geometry('{}x{}+5+5'.format(screen_width, screen_height))
    root.title('Bio Counter')


    if settings.always_on_top == True:
        root.wm_attributes('-topmost', 1)
    else:
        root.wm_attributes('-topmost', 0)

    if settings.window_is_resizable == True:
        root.resizable(width=1, height=1)
    else:
        root.resizable(width=0, height=0)

    window = Window(root, screen_width, screen_height, settings)
    window

    root.mainloop()


if __name__ == '__main__':
    if platform.system() == 'Windows':
        main()
    else:
        print('Platform not supported.')

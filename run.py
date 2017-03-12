#!/usr/bin/env python3


from screen_utilities import ScreenUtilities
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter import messagebox
import codecs
import platform


__author__ = 'Mariusz Kowalski'


class Window:

    def __init__(self, mainWidget, screen_width, screen_height):
        '''
        Main Window of the program.
        Contains all necessary elements to navigate and use all functionalities.

        Args:
            mainWidget: instance - instance of the Tk() class.
            screen_width: int - width of the screen.
            screen_height: int - width of the screen.
        '''
        self.mainWidget = mainWidget
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.always_on_top = False

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

        self.build_main_gui()

    def build_main_gui(self):
        '''
        Building the picture frame and all it's elements and options frame.
        '''

        toolbar_width = 250
        scrollbar_thickness = 18
        canvas_frame_width = self.screen_width - toolbar_width - scrollbar_thickness
        canvas_frame_height = self.screen_height - 38
        notebook_width =  toolbar_width - 5
        notebook_height = self.screen_height - 46

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

        if self.always_on_top:
            self.mainWidget.wm_attributes('-topmost', 0)
            self.always_on_top = False
        else:
            self.mainWidget.wm_attributes('-topmost', 1)
            self.always_on_top = True

    def remove_elements(self, elements):
        for element in elements:
            element.destroy()

    def placeholder(self):
        print('This is a simple placeholder message.')


def main():
    root = Tk()
    screen_width, screen_height = ScreenUtilities.check_resolution(root.winfo_screenwidth(), root.winfo_screenheight())
    screen_width -= 15
    screen_height -= 90
    root.geometry('{}x{}+5+5'.format(screen_width, screen_height))
    root.title('Bio Counter')
    root.wm_attributes('-topmost', 0)
    root.resizable(width=0, height=0)

    window = Window(root, screen_width, screen_height)
    window

    root.mainloop()


if __name__ == '__main__':
    if platform.system() == 'Windows':
        main()
    else:
        print('Platform not supported.')

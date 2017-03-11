#!/usr/bin/env python3


from screen_utilities import ScreenUtilities
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter import messagebox
import codecs
import platform


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

        self.screen_width = screen_width
        self.screen_height = screen_height

        self.status_bar_text = StringVar()
        self.status_bar_text.set('')

        self.main_frame = ttk.Frame(mainWidget, width=self.screen_width, height=self.screen_height-20, padding=(0, 0, 0, 0))
        self.main_frame.place(x=0, y=0)

        self.status_bar = ttk.Label(mainWidget, width=self.screen_width, anchor=W, border=0, relief=SUNKEN, textvariable=self.status_bar_text)
        self.status_bar.place(x=0, y=self.screen_height-20)

        self.main_gui()

    def main_gui(self):
        pass

    def remove_elements(self, elements):
        for element in elements:
            element.destroy()


def main():
    root = Tk()
    screen_width, screen_height = ScreenUtilities.check_resolution(root.winfo_screenwidth(), root.winfo_screenheight())
    screen_width -= 15
    screen_height -= 70
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

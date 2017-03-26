#!/usr/bin/env python3


from tkinter import *
from tkinter import ttk


class Main_gui:

    def __init__(self, picture_frame, widget_geometries):
        '''
        Building the picture frame and all it's elements and options frame.
        '''
        self.picture_frame = picture_frame
        self.widget_geometries = widget_geometries

        self.canvas_frame = ttk.Frame(self.picture_frame,
                                      width=self.widget_geometries.canvas_frame_width,
                                      height=self.widget_geometries.canvas_frame_height)
        self.canvas_frame.place(x=0, y=0)

        self.scrollbar_x_frame = ttk.Frame(self.picture_frame,
                                           width=self.widget_geometries.canvas_frame_width,
                                           height=self.widget_geometries.scrollbar_thickness)
        self.scrollbar_x_frame.place(x=0, y=self.widget_geometries.canvas_frame_height)

        self.scrollbar_y_frame = ttk.Frame(self.picture_frame,
                                           width=self.widget_geometries.scrollbar_thickness,
                                           height=self.widget_geometries.canvas_frame_height)
        self.scrollbar_y_frame.place(x=self.widget_geometries.canvas_frame_width, y=0)

        self.canvas = Canvas(self.canvas_frame,
                             width=self.widget_geometries.canvas_frame_width,
                             height=self.widget_geometries.canvas_frame_height,
                             borderwidth=0,
                             highlightthickness=0)
        self.canvas.place(x=0, y=0)
        self.canvas.bind('<Button-1>', self.place_marker_on_canvas)
        self.canvas.bind('<MouseWheel>', self.use_mousewheel_on_canvas)
        self.canvas.bind('<Shift-MouseWheel>', self.use_mousewheel_and_shift_on_canvas)
        self.canvas.bind('<Control-MouseWheel>', self.use_mousewheel_and_ctrl_on_canvas)

    def place_image_on_canvas(self, image_object):
        self.image_object = image_object
        self.image_object_width = self.image_object.width()
        self.image_object_height = self.image_object.height()

        self.canvas.create_image(self.image_object_width / 2,
                                 self.image_object_height / 2,
                                 tags='image',
                                 image=self.image_object)

        self.scrollbar_x = ttk.Scrollbar(self.scrollbar_x_frame, orient=HORIZONTAL)
        self.scrollbar_x.place(x=0, y=0, relwidth=1.0)
        self.scrollbar_x.config(command=self.canvas.xview)

        self.scrollbar_y = ttk.Scrollbar(self.scrollbar_y_frame, orient=VERTICAL)
        self.scrollbar_y.place(x=0, y=0, relheight=1.0)
        self.scrollbar_y.config(command=self.canvas.yview)

        self.canvas.config(width=self.widget_geometries.canvas_frame_width,
                           height=self.widget_geometries.canvas_frame_height,
                           xscrollcommand=self.scrollbar_x.set,
                           yscrollcommand=self.scrollbar_y.set,
                           scrollregion=(0, 0, self.image_object_width, self.image_object_height))
        self.canvas.focus()

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

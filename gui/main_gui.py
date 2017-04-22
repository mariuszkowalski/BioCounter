#!/usr/bin/env python3


from tkinter import *
from tkinter import ttk

from PIL import ImageTk

from markers.marker import Marker
from markers.marker_utilities import MarkerUtilities
from markers.shapes import Shapes


class Main_gui:

    def __init__(self, picture_frame, widget_geometries, samples, statistics, texts):
        '''
        Building the picture frame and all it's elements and options frame.

        Args:
            picture_frame: instance - module Tkinter class ttk.Frame
            widget_geometries instance - class Widget_geometries
            samples: instance - class Samples
            statistics: instance - class Statistics
            texts: instance - class Texts
        '''

        self.picture_frame = picture_frame
        self.widget_geometries = widget_geometries[0]
        self.samples = samples[0]
        self.statistics = statistics[0]
        self.texts = texts[0]

        self.valid_marker_tags = ['1', '2', '3', '4', '5', '6', '7', '8']

        self.image_scale = 1.0
        self.old_image_scale = None
        self.raw_image_object = None
        self.resized_image_object = None

        self.canvas_frame = ttk.Frame(
            self.picture_frame,
            width=self.widget_geometries.canvas_frame_width,
            height=self.widget_geometries.canvas_frame_height)
        self.canvas_frame.place(x=0, y=0)

        self.scrollbar_x_frame = ttk.Frame(
            self.picture_frame,
            width=self.widget_geometries.canvas_frame_width,
            height=self.widget_geometries.scrollbar_thickness)
        self.scrollbar_x_frame.place(x=0, y=self.widget_geometries.canvas_frame_height)

        self.scrollbar_y_frame = ttk.Frame(
            self.picture_frame,
            width=self.widget_geometries.scrollbar_thickness,
            height=self.widget_geometries.canvas_frame_height)
        self.scrollbar_y_frame.place(x=self.widget_geometries.canvas_frame_width, y=0)

        self.canvas = Canvas(
            self.canvas_frame,
            width=self.widget_geometries.canvas_frame_width,
            height=self.widget_geometries.canvas_frame_height,
            borderwidth=0,
            highlightthickness=0,
            scrollregion = (
                0,
                0,
                self.widget_geometries.canvas_frame_width,
                self.widget_geometries.canvas_frame_height))
        self.canvas.place(x=0, y=0)
        self.canvas.bind('<Button-1>', self.place_marker_on_canvas)
        self.canvas.bind('<Button-3>', self.remove_marker_from_canvas)
        self.canvas.bind('<MouseWheel>', self.use_mousewheel_on_canvas)
        self.canvas.bind('<Shift-MouseWheel>', self.use_mousewheel_and_shift_on_canvas)
        self.canvas.bind('<Control-MouseWheel>', self.use_mousewheel_and_ctrl_on_canvas)

    def place_image_on_canvas(self, raw_image_object):
        '''
        Places image oo center of the canvas.

        Args:
            raw_image_object: instance - the module PIL class Image.

        Return:
            No return in the method
        '''

        self.raw_image_object = raw_image_object
        self.image_object = ImageTk.PhotoImage(self.raw_image_object)

        self.image_object_width = self.image_object.width()
        self.image_object_height = self.image_object.height()

        self.canvas.create_image(
            self.image_object_width / 2,
            self.image_object_height / 2,
            tags='image',
            image=self.image_object)

        self.scrollbar_x = ttk.Scrollbar(self.scrollbar_x_frame, orient=HORIZONTAL)
        self.scrollbar_x.place(x=0, y=0, relwidth=1.0)
        self.scrollbar_x.config(command=self.canvas.xview)

        self.scrollbar_y = ttk.Scrollbar(self.scrollbar_y_frame, orient=VERTICAL)
        self.scrollbar_y.place(x=0, y=0, relheight=1.0)
        self.scrollbar_y.config(command=self.canvas.yview)

        self.canvas.config(
            width=self.widget_geometries.canvas_frame_width,
            height=self.widget_geometries.canvas_frame_height,
            xscrollcommand=self.scrollbar_x.set,
            yscrollcommand=self.scrollbar_y.set,
            scrollregion=(
                0,
                0,
                self.image_object_width,
                self.image_object_height))
        self.canvas.focus()

    def place_marker_on_canvas(self, event):
        '''
        Places activated marker with the correct mode and qualifier in the canvas
        using the coordinates from the event, recalculated to the corresponding
        coordinate on canvas.
        '''

        active_canvas = event.widget
        x = active_canvas.canvasx(event.x)
        y = active_canvas.canvasy(event.y)

        if self.samples.activated_marker:
            mode = self.samples.activated_marker['mode']
            qualifier = self.samples.activated_marker['qualifier']
            color = self.samples.activated_marker['color']
            size = self.widget_geometries.marker_size
            image_scale = self.image_scale

            self.draw_marker_on_canvas(size, color, mode, qualifier, x, y, image_scale, False)##############

            canvas_index = self.canvas.find_all()[-1]

            #
            # Does know what scale is...
            #
            adjusted_x, adjusted_y = MarkerUtilities.adjust_recorded_position(x, y, image_scale)

            print('SCALE: {}; CLICK: {}, {}; MARKER SET: {}, {}; ADJUSTED: {}, {}'.format(image_scale, event.x, event.y, x, y, adjusted_x, adjusted_y))

            marker = Marker(canvas_index, size, mode, qualifier, adjusted_x, adjusted_y)
            self.samples.placed_markers.append(marker)

            self.statistics.change_stat(mode, qualifier, True)
            self.texts.update_statistic_texts()

    def replace_markers_of_changed_color(self, mode):
        '''
        Deletes markers that has changed color from the canvas and
        creates those again with new color assigned.

        Args:
            mode: int - mode of the marker activated
                integer in range 1-8

        Return:
            No return in the method
        '''

        markers_to_delete = self.canvas.find_all()

        for element in markers_to_delete:
            # Checks only for one mode, of an marker that changed color.
            if self.canvas.gettags(element)[0] == str(mode):
                self.canvas.delete(element)

        for current_marker in self.samples.placed_markers:
            if mode == current_marker.mode:
                size = current_marker.size
                qualifier = current_marker.qualifier
                color = self.samples.colors[mode]
                x = current_marker.position_x
                y = current_marker.position_y
                image_scale = self.image_scale

                self.draw_marker_on_canvas(size, color, mode, qualifier, x, y, image_scale, True)################

                new_index = self.canvas.find_all()[-1]
                current_marker.canvas_index = new_index

    def redraw_all_markers(self):
        '''
        Deletes all the markers placed on the canvas and all the other elements and
        redraws all the markers from the list.
        '''

        markers_to_delete = self.canvas.find_all()

        for element in markers_to_delete:
            # Checks for all valid marker tags.
            if self.canvas.gettags(element)[0] in self.valid_marker_tags:
                self.canvas.delete(element)

        for current_marker in self.samples.placed_markers:
            current_marker.size = self.widget_geometries.marker_size
            size = current_marker.size
            mode = current_marker.mode
            qualifier = current_marker.qualifier
            color = self.samples.colors[current_marker.mode]
            x = current_marker.position_x
            y = current_marker.position_y
            image_scale = self.image_scale

            print(' ---- REDRAW ---- ')
            print('MARKER DATA // {}, {}'.format(x, y))
            self.draw_marker_on_canvas(size, color, mode, qualifier, x, y, image_scale, True)###################

            new_index = self.canvas.find_all()[-1]
            current_marker.canvas_index = new_index

    def remove_marker_from_canvas(self, event):
        '''
        Removes given marker from canvas which is overlapping with the test area.
        '''

        active_canvas = event.widget
        x = active_canvas.canvasx(event.x)
        y = active_canvas.canvasy(event.y)

        markers_to_remove = self.canvas.find_overlapping(x-2, y-2, x+2, y+2)

        for element in markers_to_remove:
            # Checks for all valid marker tags.
            if self.canvas.gettags(element)[0] in self.valid_marker_tags:
                self.canvas.delete(element)

        for i, element in enumerate(self.samples.placed_markers):
            if element.canvas_index in markers_to_remove:

                mode = element.mode
                qualifier = element.qualifier

                self.statistics.change_stat(mode, qualifier, False)
                self.texts.update_statistic_texts()

                del self.samples.placed_markers[i]

    def draw_marker_on_canvas(self, size, color, mode, qualifier, x, y, image_scale, redraw):
        '''
        Draws the marker on the canvas, using the passed parameters.

        Args:
            size: int - contains the current size of the marker specified
            color: string -  this is passed in the format:
                "'#{:02X}{:02X}{:02X}'.format(255, 100, 100)"
                the numbers corresponds to the RGB color palette
            mode: int - mode of the marker activated
                integer in range 1-8
            qualifier: int - qualifier of the marker activated
                integer in range 1-4
            x: int - horizontal position of the marker
            y: int - vertical position of the marker
            image_scale: float - current scale of the loaded image.

        Return:
            No return in the method
        '''

        shape = Shapes.calculate_shape(qualifier, x, y, size, image_scale, redraw)

        if qualifier == 1:
            self.canvas.create_polygon(shape[0],
                                       shape[1],
                                       shape[2],
                                       shape[3],
                                       shape[4],
                                       shape[5],
                                       tags=mode,
                                       fill=color)

        elif qualifier == 2:
            self.canvas.create_oval(shape[0],
                                    shape[1],
                                    shape[2],
                                    shape[3],
                                    width=0,
                                    tags=mode,
                                    fill=color)

        elif qualifier == 3:
            self.canvas.create_rectangle(shape[0],
                                         shape[1],
                                         shape[2],
                                         shape[3],
                                         width=0,
                                         tags=mode,
                                         fill=color)

        elif qualifier == 4:
            self.canvas.create_line(shape[0],
                                    shape[1],
                                    shape[2],
                                    shape[3],
                                    width=[4],
                                    tags=mode,
                                    fill=color)

    def clear_all_markers_from_canvas(self):
        '''
        Method removes all markers form canvas, but also removes all other elements from canvas.
        This is due to 'all' argument in canvas.delete() method.

        Return:
             No return in the method
        '''

        markers_to_delete = self.canvas.find_all()

        for element in markers_to_delete:
            # Checks for all valid marker tags.
            if self.canvas.gettags(element)[0] in self.valid_marker_tags:
                self.canvas.delete(element)

        self.statistics.clear_all()
        self.texts.update_statistic_texts()
        self.samples.placed_markers = []

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
        if self.image_object:
            scrolled = int(event.delta / 60)

            if scrolled < 0:
                self.image_scale /= abs(scrolled)

                if self.image_scale < 0.5:
                    self.image_scale = 0.5
                else:
                    self.scale_image(event.x, event.y)

            elif scrolled > 0:
                self.image_scale *= abs(scrolled)

                if self.image_scale > 4:
                    self.image_scale = 4
                else:
                    self.scale_image(event.x, event.y)

    def scale_image(self, x, y):
        '''
        Scales the loaded image according to given scale.
        Removes all placed markers, recalculates positioning and redraws markers.

        Args:
            x: int - x coordinates of the scaling
            y: int - y coordinates of the scaling

        Return:
            No return in the method
        '''

        self.canvas.delete('all')

        new_size = int(self.image_object_width * self.image_scale), int(self.image_object_height * self.image_scale)
        self.resized_raw_image_object = self.raw_image_object.resize(new_size)

        self.resized_image_object = ImageTk.PhotoImage(self.resized_raw_image_object)
        self.resized_image_object_width = self.resized_image_object.width()
        self.resized_image_object_height = self.resized_image_object.height()

        self.canvas.create_image(
            self.resized_image_object_width / 2,
            self.resized_image_object_height / 2,
            tags='resized_image',
            image=self.resized_image_object)

        self.canvas.config(
            scrollregion=(
                0,
                0,
                self.resized_image_object_width,
                self.resized_image_object_height))

        self.redraw_all_markers()
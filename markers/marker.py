#!/usr/bin/env python3


class Marker:

    def __init__(self, canvas_index, size, mode, qualifier, position_x, position_y):
        '''
        Container for all information corresponding to a single marker.

        Args:
            canvas_index: int - number of the marker on the canvas, corresponds
                to the order of placing all elements in the canvas.
            size: int - contains the current size of the marker specified.
            mode: int - mode of the marker activated.
                integer in range 1-8
            qualifier: int - qualifier of the marker activated.
                integer in range 1-4
            position_x: int - horizontal position of the marker.
            position_y: int - vertical position of the marker.
        '''

        self.canvas_index = canvas_index
        self.size = size
        self.mode = mode
        self.qualifier = qualifier
        self.position_x = position_x
        self.position_y = position_y

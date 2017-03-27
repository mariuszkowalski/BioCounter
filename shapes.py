#!/usr/bin/env python3


class Shapes:

    @staticmethod
    def calculate_shape(qualifier, position_x, position_y, size):
        '''
        Calculate position of vertexes of defined marker shapes.

        Args:
            qualifier: int - activated qualifier, defines shape .
            position_x: int - position x of the left mouse button event.
            position_y: int - position y of the left mouse button event.
            size: int - defined size of the marker in pixels.

        Return:
            list: contains coordinates for each vertex of given shape.
        '''

        shape = []

        if qualifier == 1:
            #Triangle.
            shape = [
                position_x - size - 1,
                position_y + size,
                position_x + size,
                position_y + size,
                position_x,
                position_y - size
            ]

        elif qualifier == 2:
            #Oval.
            shape = [
                position_x - size,
                position_y - size,
                position_x + size,
                position_y + size
            ]

        elif qualifier == 3:
            #Rectangle.
            shape = [
                position_x - size,
                position_y - size,
                position_x + size,
                position_y + size
            ]

        elif qualifier == 4:
            #Line.
            shape = [
                position_x + size,
                position_y - size,
                position_x - size,
                position_y + size,
                size
            ]

        return shape
#!/usr/bin/env python3


class Shapes:

    @staticmethod
    def calculate_shape(qualifier, position_x, position_y, size, image_scale):
        '''
        Calculate position of vertexes of defined marker shapes.

        Args:
            qualifier: int - activated qualifier, defines shape.
            position_x: int - position x of the left mouse button event.
            position_y: int - position y of the left mouse button event.
            size: int - defined size of the marker in pixels.
            image_scale: float - current scale of the loaded image.

        Return:
            list: contains coordinates for each vertex of given shape.
        '''

        position_x *= image_scale
        position_y *= image_scale

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

    @staticmethod
    def calculate_scale_factor(old_scale, scale):
        if old_scale:
            if scale > old_scale:
                return 2.0
            else:
                return 0.5
        else:
            return 1.0

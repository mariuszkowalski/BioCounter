#!/usr/bin/env python3


class MarkerUtilities:
    '''
    Static method required for markers zoom operations.
    '''

    @staticmethod
    def adjust_recorded_position(position_x, position_y, scale):
        '''
        Takes relative position of the marker placed in canvas which corresponds to
        the set image scale and calculates absolute position of the marker.

        Args:
            position_x: float - relative position x of the marker in the canvas.
            position_y: float - relative position y of the marker in the canvas.
            scale: float - set scale of the image.

        Return:
            position_x: float - absolute position x of the marker.
            position_y: float - absolute position y of the marker.
        '''

        if scale != 1.0:
            position_x /= scale
            position_y /= scale

        return position_x, position_y

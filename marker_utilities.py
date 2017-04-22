#!/usr/bin/env python3


class MarkerUtilities:

    @staticmethod
    def adjust_recorded_position(position_x, position_y, scale):
        if scale > 1.0:
            position_x /= scale
            position_y /= scale
        elif scale < 1.0:
            position_x /= scale
            position_y /= scale

        return position_x, position_y

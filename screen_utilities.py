#!/usr/bin/env python3


class ScreenUtilities:
    '''
    Helps manage the proper resolution of the main window of the application.
    '''

    @staticmethod
    def check_resolution(screen_width, screen_height):
        '''
        Checks resolution of the screen and detects if there is a multiple screen setup in use.

        Args:
             screen_width: int - width of the set screen
             screen_height: int - height of the set screen

        Return:
            screen_width: int - corrected width of the screen set for one monitor
            screen_height: int - corrected height of the screen set for the one monitor
        '''
        ratio = '{0:.2f}'.format(screen_width / screen_height)

        if screen_height == 1080 and screen_width > 1920 and ratio > 1.78:
            if screen_height > 1080:
                screen_height = 1080
            if screen_width > 1920:
                screen_width = 1920
        elif screen_height == 768 and screen_width > 1366 and ratio > 1.78:
            if screen_height > 768:
                screen_height = 768
            if screen_width > 1366:
                screen_width = 1366

        return screen_width, screen_height

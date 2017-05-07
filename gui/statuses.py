#!/usr/bin/env python3


class Statuses:

    def __init__(self, texts, widget_geometries):
        '''
        Contains all the status messages used in the program.

        Args:
            texts: instance - class Texts.
            widget_geometries: instance - class Widget_geometries.
        '''
        self.texts = texts[0]
        self.widget_geometries = widget_geometries[0]

        self.messages = ''

        self.markers_cleared = 'All markers cleared.'
        self.markers_size_changed = 'Markers size changed to:'

    def show_markers_size_change_message(self):
        '''
        Formats text to contain current market size value.

        Return:
             string - formatted text containing current marker size.
        '''

        return '{} {}.'.format(self.markers_size_changed, self.widget_geometries.marker_size)

    def clear_status_bar_text(self):
        '''
        Clears the text shown in the status bar.
        '''

        self.texts.status_bar_text.set('')
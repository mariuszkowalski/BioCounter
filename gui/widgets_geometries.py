#!/usr/bin/env python3


class Widget_geometries:

    def __init__(self, settings):
        '''
        Class container for the all dimensions of all elements used in the GUI.

        Args:
            settings: instance - class Settings.
        '''

        self.settings = settings

        self.marker_size = 10
        self.min_marker_size = 4
        self.max_marker_size = 20

        self.toolbar_width = 250
        self.scrollbar_thickness = 18
        self.main_frame_width = self.settings.adjusted_screen_width
        self.main_frame_height = self.settings.adjusted_screen_height - 20

        self.picture_frame_width = self.main_frame_width - self.toolbar_width
        self.picture_frame_height = self.main_frame_height
        self.canvas_frame_width = self.picture_frame_width - self.scrollbar_thickness
        self.canvas_frame_height = self.picture_frame_height - self.scrollbar_thickness
        self.notebook_width = self.toolbar_width - 5
        self.notebook_height = self.main_frame_height - 44

        self.sample_frame_width = self.notebook_width
        self.sample_frame_height = 53

        self.clear_all_markers_frame_width = self.notebook_width
        self.clear_all_markers_frame_height = 30

        # Option tab
        self.qualifiers_options_frame_width = 245 - 10
        self.qualifiers_options_frame_height = 265

        self.markers_options_frame_width = 245 - 10
        self.markers_options_frame_height = 50

        # Statistics tab
        self.qualifier_single_frame_width = self.qualifiers_options_frame_width - 8
        self.qualifier_single_frame_height = 47
        self.qualifier_single_frame_spacing = 48

        self.statistics_column_offset = 40
        self.statistics_sample_row_offset = 3
        self.statistics_percent_row_offset = 27
        self.statistics_label_x = 7
        self.statistics_percent_label_y = 30
        self.statistics_label_y = 6

        # About window
        self.about_window_width = 255
        self.about_window_height = 150
        self.about_window_x = int(self.settings.adjusted_screen_width / 2 - self.about_window_width / 2)
        self.about_window_y = int(self.settings.adjusted_screen_height / 2 - self.about_window_height / 2)

        # Jpg export window
        self.jpg_export_window_width = 260
        self.jpg_export_window_height = 120
        self.jpg_export_window_x = int(self.settings.adjusted_screen_width / 2 - self.jpg_export_window_width / 2)
        self.jpg_export_window_y = int(self.settings.adjusted_screen_height / 2 - self.jpg_export_window_height / 2)

        # Png export window
        self.png_export_window_width = 260
        self.png_export_window_height = 150
        self.png_export_window_x = int(self.settings.adjusted_screen_width / 2 - self.jpg_export_window_width / 2)
        self.png_export_window_y = int(self.settings.adjusted_screen_height / 2 - self.jpg_export_window_height / 2)
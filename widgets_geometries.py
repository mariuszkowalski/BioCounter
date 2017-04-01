#!/usr/bin/env python3


class Widget_geometries:

    def __init__(self, settings):
        self.settings = settings

        self.marker_size = 10

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

        self.qualifiers_options_frame_width = 245 - 10
        self.qualifiers_options_frame_height = 265
        self.qualifier_single_frame_width = self.qualifiers_options_frame_width - 8
        self.qualifier_single_frame_height = 47
        self.qualifier_single_frame_spacing = 48

        self.statistics_column_offset = 40
        self.statistics_sample_row_offset = 3
        self.statistics_label_x = 7
        self.statistics_label_y = 6
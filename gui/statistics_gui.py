#!/usr/bin/env python3


from tkinter import *
from tkinter import ttk


class Statistics_gui:

    def __init__(self, statistics_tab, widget_geometries, samples, **kwargs):
        self.statistics_tab = statistics_tab
        self.widget_geometries = widget_geometries[0]
        self.samples = samples[0]
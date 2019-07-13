# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 13:47:09 2019

@author: Filippos
"""

from PyQt5.QtWidgets import QSizePolicy

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

import random

class PlotCanvas(FigureCanvas):

    def __init__(self, parent = None, width = 6, height = 4, dpi=100):
        
        fig = Figure(figsize=(width, height), dpi = dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot()


    def plot(self):
        
        #test plot
        
        data = [random.random() for i in range(25)]
        ax = self.figure.add_subplot(111)
        ax.plot(data, 'r-')
        ax.set_title('PyQt Matplotlib Example')
        self.draw()
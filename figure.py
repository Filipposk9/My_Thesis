# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 14:21:34 2019

@author: Filippos
"""

from PyQt5.QtWidgets import QDialog
from model.plotcanvas import PlotCanvas

class Figure(QDialog):

    def __init__(self):
        
        super().__init__()
        self.left = 100
        self.top = 100
        self.title = 'PyQt5 matplotlib example'
        self.width = 600
        self.height = 400
        self.initUI()

    def initUI(self):
        
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        m = PlotCanvas(self, width = 6, height = 4)
        m.move(0, 0)

        self.show()  
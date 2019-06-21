# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 19:44:57 2019

@author: Filippos

"""

import sys
from gui.mainwindow import MainWindow
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__' : 
        
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    app.exec()
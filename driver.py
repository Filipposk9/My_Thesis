# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 19:44:57 2019

One program to rule them all, 
One program to find them;
One program to bring them all, 
and in python bind them.

@author: Filipposk9
"""

import sys
from view.mainwindow import MainWindow
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__': 
        
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec())
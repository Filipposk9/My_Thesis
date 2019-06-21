# -*- coding: utf-8 -*-
"""

This program creates the main window GUI for a statistics application.

Author: Filippos Kozanitis
Last edited: June 2019

"""

from PyQt5.QtWidgets import QMainWindow
from gui.menus import Menus
from gui.table import Table

class MainWindow(QMainWindow) :
    
    def __init__(self) :
        
        super().__init__()
        
        self.initUI()
    
    def initUI(self) : 
        
        #initialize main window components and parameters
        
        self.setWindowTitle("DeStat")
        self.showMaximized()
        Menus.initMenus(self)
        Table.createTable(self)
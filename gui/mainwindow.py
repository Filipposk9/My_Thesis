# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 19:34:57 2019

This program creates the main window GUI for a statistics application.

@author: Filipposk9
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
        Table.initTable(self)
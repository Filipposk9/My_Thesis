# -*- coding: utf-8 -*-
"""

This program creates the main window GUI for a statistics application.

Author: Filippos Kozanitis
Last edited: June 2019

"""

from PyQt5.QtWidgets import QMainWindow, QTableWidget
from gui.menus import Menus

class MainWindow(QMainWindow) :
    
    def __init__(self) :
        
        super().__init__()
        
        self.initUI()
    
    def initUI(self) : 
        
        #initialize main window components and parameters
        
        self.setWindowTitle("DeStat")
        self.showMaximized()
        Menus.initMenus(self)
        self.createTable()
        
    def createTable(self) : 
        
        #initializes table and its cells and sets it as the central widget of the app
        
        mainTable = QTableWidget(self)
        mainTable.setColumnCount(24)
        mainTable.setRowCount(24)
        self.setCentralWidget(mainTable)
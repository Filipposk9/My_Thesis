# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 16:52:35 2019

@author: Filippos
"""

from PyQt5.QtWidgets import QMainWindow, QTableWidget

class Table(QMainWindow) :
     
    def createTable(mainWindow) : 
        
        #initializes table and its cells and sets it as the central widget of the app
        
        mainTable = QTableWidget(mainWindow)
        mainTable.setColumnCount(24)
        mainTable.setRowCount(24)
        mainWindow.setCentralWidget(mainTable)
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 16:52:35 2019

This program creates the table used in the application's main window.
The table is made is to look like a spreadsheet in order to view and edit 
statistical data.

@author: Filipposk9
"""

from PyQt5.QtWidgets import QMainWindow, QTableView
from model.pandasmodel import PandasModel
import pandas as pd

class Table(QMainWindow):
    
    def initTable(mainWindow): 
        
        #initializes table and its cells and sets it as the central widget of the app
        
        global mainTable
        
        mainTable = QTableView(mainWindow)
        mainWindow.setCentralWidget(mainTable)        
        
        df = pd.DataFrame(data = [[0] * 24] * 24)
        model = PandasModel(df)
        mainTable.setModel(model)
        
    def changeTableContents(fileName): 
        
        if fileName[1] == 'csv(*.csv)':
            mainTable.setModel(PandasModel(pd.read_csv(fileName[0])))
        elif fileName[1] == 'excel(*.xls)':
            mainTable.setModel(PandasModel(pd.read_excel(fileName[0])))
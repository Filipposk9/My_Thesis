# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 16:52:35 2019

This program creates the table used in the application's main window.
The table is made is to look like a spreadsheet in order to view and edit 
statistical data.

@author: Filipposk9
"""

from PyQt5.QtWidgets import QMainWindow, QTableView
#from PyQt5 import QtWidgets
from model.pandasmodel import PandasModel
import pandas as pd

class Table(QMainWindow) :
     
    def initTable(mainWindow) : 
        
        #initializes table and its cells and sets it as the central widget of the app
        
        mainTable = QTableView(mainWindow)
        mainWindow.setCentralWidget(mainTable)        

        #fileName = 'C:/Users/Filippos/Downloads/FL_insurance_sample.csv'
        #mainTable.pathLE = QtWidgets.QLineEdit(mainTable)
        #mainTable.pathLE.setText(fileName)
        #df = pd.read_csv(fileName)
        d = {'1': list(range(1, 24)), '2': list(range(1, 24))}
        df = pd.DataFrame(data = d)
        model = PandasModel(df)
        mainTable.setModel(model)
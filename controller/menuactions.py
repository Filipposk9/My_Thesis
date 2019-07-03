# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 15:29:02 2019

@author: Filippos
"""

from PyQt5.QtWidgets import QFileDialog
from view.table import Table

class MenuActions : 
    
    def showOpenFileDialog(self) :
        
        filter = "csv(*.csv);;excel(*.xls)"
        fileName = QFileDialog.getOpenFileName(None, "Open File", None, filter)
        #fileName[0] = path, fileName[1] = fileType
        Table.changeTableContents(fileName[0])
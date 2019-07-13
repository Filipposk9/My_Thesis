# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 15:29:02 2019

@author: Filippos
"""


from PyQt5.QtWidgets import QFileDialog
from view.table import Table
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt
from figure import Figure

class MenuActions: 
    
    def showNewFileDialog():
        #
        return None
    
    def showOpenFileDialog():
        
        filter = "csv(*.csv);;excel(*.xls)"
        fileName = QFileDialog.getOpenFileName(None, "Open File", None, filter)
        Table.changeTableContents(fileName)
        
    def createBarDiagram(): 
        
        dialog = Figure()
        dialog.exec_()
        dialog.show()
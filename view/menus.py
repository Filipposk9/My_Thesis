# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 16:25:21 2019

This program creates the menus used in the application's main window.

@author: Filipposk9
"""

from PyQt5.QtWidgets import QMainWindow, QAction
from controller.menuactions import MenuActions

class Menus (QMainWindow):
     
    def initMenus(mainWindow):
        
        #initialize menus, submenus and actions
        
        menubar = mainWindow.menuBar()
        
        #menubar items
        
        fileMenu = menubar.addMenu('&File')
        editMenu = menubar.addMenu('&Edit')
        viewMenu = menubar.addMenu('&View')
        dataMenu = menubar.addMenu('&Data')
        transformMenu = menubar.addMenu('&Transform')
        analyzeMenu = menubar.addMenu('&Analyze')
        graphsMenu = menubar.addMenu('&Graphs')
        utilitiesMenu = menubar.addMenu('&Utilities')
        windowsMenu = menubar.addMenu('&Windows')
        helpMenu = menubar.addMenu('&Help')
        
        #fileMenu Actions
        
        newAct = QAction('New', mainWindow)
        newAct.setShortcut('Ctrl+N')
        openAct = QAction('Open', mainWindow)
        openAct.setShortcut('Ctrl+O')
        openAct.triggered.connect(MenuActions.showOpenFileDialog)
        saveAct = QAction('Save', mainWindow)
        saveAct.setShortcut('Ctrl+S')
        saveAsAct = QAction('Save As', mainWindow)
        saveAsAct.setShortcut('Ctrl+Shift+S')
        exitAct = QAction('Exit', mainWindow)
        exitAct.setShortcut('Ctrl+W')
        
        #graphsMenu Actions
        
        barChartAct = QAction('Bar Chart', mainWindow)
        barChartAct.triggered.connect(MenuActions.createBarDiagram)
        
        #add actions to menus
        
        fileMenu.addAction(newAct)
        fileMenu.addAction(openAct)
        fileMenu.addAction(saveAct)
        fileMenu.addAction(saveAsAct)
        fileMenu.addAction(exitAct)
        
        graphsMenu.addAction(barChartAct)
from PyQt5 import QtGui, QtCore, QtWidgets
import pyqtgraph as pg
from tree import Window
import numpy as np
import PyQt5
import pyqtgraph as pg

from plotwindow import PlotWindow as pw


import pyqtgraph.multiprocess as mp



class App():

    def __init__(self):
        self.app = QtGui.QApplication([])

        self.w = QtGui.QWidget()
        self.w.resize(500,400)
        self.app.setWindowIcon(QtGui.QIcon('uj.ico'))



        btn1 = QtGui.QPushButton('Open Windows')
        btn2 = QtGui.QPushButton('Start')
        btn3 = QtGui.QPushButton('Pause')
        lw = QtGui.QListWidget()




        layout = QtGui.QGridLayout()
        layout.addWidget(btn1, 0, 2)  # button goes in upper-left
        layout.addWidget(btn2, 1, 2)  # text edit goes in middle-left
        layout.addWidget(btn3, 2, 2)  # list widget goes in bottom-left
        layout.addWidget(lw, 3, 2)  # list widget goes in bottom-left

        self.tree = Window()
        layout.addWidget(self.tree, 0, 0, 4, 2)  # plot goes on right side, spanning 3 rows

        self.w.setLayout(layout)
        self.w.setWindowTitle("Urban Journey 2")


    def Start(self):
        self.w.show()
        self.app.exec_()


    def Update(self, data):

        1+1


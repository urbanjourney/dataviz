from PyQt5 import QtGui, QtCore, QtWidgets
import pyqtgraph as pg
from tree import Window
import numpy as np
import PyQt5
import pyqtgraph as pg




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



        proc = mp.QtProcess()
        rpg = proc._import('pyqtgraph')

        plotwin = rpg.plot(title="test")
        plotwin2 = rpg.plot(tiltle="test2")
        self.curve1 = plotwin.plot(pen='y')
        self.curve1.setPen('b')
        self.curve2 = plotwin.plot(pen='y')
        self.curve2.setPen('g')
        self.curve3 = plotwin.plot(pen='y')
        self.curve2.setPen('r')

        self.curve4 = plotwin2.plot(pen='y')
        self.curve4.setPen('b')
        self.curve5 = plotwin2.plot(pen='y')
        self.curve5.setPen('g')
        self.curve6 = plotwin2.plot(pen='y')
        self.curve6.setPen('r')











    def Start(self):
        self.w.show()
        self.app.exec_()


    def Update(self, data):

        self.curve1.setData(y=data, _callSync='async')
        self.curve2.setData(y=data*1.1+0.6, _callSync='async')
        self.curve3.setData(y=data+0.2, _callSync='async')

        self.curve4.setData(y=data*-1, _callSync='async')
        self.curve5.setData(y=data * -1.1 + 0.6, _callSync='async')
        self.curve6.setData(y=data *-1 + 0.2, _callSync='async')


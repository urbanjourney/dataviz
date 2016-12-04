from PyQt5 import QtGui
from urban_journey import NodeBase, QWidgetNodeBase, String
from .tree import Window
from urban_journey import Output, activity, Float, Clock, ModuleNodeBase, Eval, Input
import numpy as np
import time


import pyqtgraph as pg
import pyqtgraph.widgets.RemoteGraphicsView
from random import random
import sys

enable = False

class graphtree(QWidgetNodeBase):
    inp = Input()

    c = String(optional_value="-")

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.subscribe()
        self.resize(800, 400)
        self.setWindowIcon(QtGui.QIcon('uj.ico'))
        self.btn1 = QtGui.QPushButton('Open Windows')
        self.btn2 = QtGui.QPushButton('Start')
        self.btn3 = QtGui.QPushButton('Pause')
        self.lw = QtGui.QListWidget()
        self.layout = QtGui.QGridLayout()
        self.layout.addWidget(self.btn1, 0, 2)  # button goes in upper-right
        self.layout.addWidget(self.btn2, 1, 2)  # text edit goes in middle-right
        self.layout.addWidget(self.btn3, 2, 2)  # list widget goes in bottom-right
        self.layout.addWidget(self.lw, 3, 2)  # list widget goes in bottom-right
        self.tree = Window()
        self.layout.addWidget(self.tree, 0, 0, 4, 2)  # plot goes on left side, spanning 3 rows
        self.setLayout(self.layout)
        self.setWindowTitle("Urban Journey 2")
        self.update_children()

        self.btn2.clicked.connect(self.handleBtn2)
        self.btn3.clicked.connect(self.startstuff)

    def handleBtn2(self):
        self.tree.treeWidget.itemChanged.connect(self.tree.handleChanged)

    def add2DWindow(self):

        print("its working")

    def startstuff(self):
        global enable
        enable = True

sys._excepthook = sys.excepthook

def my_exception_hook(exctype, value, traceback):
    # Print the error and traceback
    print(exctype, value, traceback)
    # Call the normal Exception hook after
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)

# Set the exception hook to our wrapping function
sys.excepthook = my_exception_hook

class graphwindow(NodeBase):
    name = String(optional_value="givemeanameplease")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        tree = self.element.getparent().node.tree
        self.windowtest = tree.addWindow(tree.treeWidget.invisibleRootItem(), tree.column, self.name, [0,0,0,0])
        self.update_children()

class graph(NodeBase):
    name = String(optional_value="givemeanameplease")
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        tree = self.element.getparent().getparent().node.tree
        parent = self.element.getparent().node
        self.graphtest = tree.addGraph(parent.windowtest, tree.column, self.name, [1, 0, 0, 0])
        self.update_children()





class curve(ModuleNodeBase):
    name = String(optional_value="givemeanameplease")

    yaxis = Input()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        parent = self.element.getparent().node
        self.tree = self.element.getparent().getparent().getparent().node.tree
        self.curve = self.tree.addPlot(parent.graphtest, self.tree.column, self.name, [2, 0, 0, 0])

        self.subscribe()

        self.test = np.zeros(100)
        self.time = np.zeros(100)

        print("test")

    @activity(yaxis)
    async def updatecurve(self, yaxis):
        self.test = np.roll(self.test,-1)
        self.test[99] = yaxis
        self.time = np.roll(self.time, -1)
        self.time[99] = time.time()

        global enable
        if enable == True:
            self.tree.updateCurve(self.curve,0, self.time, self.test)



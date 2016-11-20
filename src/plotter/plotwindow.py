
from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
import pyqtgraph.widgets.RemoteGraphicsView
import numpy as np

from random import random


class PlotWindow():
    def __init__(self):

        pg.setConfigOptions(antialias=True)  ## this will be expensive for the local plot

        self.layout = pg.LayoutWidget()
        self.layout.resize(800, 800)

        ## Create a PlotItem in the remote process that will be displayed locally

    def addGraph(self,index):
        self.__dict__['view'+str(index)] = pg.widgets.RemoteGraphicsView.RemoteGraphicsView()
        self.__dict__['PlotItem'+str(index)] = self.__dict__['view'+str(index)].pg.PlotItem()
        self.__dict__['PlotItem'+str(index)]._setProxyOptions(deferGetattr=True)  ## speeds up access to rplt.plot
        self.__dict__['view'+str(index)].setCentralItem(self.__dict__['PlotItem'+str(index)])
        self.layout.addWidget(self.__dict__['view'+str(index)], row=index+2, col=0, colspan=3)


    def closeGraph(self,index):
        self.__dict__['view' + str(index)].hide()


    def addCurve(self, parentGraph, index):
        self.__dict__['g'+str(parentGraph)+'c'+str(index)] = self.__dict__['PlotItem' + str(parentGraph)].plot()
        self.__dict__['g' + str(parentGraph) + 'c' + str(index)].setData([random(), random()])

    def test(self):
        return 1

    def Show(self):
        self.layout.show()

    def Hide(self):
        self.layout.hide()






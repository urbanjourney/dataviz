from PyQt5 import QtCore, QtGui

from .plotwindow import PlotWindow


class Window(QtGui.QWidget):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.treeWidget = QtGui.QTreeWidget()
        self.treeWidget.setHeaderHidden(True)
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.treeWidget)
        self.setLayout(layout)
        self.column = 0


    def addWindow(self, parent, column, title, data):

        item = QtGui.QTreeWidgetItem(parent, [title])
        item.setChildIndicatorPolicy(QtGui.QTreeWidgetItem.ShowIndicator)
        item.setExpanded (True)
        item.setCheckState(column, QtCore.Qt.Unchecked)
        item.setData(column, QtCore.Qt.UserRole, data)
        return item

    def openWindow(self, index):
        self.__dict__['newwindow'+str(index)] = PlotWindow()
        self.__dict__['newwindow'+str(index)].Show()

    def closeWindow(self, index):
        self.__dict__['newwindow'+str(index)].Hide()

    def addGraph(self, parent, column, title, data):
        item = QtGui.QTreeWidgetItem(parent, [title])
        item.setData(column, QtCore.Qt.UserRole, data)
        item.setChildIndicatorPolicy(QtGui.QTreeWidgetItem.DontShowIndicatorWhenChildless)
        item.setCheckState(column, QtCore.Qt.Unchecked)
        item.setExpanded (True)
        return item

    def removeGraph(self):
        1 + 1

    def addPlot(self, parent, column, title, data):
        item = QtGui.QTreeWidgetItem(parent, [title])
        item.setData(column, QtCore.Qt.UserRole, data)
        item.setChildIndicatorPolicy(QtGui.QTreeWidgetItem.DontShowIndicator)
        item.setCheckState (column, QtCore.Qt.Unchecked)
        return item

    def removePlot(self):
        1 + 1

    def handleChanged(self, item, column):
        if item.checkState(column) == QtCore.Qt.Checked:
            if item.data(self.column,QtCore.Qt.UserRole)[0] == 0:
                self.openWindow(item.data(self.column, QtCore.Qt.UserRole)[1])

            if item.data(self.column, QtCore.Qt.UserRole)[0] == 1:
                self.__dict__['newwindow'+str(item.data(self.column, QtCore.Qt.UserRole)[2])].addGraph(item.data(self.column,QtCore.Qt.UserRole)[1])

            if item.data(self.column, QtCore.Qt.UserRole)[0] == 2:
                self.__dict__['newwindow' + str(item.data(self.column, QtCore.Qt.UserRole)[2])].addCurve(item.data(self.column, QtCore.Qt.UserRole)[3],item.data(self.column, QtCore.Qt.UserRole)[1])

            print ("checked", item, item.text(column))
        if item.checkState(column) == QtCore.Qt.Unchecked:

            if item.data(self.column,QtCore.Qt.UserRole)[0] == 0:
                self.closeWindow(item.data(self.column, QtCore.Qt.UserRole)[1])

            if item.data(self.column, QtCore.Qt.UserRole)[0] == 1:
                self.__dict__['newwindow'+str(item.data(self.column, QtCore.Qt.UserRole)[2])].closeGraph(item.data(self.column,QtCore.Qt.UserRole)[1])

            print ("unchecked", item, item.text(column))

    def updateCurve(self, item, column, data, xaxis=None):
        if xaxis is None:
            self.__dict__['newwindow' + str(item.data(self.column, QtCore.Qt.UserRole)[2])].updateCurve(item.data(self.column, QtCore.Qt.UserRole)[3], item.data(self.column, QtCore.Qt.UserRole)[1], data)
        else:
            self.__dict__['newwindow' + str(item.data(self.column, QtCore.Qt.UserRole)[2])].updateCurve(item.data(self.column, QtCore.Qt.UserRole)[3], item.data(self.column, QtCore.Qt.UserRole)[1], data, xaxis)
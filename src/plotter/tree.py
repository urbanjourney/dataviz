import sys
from PyQt5 import QtCore, QtGui


class Window(QtGui.QWidget):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.treeWidget = QtGui.QTreeWidget()
        self.treeWidget.setHeaderHidden(True)
        self.addItems(self.treeWidget.invisibleRootItem())
        self.treeWidget.itemChanged.connect (self.handleChanged)
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.treeWidget)
        self.setLayout(layout)

    def addItems(self, parent):
        column = 0
        sensors = self.addParent(parent, column, 'Window sensors', 'data')
        accel = self.addParent(sensors, column, 'Graph accelerometer', 'data')
        gyr = self.addParent(sensors, column, 'Graph gyroscope', 'data')
        mag = self.addParent(sensors, column, 'Graph magnetometer', 'data')

        self.addChild(accel, column, 'Curve X', 'data Type A')
        self.addChild(accel, column, 'Curve Y', 'data Type B')
        self.addChild(accel, column, 'Curve Z', 'data Type B')

        self.addChild(gyr, column, 'Curve ', 'data Type A')
        self.addChild(gyr, column, 'Curve Y', 'data Type B')
        self.addChild(gyr, column, 'Curve Z', 'data Type B')

        self.addChild(mag, column, 'Curve X', 'data Type A')
        self.addChild(mag, column, 'Curve Y', 'data Type B')
        self.addChild(mag, column, 'Curve Z', 'data Type B')
        self.addChild(mag, column, 'Curve N', 'data Type A')

        states = self.addParent(parent, column, 'Sensors', 'data')

        pins = self.addParent(states, column, 'Graph pin states', 'data')
        self.addChild(pins, column, 'RBF', 'data')
        self.addChild(pins, column, 'BW', 'data')

        logger = self.addParent(states, column, 'Graph Logger', 'data')
        self.addChild(logger, column, 'Curve write speed', 'data ')




    def addParent(self, parent, column, title, data):
        item = QtGui.QTreeWidgetItem(parent, [title])
        item.setData(column, QtCore.Qt.UserRole, data)
        item.setChildIndicatorPolicy(QtGui.QTreeWidgetItem.ShowIndicator)
        item.setExpanded (True)
        return item

    def addChild(self, parent, column, title, data):
        item = QtGui.QTreeWidgetItem(parent, [title])
        item.setData(column, QtCore.Qt.UserRole, data)
        item.setCheckState (column, QtCore.Qt.Unchecked)
        return item

    def handleChanged(self, item, column):
        if item.checkState(column) == QtCore.Qt.Checked:
            print ("checked", item, item.text(column))
        if item.checkState(column) == QtCore.Qt.Unchecked:
            print ("unchecked", item, item.text(column))
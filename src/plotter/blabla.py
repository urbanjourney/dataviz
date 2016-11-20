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

        Window1 = self.addParent(parent, column, 'Window 1', 'data Magneto')
        clients_item = self.addParent(Window1, column, 'Accel', [1,2,4])
        vendors_item = self.addParent(Window1, column, 'Gyro', 'data Gyro')
        time_period_item = self.addParent(Window1, column, 'Magneto', 'data Magneto')

        self.addChild(clients_item, column, 'Accel x', 1)
        self.addChild(clients_item, column, 'Accel y', 2)
        self.addChild(clients_item, column, 'Accel z', 3)

        self.addChild(vendors_item, column, 'Gyro x', 4)
        self.addChild(vendors_item, column, 'Gyro y', 'data adsf')
        self.addChild(vendors_item, column, 'Gyro z', 'adf')
        self.addChild(time_period_item, column, 'Magneto x', 'data Madsffgneto')
        self.addChild(time_period_item, column, 'Magneto y', 'sddsf sdf')
        self.addChild(time_period_item, column, 'Magneto z', 'data sdf')

        Window2 = self.addParent(parent, column, 'Window 2', 'data Magneto')
        states = self.addParent(Window2, column, 'Accel', [1, 2, 4])
        self.addChild(states, column, 'state iets', 'data sdf')
        self.addChild(states, column, 'state 2', 'data sdf')



    def addParent(self, parent, column, title, data):
        item = QtGui.QTreeWidgetItem(parent, [title])
        item.setData(column, QtCore.Qt.UserRole, data)
        item.setChildIndicatorPolicy(QtGui.QTreeWidgetItem.ShowIndicator)
        item.setExpanded(True)
        return item

    def addChild(self, parent, column, title, data):
        item = QtGui.QTreeWidgetItem(parent, [title])
        item.setData(column, QtCore.Qt.UserRole, data)
        item.setCheckState(column, QtCore.Qt.Unchecked)
        return item

    def handleChanged(self, item, column):
        if item.checkState(column) == QtCore.Qt.Checked:
            print("checked", item, item.text(column))
        if item.checkState(column) == QtCore.Qt.Unchecked:
            print("unchecked", item, item.text(column))
from PyQt5 import QtGui
from urban_journey import NodeBase, QWidgetNodeBase, String
from .tree import Window
from urban_journey import Output, activity, Float, Clock, ModuleNodeBase, Eval, Input


class graphtree(QtGui, ModuleNodeBase):
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
        self.layout.addWidget(self.btn1, 0, 2)  # button goes in upper-left
        self.layout.addWidget(self.btn2, 1, 2)  # text edit goes in middle-left
        self.layout.addWidget(self.btn3, 2, 2)  # list widget goes in bottom-left
        self.layout.addWidget(self.lw, 3, 2)  # list widget goes in bottom-left
        self.tree = Window()
        self.layout.addWidget(self.tree, 0, 0, 4, 2)  # plot goes on right side, spanning 3 rows
        self.setLayout(self.layout)
        self.setWindowTitle("Urban Journey 2")
        self.update_children()



    @activity(inp)
    async def handle(self, inp):
        # Write data to output port. This is a coroutine, so don't forget to await.
        1+1

        print(inp)

class graphwindow(NodeBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.update_children()

class graph(NodeBase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.update_children()

class curve(NodeBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

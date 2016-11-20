import numpy as np
from urban_journey import NodeBase, Input, activity
import sys
sys.path.append('./src/plotter')
sys.path.append('./plotter')
import gui


# Create an input port. Inputs ports are triggers and are connected to channels when
# subscribed.






class scope(NodeBase):

    inp = Input()
    app = gui.App()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Minimum signal value.
        self.min = 0
        self.last = None
        self.count = 0
        self.data = np.ones(100)
        self.app.Start()



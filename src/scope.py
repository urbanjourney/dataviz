import numpy as np
from urban_journey import ModuleNodeBase, Input, activity
import sys
sys.path.append('./src/plotter')
sys.path.append('./plotter')
import gui


# Create an input port. Inputs ports are triggers and are connected to channels when
# subscribed.






class scope(ModuleNodeBase):

    inp = Input()
    app = gui.App()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Subscribe all ports to their channels.
        self.subscribe()

        # Minimum signal value.
        self.min = 0
        self.last = None
        self.count = 0
        self.data = np.ones(100)
        self.app.Start()

    # Create an activity to handle the input port. The port data will be passed as a
    # parameter.
    @activity(inp)
    async def handle(self, inp):
        if inp < self.min:
            self.min = inp

        # Rescale signal so it can be plotted on the console.
        signal = int(round((inp-self.min)*10))

        # Create scope line and print it.

        if self.last is None:
            pass
        else:

            if self.count < 99:
                self.count += 1
            else:
                self.count = 0

            self.data[self.count] = inp
            self.app.Update(self.data)

        self.last = signal

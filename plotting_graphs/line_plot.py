import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

class LinePlot():
    def __init__(self, no_repeat=False, interval=20, frequency=2, amplitude=1, colour="blue"):
        self.fig, self.ax = plt.subplots()
        self.x = np.arange(0, frequency*np.pi, 0.01)
        self.line, = self.ax.plot(self.x, (np.sin(self.x))/amplitude)
        self.line.set_color(colour)
        self.no_repeat = no_repeat
        self.interval = interval

    def animate(self, i):
        self.line.set_ydata(np.sin(self.x + i / 50))  # update the data.
        return self.line,

    def plot(self):
        if self.no_repeat == False:
            ani = animation.FuncAnimation(
                self.fig, self.animate, frames=320, interval=self.interval, blit=True, save_count=50)
        if self.no_repeat == True:
            pass
        plt.show()
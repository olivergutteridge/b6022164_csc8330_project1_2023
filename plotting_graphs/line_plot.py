import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

class LinePlot():
    def __init__(self, no_repeat=False):
        self.fig, self.ax = plt.subplots()
        self.x = np.arange(0, 2*np.pi, 0.01)
        self.line, = self.ax.plot(self.x, np.sin(self.x))
        self.no_repeat = no_repeat

    def animate(self, i):
        self.line.set_ydata(np.sin(self.x + i / 50))  # update the data.
        return self.line,

    def plot(self):
        if self.no_repeat == False:
            ani = animation.FuncAnimation(
                self.fig, self.animate, frames=320, interval=20, blit=True, save_count=50)
        elif self.no_repeat == True:
            pass
        plt.show()

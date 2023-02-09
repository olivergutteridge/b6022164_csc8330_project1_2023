import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

class LinePlot():
    def __init__(self, no_repeat=False, speed=1, frequency=2, amplitude=1, colour="blue"):
        self.no_repeat = no_repeat
        self.speed = 100 * (1 - (speed / 10)) + (speed / 2)
        self.frequency = frequency
        self.amplitude = amplitude
        self.colour = colour
        self.fig, self.ax = plt.subplots()
        self.x = np.arange(0, self.frequency*np.pi, 0.01)
        self.line, = self.ax.plot(self.x, np.sin(self.x))
        self.line.set_color(self.colour)
        
    def animate(self, i):
        self.line.set_ydata(np.sin(self.x + i / self.speed)*self.amplitude)  # update the data.
        return self.line,

    def plot(self):
        if self.no_repeat == False:
            ani = animation.FuncAnimation(
                self.fig, self.animate, frames=320, interval=20, blit=True, save_count=50)
        if self.no_repeat == True:
            ani = animation.FuncAnimation(
                self.fig, self.animate, frames=320, interval=20, blit=True, save_count=50, repeat=False)
        plt.show()

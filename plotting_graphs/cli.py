from . import line_plot
import numpy as np
import argparse

def cli():
    parser = argparse.ArgumentParser(prog="plotting_graphs", description="a simple program that plots a sine waveform graph")
    parser.add_argument("--no-repeat", help="suppress repeat", action="store_true") 
    parser.add_argument("--speed", help="set wave speed, int: 1->10", default=5, action="store", type=int, choices=range(1, 11), metavar="SPEED")
    parser.add_argument("--frequency", help="set wave frequency, int: 1->10", default=2, action="store", type=int, choices=range(1, 11), metavar="FREQUENCY")
    parser.add_argument("--amplitude", help="set wave amplitude, float: 0.0->1.0", default=1, action="store", type=float, choices=np.arange(0.0, 1.01, 0.01), metavar="AMPLITUDE")
    parser.add_argument("--colour", help="set wave colour, str: colour from matplotlib package", default="blue", action="store", type=str, metavar="COLOUR")
    args = parser.parse_args()

    animation = line_plot.LinePlot(**vars(args))
    animation.plot()

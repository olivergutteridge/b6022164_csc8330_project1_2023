from . import line_plot
import numpy as np
import argparse

def cli():
    parser = argparse.ArgumentParser(prog="plotting_graphs", description="A simple program that plots a Sine waveform graph")
    parser.add_argument("--no-repeat", help="Suppress repeat", action="store_true") 
    parser.add_argument("--interval", help="Set wave interval", default=20, action="store", type=int, choices=range(1, 31), metavar="INTERVAL")
    parser.add_argument("--frequency", help="Set wave frequency", default=2, action="store", type=int, metavar="FREQUENCY")
    parser.add_argument("--amplitude", help="Set wave amplitude", default=1, action="store", type=float, choices=np.arange(0.0,1.01,0.01), metavar="AMPLITUDE")
    parser.add_argument("--colour", help="Set wave colour", default="blue", action="store", type=str, metavar="COLOUR")
    args = parser.parse_args()

    animation = line_plot.LinePlot(**vars(args))
    animation.plot()

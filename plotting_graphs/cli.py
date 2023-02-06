from . import line_plot
import argparse

def cli():
    parser = argparse.ArgumentParser(prog="plotting_graphs", description="a program that plots a waveform graph")
    parser.add_argument("--no-repeat", help="suppress repeat", action="store_true") 
    parser.add_argument("--interval", help="set interval (default 20)", default=20, action="store", type=int, choices=range(1, 31))
    parser.add_argument("--frequency", help="set frequency (default 2)", default=2, action="store", type=int)
    parser.add_argument("--amplitude", help="set amplitude (default 1)", default=1, action="store", type=float)
    parser.add_argument("--colour", help="set the colour of the wave (default blue)", default="blue", action="store", type=str)
    args = parser.parse_args()

    animation = line_plot.LinePlot(**vars(args))
    animation.plot()
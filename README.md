CSC8330: Practical 1
Advanced Programming for Digital Biology

This package is built as a part of the CSC8330: Advanced Programming
for Digital Biology.
Type `python hello_world.py` to see some useful information.

Argument options for plotting_graphs.py

--no-interval : stops the plot from animating - cannot be used with other arguments (default False)
    $ python3.11 plotting_graphs.py --no-repeat

--interval : alter the speed of the animation - integer value in range 1-31, lower value = higher speed (default 20)
    $ python3.11 plotting_graphs.py --interval 10

--frequency : alter the frequency of the animated sine wave - integer value, higher value = higher frequency (default 2)
    $ python3.11 plotting_graphs.py --frequency 50

--amplitude : select the amplitude of the animated sine wave - float value in range 0.0-1.01, higher value = lower amplitude (default 1)
    $ python3.11 plotting_graphs.py --amplitude 0.5

--colour : select a colour for the sine wave - string copatible with matplotlib (3.6.3)
    $ python3.11 plotting_graphs.py --colour green

Code adapted from source material provided by Dr Jichung Li
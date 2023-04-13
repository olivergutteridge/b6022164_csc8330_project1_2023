# CSC8330: Practical 1

# Advanced Programming for Digital Biology

## Getting Started

This package is built as a part of the CSC8330: Advanced Programming
for Digital Biology.   
Plotting Graphs is a simple prgarm that allows the user to visualise and customise a sine waveform.  
Aditional usage information can be found using the command  ```python3.11 plotting_graphs.py --help```.  
Install dependicies using the command ```pip3 install -r requirements.txt```.

## Arguments

| Argument | Description | Default | Example | 
| -------- | ----------- | ------- | ------- |
| --no-repeat | Stop animation from repeating. | False | ```python3.11 plotting_graphs.py --no-repeat``` |
| --speed | Alter the animation speed. | 5 | ```python3.11 plotting_graphs.py --speed 7``` |
| --frequency | Alter the sine wave frequency. | 2 | ```python3.11 plotting_graphs.py --frequency 50``` |
| --amplitude | Alter the sine wave amplitude. | 1 | ```python3.11 plotting_graphs.py --amplitude 0.5``` |
| --colour | Select a colour for the sine wave (matplotlib v3.6.3). | Blue | ```python3.11 plotting_graphs.py --colour green``` |

## Credits

Code adapted from source material provided by Dr Jichung Li.
import pandas as pd
import numpy as np
from math import pi
import random
from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x_vals = []
y_vals = []

x = np.linspace(0, 20, 1000)
frequency = 9
y = np.sin(2*pi*frequency*x)
ind = 0


def animate(i):
    global ind
    x_vals.extend(x[ind:ind + 50])
    y_vals.extend(y[ind:ind + 50])

    ind += 50

    plt.cla()
    plt.plot(x_vals, y_vals, linewidth=2)


a_plot = FuncAnimation(plt.gcf(), animate, interval=1000)
plt.tight_layout()
plt.show()

'''
Questions:
1. Should we continue with simulated sine waves or should we continue with one of the existing data sets?
2. What is the sampling frequency of the EEG hardware that RTx is working on, so if we continue with simulation,
   we can set the same sampling frequency in simulation.
3. 

For next week:
1. Adding Noice to Simulation
2. Multi channel Simulation
3. Commit progress to github
'''



import numpy as np
from matplotlib import pyplot as plt

def map_plot():
    fig = plt.figure()
    fig.set_dpi(100)
    fig.set_size_inches(24, 10)
    ax = plt.axes(xlim=(0, 600), ylim=(0, 250))
    obstacles = []
    for x in range (0,601, 1):
        for y in range(0, 251, 1):
            if  (95 <= x <= 155) and (0 <= y <= 105):
                obstacles.append(tuple((x,y)))
                ax.plot(x,y, color = 'red', marker='o', markersize=5)
            if  (95 <= x <= 155) and (145 <= y <= 250):
                obstacles.append(tuple((x,y)))
                ax.plot(x,y, color = 'red', marker='o', markersize=5)
            if  (y +2*x - 1156) < 0 and (y- 2*x + 906) > 0 and (460 <= x):
                ax.plot(x,y, color = 'red', marker='o', markersize=5)
                obstacles.append(tuple((x,y)))
            if  (y - (15/26)*x - (425/13)) < 0 and (y + (15/26)*x - (4925/13)) < 0 and (y - (15/26)*x + (1675/13)) > 0 and (y + (15/26)*x - (2825/13)) > 0 and (230 <= x <= 370):
                ax.plot(x,y, color = 'red', marker='o', markersize=5)
                obstacles.append(tuple((x,y)))
    plt.show()
    return obstacles
obstacle_space = map_plot()


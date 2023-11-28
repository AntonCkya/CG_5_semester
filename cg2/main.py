import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
from matplotlib.widgets import Button, Slider
import numpy as np

fig = plt.figure(figsize=(5,5))
ax = fig.add_subplot(111, projection='3d')

plt.axis('off')
plt.grid(visible=None)

G_RATIO = (1 + 5**0.5)/2

dots = [
    [-1, 1, 1],                #A 0
    [0, 1/G_RATIO, G_RATIO],   #B 1
    [0, -1/G_RATIO, G_RATIO],  #C 2
    [-1, -1, 1],               #D 3
    [-G_RATIO, 0, 1/G_RATIO],  #E 4
    [1, 1, 1],                 #F 5
    [G_RATIO, 0, 1/G_RATIO],   #G 6
    [1, -1, 1],                #H 7
    [1/G_RATIO, G_RATIO, 0],   #I 8
    [-1/G_RATIO, G_RATIO, 0],  #J 9
    [-1, 1, -1],               #K 10
    [-G_RATIO, 0, -1/G_RATIO], #L 11
    [-1, -1, -1],              #M 12
    [-1/G_RATIO, -G_RATIO, 0], #N 13
    [1/G_RATIO, -G_RATIO, 0],  #O 14
    [1, 1, -1],                #P 15
    [0, 1/G_RATIO, -G_RATIO],  #Q 16
    [G_RATIO, 0, -1/G_RATIO],  #R 17
    [0, -1/G_RATIO, -G_RATIO], #S 18
    [1, -1, -1]                #T 19
]

polygons = [
    (dots[0], dots[4], dots[3], dots[2], dots[1]),
    (dots[0], dots[9], dots[10], dots[11], dots[4]),
    (dots[0], dots[1], dots[5], dots[8], dots[9]),
    (dots[1], dots[2], dots[7], dots[6], dots[5]),
    (dots[2], dots[3], dots[13], dots[14], dots[7]),
    (dots[3], dots[4], dots[11], dots[12], dots[13]),
    (dots[15], dots[17], dots[6], dots[5], dots[8]),
    (dots[15], dots[16], dots[18], dots[19], dots[17]),
    (dots[15], dots[8], dots[9], dots[10], dots[16]),
    (dots[16], dots[10], dots[11], dots[12], dots[18]),
    (dots[18], dots[12], dots[13], dots[14], dots[19]),
    (dots[19], dots[14], dots[7], dots[6], dots[17])
]

ax2 = fig.add_axes([0.25, 0.15, 0.65, 0.03])
slider2 = Slider(
    ax=ax2,
    label='angle   ',
    valmin=0,
    valmax=180,
    valinit=0,
    valstep=0.1
)

def plot_dod(val):
    ax.view_init(0, val)

    for i in polygons:
        x = []
        y = []
        z = []
        for j in i:
            x.append(j[0] + 2.5)
            y.append(j[1] + 2.5)
            z.append(j[2] + 2.5)
        vertices = [list(zip(x,y,z))]
        poly = Poly3DCollection(vertices, facecolors='crimson', alpha=0.9)
        ax.add_collection3d(poly)
        ax.set_xlim(0,5)
        ax.set_ylim(0,5)
        ax.set_zlim(0,5)

    for i in polygons:
        x = []
        y = []
        z = []
        for j in i:
            x.append(j[0] + 2.5)
            y.append(j[1] + 2.5)
            z.append(j[2] + 2.5)
        vertices = [list(zip(x,y,z))]
        line = Line3DCollection(vertices, colors='black', linewidths=1.25)
        ax.add_collection3d(line)
        ax.set_xlim(0,5)
        ax.set_ylim(0,5)
        ax.set_zlim(0,5)

plot_dod(0)

def update(val):
    ax.clear()
    ax.axis('off')
    ax.grid(visible=None)
    plot_dod(val)


slider2.on_changed(update)

plt.show()

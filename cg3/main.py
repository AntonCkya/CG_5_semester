import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
import numpy as np
from matplotlib.widgets import Button, Slider

fig = plt.figure(figsize=(5,5))
ax = fig.add_subplot(111, projection='3d')

plt.axis('off')
plt.grid(visible=None)

c = 10
a = c / 3
aq = 10

ax1 = fig.add_axes([0.25, 0.05, 0.65, 0.03])
slider = Slider(
    ax=ax1,
    label='approximation   ',
    valmin=1,
    valmax=100,
    valinit=aq,
    valstep=1
)

ax2 = fig.add_axes([0.25, 0.15, 0.65, 0.03])
slider2 = Slider(
    ax=ax2,
    label='angle   ',
    valmin=0,
    valmax=180,
    valinit=0,
    valstep=0.1
)

def plot_bochka(val):
    u = np.linspace(0, 2 * np.pi, slider.val)
    v = np.linspace(0, np.pi, slider.val)
    x = a * np.outer(np.cos(u), np.sin(v))
    y = a * np.outer(np.sin(u), np.sin(v))
    z = c * np.outer(np.ones_like(u), np.cos(v))
    for i in range(len(z)):
        for j in range(len(z[i])):
            if z[i][j] > c/1.8:
                z[i][j] = c/1.8
            if z[i][j] < -c/1.8:
                z[i][j] = -c/1.8
    
    angle = np.deg2rad(slider2.val)
    t = np.transpose(np.array([x, y, z]), (1, 2, 0))
    m = [[np.cos(angle), 0, np.sin(angle)], [0, 1, 0], [-np.sin(angle), 0, np.cos(angle)]]
    x,y,z = np.transpose(np.dot(t, m), (2, 0, 1))
    
    ax.plot_surface(x, y, z, cmap='inferno', rcount=slider.val, ccount=slider.val, alpha=0.9)
    ax.set_xlim([-c/1.8, c/1.8])
    ax.set_ylim([-c/1.8, c/1.8])
    ax.set_zlim([-c/1.8, c/1.8])

plot_bochka(aq)

def update(val):
    ax.clear()
    ax.axis('off')
    ax.grid(visible=None)
    plot_bochka(val)

slider.on_changed(update)
slider2.on_changed(update)

plt.show()

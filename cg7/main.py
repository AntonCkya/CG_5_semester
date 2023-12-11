import sys
from math import(
    sin,
    cos,
    pi,
)
from PyQt6.QtWidgets import (
    QApplication,
    QGraphicsScene,
    QGraphicsView,
    QGraphicsTextItem,
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QPen
import numpy as np

WIDTH = int(sys.argv[1])
HEIGHT = int(sys.argv[2])

step = float(sys.argv[3])
show_nums = int(sys.argv[4])

P1i = (int(sys.argv[5]), int(sys.argv[6]))
P2i = (int(sys.argv[7]), int(sys.argv[8]))
P3i = (int(sys.argv[9]), int(sys.argv[10]))
P4i = (int(sys.argv[11]), int(sys.argv[12]))

scalecount = max(P1i[0], P1i[1], P2i[0], P2i[1], P3i[0], P3i[1], P4i[0], P4i[1])

scale = (HEIGHT - 40) // (2 * scalecount + 2)

app = QApplication(sys.argv)

scene = QGraphicsScene(0, 0, WIDTH, HEIGHT)

#Y Axis
scene.addLine(WIDTH // 2, 10, WIDTH // 2, HEIGHT - 10)
scene.addLine(WIDTH // 2, 10, WIDTH // 2 - 5, 20)
scene.addLine(WIDTH // 2, 10, WIDTH // 2 + 5, 20)

y_text = QGraphicsTextItem()
y_text.setPlainText("Y")
y_text.setPos(WIDTH // 2 + 5, 5)
scene.addItem(y_text)

i = HEIGHT // 2 + scale
ci = 1
while i < HEIGHT:
    scene.addLine(WIDTH // 2 - 5, i, WIDTH // 2 + 5, i) 

    if show_nums == 1:
        yd_text = QGraphicsTextItem()
        yd_text.setPlainText("-" + str(ci))
        yd_text.setPos(WIDTH // 2 + 2, i - 10)
        scene.addItem(yd_text)

    i += scale
    ci += 1
i = HEIGHT // 2 - scale
ci = 1
while i > scale:
    scene.addLine(WIDTH // 2 - 5, i, WIDTH // 2 + 5, i)
    
    if show_nums == 1:
        yd_text = QGraphicsTextItem()
        yd_text.setPlainText(str(ci))
        yd_text.setPos(WIDTH // 2 + 2, i - 10)
        scene.addItem(yd_text)

    i -= scale
    ci += 1
#X Axis
scene.addLine(10, HEIGHT // 2, WIDTH - 10, HEIGHT // 2)
scene.addLine(WIDTH - 10, HEIGHT // 2, WIDTH - 20, HEIGHT // 2 - 5)
scene.addLine(WIDTH - 10, HEIGHT // 2, WIDTH - 20, HEIGHT // 2 + 5)

x_text = QGraphicsTextItem()
x_text.setPlainText("X")
x_text.setPos(WIDTH - 25, HEIGHT // 2 + 5)
scene.addItem(x_text)

i = WIDTH // 2 + scale
ci = 1
while i <= WIDTH - 40:
    scene.addLine(i, HEIGHT // 2 - 5, i, HEIGHT // 2 + 5)

    if show_nums == 1:
        xd_text = QGraphicsTextItem()
        xd_text.setPlainText(str(ci))
        xd_text.setPos(i - 10, HEIGHT // 2 + 2)
        scene.addItem(xd_text)

    i += scale
    ci += 1
i = WIDTH // 2 - scale
ci = 1
while i > 0:
    scene.addLine(i, HEIGHT // 2 - 5, i, HEIGHT // 2 + 5)

    if show_nums == 1:
        xd_text = QGraphicsTextItem()
        xd_text.setPlainText("-" + str(ci))
        xd_text.setPos(i - 10, HEIGHT // 2 + 2)
        scene.addItem(xd_text)

    i -= scale
    ci += 1

P1 = (scale * P1i[0] + WIDTH // 2, - scale * P1i[1] + HEIGHT // 2)
P2 = (scale * P2i[0] + WIDTH // 2, - scale * P2i[1] + HEIGHT // 2)
P3 = (scale * P3i[0] + WIDTH // 2, - scale * P3i[1] + HEIGHT // 2)
P4 = (scale * P4i[0] + WIDTH // 2, - scale * P4i[1] + HEIGHT // 2)

scene.addLine(P1[0], P1[1], P2[0], P2[1], pen=QPen(Qt.GlobalColor.blue))
scene.addLine(P2[0], P2[1], P3[0], P3[1], pen=QPen(Qt.GlobalColor.blue))
scene.addLine(P3[0], P3[1], P4[0], P4[1], pen=QPen(Qt.GlobalColor.blue))

t = np.linspace(0, 1, int(step**-1))
x = []
y = []
for i in t:
    xi = (1 - i)**3 * P1[0] + 3*i*(1 - i)**2 * P2[0] + 3*i*i*(1 - i) * P3[0] + i**3 * P4[0]
    yi = (1 - i)**3 * P1[1] + 3*i*(1 - i)**2 * P2[1] + 3*i*i*(1 - i) * P3[1] + i**3 * P4[1]
    x.append(xi)
    y.append(yi)

for i in range(1, len(x)):
    scene.addLine(x[i - 1] , y[i - 1], x[i], y[i], pen=QPen(Qt.GlobalColor.red))

view = QGraphicsView(scene)
view.setWindowTitle("lab1")
view.show()
sys.exit(app.exec())

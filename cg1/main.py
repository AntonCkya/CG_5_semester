"""
Программа выводит график функции p = a * sin(6φ)

Ввод:
python main.py width height a step show_nums
Пример:
python main.py 640 480 10 0.01 1

width x height - размеры окна в пикселях
a - параметр функции (a > 0)
step - шаг для параметра ф (рекомендовано 0.01)
show_nums - флаг на рисование чисел
"""
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
from PyQt6.QtGui import QIcon

WIDTH = int(sys.argv[1])
HEIGHT = int(sys.argv[2])
a = float(sys.argv[3])
step = float(sys.argv[4])
show_nums = int(sys.argv[5])

if a <= 0:
    print("Параметр a должен быть больше 0!")
    exit()

scale = (HEIGHT - 40) // (2 * a + 2)

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

x1 = 0
y1 = 0
x2 = a*sin(6*step)*cos(step)
y2 = a*sin(6*step)*sin(step)
i = 2
while step*i <= 2 * pi:
    scene.addLine(x1 * scale + WIDTH // 2, y1 * scale + HEIGHT // 2, x2 * scale + WIDTH // 2, y2 * scale + HEIGHT // 2)
    x1 = x2
    y1 = y2
    x2 = a*sin(6*step*i)*cos(step*i)
    y2 = a*sin(6*step*i)*sin(step*i)
    i += 1

a_text = QGraphicsTextItem()
a_text.setPlainText("a = " + str(a))
a_text.setPos(20, 20)
scene.addItem(a_text)

view = QGraphicsView(scene)
view.setWindowTitle("lab1")
view.setWindowIcon(QIcon("icon.png"))
view.show()
sys.exit(app.exec())

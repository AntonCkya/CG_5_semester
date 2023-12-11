from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import threading
import time
import math


global xrot
global yrot
global scale

global color_red
global color_green
global color_blue

color_red = 0.0
color_green = 0.0
color_blue = 0.0

def change_color():
    global color_red
    global color_green
    global color_blue
    x = 0.1
    while True:
        color_red = math.sin(x) / 2 * math.pi
        color_green = math.sin(2 * x) / 2 * math.pi
        color_blue = math.sin(3 * x) / 2 * math.pi
        x += 0.1
        time.sleep(0.1)
        glutPostRedisplay()


WIDTH = int(sys.argv[1])
HEIGHT = int(sys.argv[2])
AMBIENT_MODE = int(sys.argv[3])
if AMBIENT_MODE == 1:
    AMBIENT = (1.0, 1.0, 1.0, 1)
elif AMBIENT_MODE == 2:
    AMBIENT = (0.0, 1.0, 0.0, 1)
elif AMBIENT_MODE == 3:
    AMBIENT = (1.0, 0.0, 0.0, 1)
elif AMBIENT_MODE == 4:
    AMBIENT = (0.0, 0.0, 1.0, 1)

AMBIENT_MODEL = GL_LIGHT_MODEL_AMBIENT

FILLING = int(sys.argv[4])

APPROX = int(sys.argv[5])

LIGHT_POS = (1.0, 1.0, 1.0)


def init():
    global xrot
    global yrot
    global scale
    global color_red
    global color_green
    global color_blue
    xrot = 0.0
    yrot = 0.0
    scale = 1

    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)
    glRotatef(-90, 1.0, 0.0, 0.0)
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, AMBIENT)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, LIGHT_POS)


def specialkeys(key, x, y):
    global xrot
    global yrot
    global scale
    if key == GLUT_KEY_UP:
        xrot -= 2.0
    if key == GLUT_KEY_DOWN:
        xrot += 2.0
    if key == GLUT_KEY_LEFT:
        yrot -= 2.0
    if key == GLUT_KEY_RIGHT:
        yrot += 2.0
    if key == GLUT_KEY_PAGE_UP:
        scale += 0.1
    if key == GLUT_KEY_PAGE_DOWN:
        scale -= 0.1

    glutPostRedisplay()


def draw():
    global xrot
    global yrot
    global scale
    global color_red
    global color_green
    global color_blue

    glClear(GL_COLOR_BUFFER_BIT)
    glPushMatrix()
    glRotatef(xrot, 1.0, 0.0, 0.0)
    glRotatef(yrot, 0.0, 1.0, 0.0)
    glLightfv(GL_LIGHT0, GL_POSITION, LIGHT_POS)


    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, (color_red, color_green, color_blue, 1.0))

    glTranslatef(0.0, 0.0, -0.5)
    glScalef(scale, scale, scale)
    if FILLING == 1:
        glutSolidCylinder(0.2, 1, 20, 20)
    elif FILLING == 0:
        glutWireCylinder(0.2, 1, 20, 20)

    glPopMatrix()
    glutSwapBuffers()


glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)

glutInitWindowSize(WIDTH, HEIGHT)

glutInitWindowPosition(200, 200)

glutInit(sys.argv)

glutCreateWindow(b"lab 6")

glutDisplayFunc(draw)

glutSpecialFunc(specialkeys)

init()

t = threading.Thread(target=change_color, daemon=False)
t.start()

glutMainLoop()

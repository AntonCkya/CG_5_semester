from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

global xrot
global yrot
global scale

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

BOCHKA_MODE = int(sys.argv[4])
if BOCHKA_MODE == 1:
    BOCHKA_COLOR = (0.8, 0.0, 0.0, 1.0)
elif BOCHKA_MODE == 2:
    BOCHKA_COLOR = (0.0, 0.8, 0.0, 1.0)
elif BOCHKA_MODE == 3:
    BOCHKA_COLOR = (0.0, 0.0, 0.8, 1.0)
elif BOCHKA_MODE == 4:
    BOCHKA_COLOR = (1.0, 1.0, 1.0, 1.0)

FILLING = int(sys.argv[5])

APPROX = int(sys.argv[6])

LIGHT_POS = (1.0, 1.0, 1.0)


def init():
    global xrot
    global yrot
    global scale 
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

    glClear(GL_COLOR_BUFFER_BIT)
    glPushMatrix()
    glRotatef(xrot, 1.0, 0.0, 0.0)
    glRotatef(yrot, 0.0, 1.0, 0.0)
    glLightfv(GL_LIGHT0, GL_POSITION, LIGHT_POS)

    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, BOCHKA_COLOR)
    glScalef(scale, scale, scale)
    glTranslatef(0.0, 0.0, -0.5)
    if FILLING == 1:
        glutSolidCylinder(0.2, 1, APPROX, APPROX)
    elif FILLING == 0:
        glutSolidCylinder(0.2, 1, APPROX, APPROX)

    glPopMatrix()
    glutSwapBuffers()


glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)

glutInitWindowSize(WIDTH, HEIGHT)

glutInitWindowPosition(200, 200)

glutInit(sys.argv)

glutCreateWindow(b"cg45")

glutDisplayFunc(draw)

glutSpecialFunc(specialkeys)

init()

glutMainLoop()

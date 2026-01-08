from OpenGL.GL import *
from OpenGL.GLU import *    
from OpenGL.GLUT import *

def DDA(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    if abs(dx) > abs(dy):
        steps = abs(dx)
    else:
        steps = abs(dy)

    xinc = dx / steps
    yinc = dy / steps

    x = x1
    y = y1

    glBegin(GL_LINE_STRIP)
    for i in range(steps):
        glVertex2f(round(x), round(y))
        x += xinc
        y += yinc
    glEnd()
    glFlush()

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    DDA(0,0,100,100) # Draw a line from (0,0) to (100,100)
    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutInitWindowPosition(300, 300)
glutCreateWindow(b"DDA Line Drawing Algorithm")
glClearColor(0, 0, 0, 0)
gluOrtho2D(0.0, 100.0, 0.0, 100.0)
glutDisplayFunc(draw)
glutMainLoop()



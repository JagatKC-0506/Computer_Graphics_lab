from OpenGL.GL import *
from OpenGL.GLU import *    
from OpenGL.GLUT import *

def midpoint(xc, yc, r):
    x = 0
    y = r

    p = 1 - r  # Initial decision parameter
    glBegin(GL_POINTS)
    
    # Loop from x=0 to x=y (45 degrees)
    # We iterate based on x and check the condition x <= y
    for _ in range(r + 1):
        if x > y:
            break
        
        glVertex2f(xc + x, yc + y)
        glVertex2f(xc - x, yc + y)
        glVertex2f(xc + x, yc - y)
        glVertex2f(xc - x, yc - y)
        glVertex2f(xc + y, yc + x)
        glVertex2f(xc - y, yc + x)
        glVertex2f(xc + y, yc - x)
        glVertex2f(xc - y, yc - x)

        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * x - 2 * y + 1
    glEnd()
    glFlush()

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    midpoint(50,50,40) # Draw a circle with center (50,50) and radius 40
    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutInitWindowPosition(300, 300)
glutCreateWindow(b"Midpoint Circle Drawing Algorithm")
glClearColor(0.0, 0.0, 0.0, 0.0)
gluOrtho2D(0.0, 100.0, 0.0, 100.0)
glutDisplayFunc(draw)
glutMainLoop()



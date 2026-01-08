# Bresenham Line Drawing algorithm for m>=1
from OpenGL.GL import *
from OpenGL.GLU import *    
from OpenGL.GLUT import *

def Bresenham(x1, y1, x2, y2):

    x = x1
    y = y1

    dx = x2 - x1
    dy = y2 - y1

    pk = 2 * dx - dy  # Initial decision parameter
    glBegin(GL_LINE_STRIP)
    for i in range(dy + 1):
        glVertex2f(x, y)  # Plot the current point
        y += 1  # Move in y direction
        if pk < 0:
            x = x 
            pk += 2 * dx 
             
        else:
            x += 1  
            pk += 2 * (dx - dy)  # Update decision parameter
    glEnd()
    glFlush()
# Display callback function - called whenever the window needs to be redrawn

    


def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    Bresenham(20,20,80,80) # Draw a line from (20,20) to (80,80)
    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutInitWindowPosition(300, 300)
glutCreateWindow(b"Bresenham Line Drawing Algorithm")
glClearColor(0.0, 0.0, 0.0, 0.0)
gluOrtho2D(0.0, 100.0, 0.0, 100.0)
glutDisplayFunc(draw)
glutMainLoop()



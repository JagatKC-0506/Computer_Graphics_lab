from OpenGL.GL import *
from OpenGL.GLU import *    
from OpenGL.GLUT import *

# Bresenham Line Drawing algorithm for m < 1
def Bresenham(x1, y1, x2, y2):
    """
    Bresenham's line algorithm optimized for slopes m < 1 (|dy| < |dx|).
    In this case, the line is more horizontal than vertical.
    For each step in x, we decide whether to increment y.
    """
    x = x1
    y = y1
    
    dx = x2 - x1
    dy = y2 - y1
    
    pk = 2 * dy - dx  # Initial decision parameter
    
    glBegin(GL_LINE_STRIP)
    for i in range(dx + 1):
        glVertex2f(x, y)  # Plot the current point
        x += 1  # Move in x direction
        if pk < 0:
            y = y  # Don't move in y
            pk += 2 * dy
        else:
            y += 1  # Move in y
            pk += 2 * (dy - dx)  # Update decision parameter
    glEnd()
    glFlush()

# Display callback function - called whenever the window needs to be redrawn
def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    Bresenham(20, 20, 90, 40)  # Draw a line from (20,20) to (90,40)
    glFlush()

# Initialize GLUT and OpenGL
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutInitWindowPosition(300, 300)
glutCreateWindow(b"Bresenham Line Drawing Algorithm")
glClearColor(0.0, 0.0, 0.0, 0.0)  # Black background
gluOrtho2D(0.0, 100.0, 0.0, 100.0)  # 2D coordinate system (0-100)
glutDisplayFunc(draw)
glutMainLoop()

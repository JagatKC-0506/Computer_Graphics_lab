from OpenGL.GL import *
from OpenGL.GLU import *    
from OpenGL.GLUT import *

# Midpoint Ellipse Drawing Algorithm
def midpoint_ellipse(xc, yc, rx, ry):
    """
    Midpoint ellipse drawing algorithm
    xc, yc: center of ellipse
    rx: semi-major axis (horizontal)
    ry: semi-minor axis (vertical)
    """
    x = 0
    y = ry
    
    # Decision parameter for region 1
    p1 = (ry * ry) - (rx * rx * ry) + (rx * rx / 4)
    
    glBegin(GL_POINTS)
    
    # Region 1: iterate along x-axis
    while (2 * ry * ry * x) <= (2 * rx * rx * y):
        # Plot the 4 symmetric points
        glVertex2f(xc + x, yc + y)
        glVertex2f(xc - x, yc + y)
        glVertex2f(xc + x, yc - y)
        glVertex2f(xc - x, yc - y)
        
        x += 1
        if p1 < 0:
            p1 = p1 + 2 * ry * ry * x + ry * ry
        else:
            y -= 1
            p1 = p1 + 2 * ry * ry * x - 2 * rx * rx * y + ry * ry
    
    # Region 2: iterate along y-axis
    p2 = (ry * ry * (x + 0.5) * (x + 0.5)) + (rx * rx * (y - 1) * (y - 1)) - (rx * rx * ry * ry)
    
    while y >= 0:
        # Plot the 4 symmetric points
        glVertex2f(xc + x, yc + y)
        glVertex2f(xc - x, yc + y)
        glVertex2f(xc + x, yc - y)
        glVertex2f(xc - x, yc - y)
        
        y -= 1
        if p2 > 0:
            p2 -= 2 * rx * rx * y - rx * rx
        else:
            x += 1
            p2 += 2 * ry * ry * x - 2 * rx * rx * y - rx * rx
    
    glEnd()
    glFlush()

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    midpoint_ellipse(250, 250, 150, 100)  # Draw an ellipse with center (250,250), semi-major axis 150, semi-minor axis 100
    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutCreateWindow(b"Midpoint Ellipse Drawing Algorithm")
glClearColor(0.0, 0.0, 0.0, 0.0)
gluOrtho2D(0.0, 500.0, 0.0, 500.0)
glutDisplayFunc(draw)
glutMainLoop()



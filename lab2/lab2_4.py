# Line Graph Using DDA and Bresenham Line Algorithm
from OpenGL.GL import *
from OpenGL.GLU import *    
from OpenGL.GLUT import *

# Sample data
data = [10, 25, 40, 35, 50, 45, 60, 55, 70, 65]

def DDA(x1, y1, x2, y2):
    """
    DDA (Digital Differential Analyzer) Algorithm
    Uses floating point arithmetic and incremental calculations
    """
    dx = x2 - x1
    dy = y2 - y1
    
    steps = max(abs(dx), abs(dy))
    
    if steps == 0:
        return
    
    xinc = dx / steps
    yinc = dy / steps
    
    x = x1
    y = y1
    
    glBegin(GL_LINE_STRIP)
    for i in range(int(steps) + 1):
        glVertex2f(round(x), round(y))
        x += xinc
        y += yinc
    glEnd()
    glFlush()

def Bresenham(x1, y1, x2, y2):
    """
    Bresenham Line Algorithm (BLA)
    Uses integer arithmetic only for efficient line drawing
    """
    x = int(x1)
    y = int(y1)
    x2 = int(x2)
    y2 = int(y2)
    
    dx = abs(x2 - x)
    dy = abs(y2 - y)
    
    sx = 1 if x2 > x else -1
    sy = 1 if y2 > y else -1
    
    glBegin(GL_LINE_STRIP)
    
    # Determine which is the primary direction
    if dx >= dy:
        # Line is more horizontal (m < 1)
        if dx == 0:
            # Single point
            glVertex2f(x, y)
        else:
            pk = 2 * dy - dx
            for i in range(dx + 1):
                glVertex2f(x, y)
                x += sx
                if pk < 0:
                    pk += 2 * dy
                else:
                    y += sy
                    pk += 2 * (dy - dx)
    else:
        # Line is more vertical (m >= 1)
        if dy == 0:
            # Single point
            glVertex2f(x, y)
        else:
            pk = 2 * dx - dy
            for i in range(dy + 1):
                glVertex2f(x, y)
                y += sy
                if pk < 0:
                    pk += 2 * dx
                else:
                    x += sx
                    pk += 2 * (dx - dy)
    
    glEnd()
    glFlush()

def draw():
    """Display callback function"""
    glClear(GL_COLOR_BUFFER_BIT)
    
    # Draw axes using Bresenham
    glColor3f(1.0, 1.0, 1.0)  # White
    Bresenham(5, 10, 5, 100)   # Y-axis
    Bresenham(5, 10, 100, 10)  # X-axis
    
    # Draw graph lines using DDA
    glColor3f(0.0, 1.0, 0.0)  # Green
    x_pos = 10
    scale_x = 8
    scale_y = 1.5
    
    for i in range(len(data) - 1):
        x1 = x_pos + i * scale_x
        y1 = 10 + data[i] * scale_y
        x2 = x_pos + (i + 1) * scale_x
        y2 = 10 + data[i + 1] * scale_y
        DDA(x1, y1, x2, y2)
    
    # Draw data points using Bresenham (small squares)
    glColor3f(1.0, 0.0, 0.0)  # Red
    for i in range(len(data)):
        x = int(x_pos + i * scale_x)
        y = int(10 + data[i] * scale_y)
        # Draw point at data position
        glBegin(GL_POINTS)
        glVertex2f(x, y)
        glEnd()
    
    glFlush()

# Initialize GLUT and OpenGL
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(800, 600)
glutInitWindowPosition(100, 100)
glutCreateWindow(b"Line Graph - DDA and Bresenham")
glClearColor(0.0, 0.0, 0.0, 0.0)
gluOrtho2D(0.0, 100.0, 0.0, 100.0)
glutDisplayFunc(draw)
glutMainLoop()

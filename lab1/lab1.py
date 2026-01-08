from OpenGL.GL import *
from OpenGL.GLU import *    
from OpenGL.GLUT import *

def draw_J(x):
    glBegin(GL_POLYGON)
    glVertex2f(x, 0.3)
    glVertex2f(x + 0.15, 0.3)
    glVertex2f(x + 0.15, 0.8)
    glVertex2f(x, 0.8)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(x - 0.1, 0.1)
    glVertex2f(x + 0.15, 0.1)
    glVertex2f(x + 0.15, 0.3)
    glVertex2f(x - 0.1, 0.3)
    glEnd()

def draw_A(x):
    # Triangle for A
    glBegin(GL_POLYGON)
    glVertex2f(x, 0.2)
    glVertex2f(x + 0.2, 0.8)
    glVertex2f(x + 0.4, 0.2)
    glEnd()
    
    # Horizontal bar in middle
    glBegin(GL_POLYGON)
    glVertex2f(x + 0.05, 0.45)
    glVertex2f(x + 0.35, 0.45)
    glVertex2f(x + 0.35, 0.55)
    glVertex2f(x + 0.05, 0.55)
    glEnd()









def draw_G(x):
    # Top horizontal bar
    glBegin(GL_POLYGON)
    glVertex2f(x, 0.7)
    glVertex2f(x + 0.35, 0.7)
    glVertex2f(x + 0.35, 0.8)
    glVertex2f(x, 0.8)
    glEnd()
    
    # Left vertical bar
    glBegin(GL_POLYGON)
    glVertex2f(x, 0.2)
    glVertex2f(x + 0.1, 0.2)
    glVertex2f(x + 0.1, 0.8)
    glVertex2f(x, 0.8)
    glEnd()
    
    # Bottom horizontal bar
    glBegin(GL_POLYGON)
    glVertex2f(x, 0.2)
    glVertex2f(x + 0.35, 0.2)
    glVertex2f(x + 0.35, 0.3)
    glVertex2f(x, 0.3)
    glEnd()
    
    # Right vertical bar (partial)
    glBegin(GL_POLYGON)
    glVertex2f(x + 0.25, 0.2)
    glVertex2f(x + 0.35, 0.2)
    glVertex2f(x + 0.35, 0.45)
    glVertex2f(x + 0.25, 0.45)
    glEnd()











def draw_T(x):
    glBegin(GL_POLYGON)
    glVertex2f(x, 0.7)
    glVertex2f(x + 0.4, 0.7)
    glVertex2f(x + 0.4, 0.8)
    glVertex2f(x, 0.8)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(x + 0.15, 0.2)
    glVertex2f(x + 0.25, 0.2)
    glVertex2f(x + 0.25, 0.7)
    glVertex2f(x + 0.15, 0.7)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.1, 0.9, 0.7)
    
    draw_J(-0.85)
    draw_A(-0.5)
    draw_G(-0.1)
    draw_A(0.25)
    draw_T(0.65)
    
    glFlush()











    

def init():
    glClearColor(0.05, 0.05, 0.1, 1.0)
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(-1.0, 1.0, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(1400, 700)
    glutCreateWindow(b"My Name - JAGAT")
    
    init()
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()
# Pie Chart Implementation
from OpenGL.GL import *
from OpenGL.GLU import *    
from OpenGL.GLUT import *
import math

# Sample data for pie chart
data = [30, 25, 20, 15, 10]  # Values that sum to 100
labels = ['A', 'B', 'C', 'D', 'E']

# Colors for each slice (RGB)
colors = [
    (1.0, 0.0, 0.0),  # Red
    (0.0, 1.0, 0.0),  # Green
    (0.0, 0.0, 1.0),  # Blue
    (1.0, 1.0, 0.0),  # Yellow
    (1.0, 0.0, 1.0)   # Magenta
]

def draw_pie_chart(data, center_x, center_y, radius):
    """
    Draw a pie chart with the given data
    - data: list of values (will be converted to percentages)
    - center_x, center_y: center of the pie chart
    - radius: radius of the pie chart
    """
    # Calculate total
    total = sum(data)
    
    # Starting angle
    start_angle = 0.0
    
    # Draw each slice
    for i in range(len(data)):
        # Calculate percentage and angle for this slice
        percentage = data[i] / total
        angle = percentage * 360.0  # in degrees
        
        # Set color for this slice
        glColor3f(colors[i][0], colors[i][1], colors[i][2])
        
        # Draw the slice as a triangle fan
        glBegin(GL_TRIANGLE_FAN)
        
        # Center point
        glVertex2f(center_x, center_y)
        
        # Draw arc points around the slice
        num_points = int(angle) + 1
        for j in range(num_points + 1):
            # Current angle for this point
            current_angle = start_angle + (angle * j / num_points)
            
            # Convert to radians
            rad = math.radians(current_angle)
            
            # Calculate point on circle
            x = center_x + radius * math.cos(rad)
            y = center_y + radius * math.sin(rad)
            
            glVertex2f(x, y)
        
        glEnd()
        glFlush()
        
        # Update start angle for next slice
        start_angle += angle

def draw_legend(data, labels, start_x, start_y):
    """
    Draw legend for the pie chart
    """
    glColor3f(1.0, 1.0, 1.0)  # White text
    
    for i in range(len(data)):
        # Draw colored square
        glColor3f(colors[i][0], colors[i][1], colors[i][2])
        
        # Draw small rectangle for legend
        glBegin(GL_QUADS)
        size = 2
        glVertex2f(start_x, start_y - i * 5)
        glVertex2f(start_x + size, start_y - i * 5)
        glVertex2f(start_x + size, start_y - size - i * 5)
        glVertex2f(start_x, start_y - size - i * 5)
        glEnd()
        
        glFlush()

def draw():
    """Display callback function"""
    glClear(GL_COLOR_BUFFER_BIT)
    
    # Draw pie chart in the center
    draw_pie_chart(data, 40, 50, 30)
    
    # Draw legend on the right
    draw_legend(data, labels, 75, 90)
    
    glFlush()

# Initialize GLUT and OpenGL
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(800, 600)
glutInitWindowPosition(100, 100)
glutCreateWindow(b"Pie Chart")
glClearColor(0.0, 0.0, 0.0, 0.0)  # Black background
gluOrtho2D(0.0, 100.0, 0.0, 100.0)  # 2D coordinate system
glutDisplayFunc(draw)
glutMainLoop()

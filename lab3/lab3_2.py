from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

# Draw X/Y axes with tick marks for reference
def draw_axes():
	glColor3f(0.9, 0.9, 0.9)
	glLineWidth(1.5)

	glBegin(GL_LINES)  # X axis
	glVertex2f(-100, 0)
	glVertex2f(100, 0)
	glEnd()

	glBegin(GL_LINES)  # Y axis
	glVertex2f(0, -100)
	glVertex2f(0, 100)
	glEnd()

	glLineWidth(1.0)
	glBegin(GL_LINES)  # tick marks every 10 units
	for x in range(-100, 101, 10):
		glVertex2f(x, -3)
		glVertex2f(x, 3)
	for y in range(-100, 101, 10):
		glVertex2f(-3, y)
		glVertex2f(3, y)
	glEnd()


# Base rectangle in 1st quadrant (counter-clockwise) - small rectangle
BASE_RECT = [(20.0, 20.0), (40.0, 20.0), (40.0, 35.0), (20.0, 35.0)]


def draw_rectangle(vertices):
	glBegin(GL_POLYGON)
	for x, y in vertices:
		glVertex2f(x, y)
	glEnd()


# Transformation controls (homogeneous coordinates)
# translation part
TX_OFFSET = 10.0  # adjust to move translated rectangle along X
TY_OFFSET = 10.0  # adjust to move translated rectangle along Y
# rotation part
ROT_ANGLE_DEG = 30.0  # rotation angle (degrees) for rotated rectangle
# scaling part
SCALE_X = 2  # scale factor along X axis
SCALE_Y = 2  # scale factor along Y axis
# reflection part
REFLECT_AXIS = 'y'  # reflection axis: 'x' for X-axis, 'y' for Y-axis
# shearing part
SHEAR_X = 0  # shear factor along X (shears Y coordinates)
SHEAR_Y = 0.1  # shear factor along Y (shears X coordinates)

def apply_transform(vertex, matrix):
	x, y = vertex
	# Multiply (x, y, 1) by 3x3 matrix -> (vx, vy, vw) in homogeneous coords
	vx = matrix[0][0] * x + matrix[0][1] * y + matrix[0][2]
	vy = matrix[1][0] * x + matrix[1][1] * y + matrix[1][2]
	vw = matrix[2][0] * x + matrix[2][1] * y + matrix[2][2]
	if vw != 0:  # project back to Cartesian by dividing through vw
		vx = vx / vw
		vy = vy / vw
	return vx, vy


def transform_shape(vertices, matrix):
	return [apply_transform(v, matrix) for v in vertices]


def multiply_matrices(m1, m2):
	# Multiply two 3x3 matrices: result = m1 * m2
	result = [[0.0 for _ in range(3)] for _ in range(3)]
	for i in range(3):
		for j in range(3):
			for k in range(3):
				result[i][j] += m1[i][k] * m2[k][j]
	return result


def display():
	glClear(GL_COLOR_BUFFER_BIT)
	draw_axes()

	# Fixed rectangle (green) at its original position
	glColor3f(0.0, 1.0, 0.0)
	draw_rectangle(BASE_RECT)

	# # Translated rectangle (red) using homogeneous translation matrix
	# translation_matrix = [
	# 	[1.0, 0.0, TX_OFFSET],  # add TX to x component
	# 	[0.0, 1.0, TY_OFFSET],  # add TY to y component
	# 	[0.0, 0.0, 1.0],
	# ]
	# # Apply matrix to every vertex to get translated copy
	# moved_rect = transform_shape(BASE_RECT, translation_matrix)
	# glColor3f(1.0, 0.2, 0.2)  # red for translated rectangle
	# draw_rectangle(moved_rect)

	# # Rotated rectangle (blue) about origin using homogeneous rotation matrix
	# angle_rad = math.radians(ROT_ANGLE_DEG)
	# cos_a, sin_a = math.cos(angle_rad), math.sin(angle_rad)
	# rotation_matrix = [
	# 	[cos_a, -sin_a, 0.0],
	# 	[sin_a,  cos_a, 0.0],
	# 	[0.0,    0.0,  1.0],
	# ]
	# rotated_rect = transform_shape(BASE_RECT, rotation_matrix)
	# glColor3f(0.2, 0.8, 1.0)  # blue for rotated rectangle
	# draw_rectangle(rotated_rect)

	# Scaled rectangle (yellow) using homogeneous scaling matrix
	# scaling matrix multiplies x and y by scale factors
	# scaling_matrix = [
	# 	[SCALE_X, 0.0,     0.0],  # scale X component
	# 	[0.0,     SCALE_Y, 0.0],  # scale Y component
	# 	[0.0,     0.0,     1.0],
	# ]
	# # Apply scaling to every vertex to get scaled copy
	# scaled_rect = transform_shape(BASE_RECT, scaling_matrix)
	# glColor3f(1.0, 1.0, 0.0)  # yellow for scaled rectangle
	# draw_rectangle(scaled_rect)

	# Reflected rectangle (magenta) using homogeneous reflection matrix
	# reflection matrix flips across an axis
	# if REFLECT_AXIS.lower() == 'x':
	# 	reflection_matrix = [
	# 		[1.0,  0.0, 0.0],  # x stays same
	# 		[0.0, -1.0, 0.0],  # y gets negated (reflect across X-axis)
	# 		[0.0,  0.0, 1.0],
	# 	]
	# else:  # reflect across Y-axis
	# 	reflection_matrix = [
	# 		[-1.0, 0.0, 0.0],  # x gets negated (reflect across Y-axis)
	# 		[0.0,  1.0, 0.0],  # y stays same
	# 		[0.0,  0.0, 1.0],
	# 	]
	# # Apply reflection to every vertex to get reflected copy
	# reflected_rect = transform_shape(BASE_RECT, reflection_matrix)
	# glColor3f(1.0, 0.0, 1.0)  # magenta for reflected rectangle
	# draw_rectangle(reflected_rect)

	# Sheared rectangle (cyan) using homogeneous shearing matrix
	# shearing matrix slants the shape along an axis
	# shearing_matrix = [
	# 	[1.0, SHEAR_Y, 0.0],  # shear X based on Y coordinate
	# 	[SHEAR_X, 1.0, 0.0],  # shear Y based on X coordinate
	# 	[0.0, 0.0, 1.0],
	# ]
	# # Apply shearing to every vertex to get sheared copy
	# sheared_rect = transform_shape(BASE_RECT, shearing_matrix)
	# glColor3f(0.0, 1.0, 1.0)  # cyan for sheared rectangle
	# draw_rectangle(sheared_rect)

	# COMPOSITE TRANSFORMATION: Combining 4 transformations
	# Order: Scale -> Rotate -> Shear -> Translate
	
	# 1. Scaling matrix
	scale_matrix = [
		[SCALE_X, 0.0, 0.0],
		[0.0, SCALE_Y, 0.0],
		[0.0, 0.0, 1.0],
	]
	
	# 2. Rotation matrix
	angle_rad = math.radians(ROT_ANGLE_DEG)
	cos_a, sin_a = math.cos(angle_rad), math.sin(angle_rad)
	rotate_matrix = [
		[cos_a, -sin_a, 0.0],
		[sin_a, cos_a, 0.0],
		[0.0, 0.0, 1.0],
	]
	
	# 3. Shearing matrix
	shear_matrix = [
		[1.0, SHEAR_Y, 0.0],
		[SHEAR_X, 1.0, 0.0],
		[0.0, 0.0, 1.0],
	]
	
	# 4. Translation matrix
	translate_matrix = [
		[1.0, 0.0, TX_OFFSET],
		[0.0, 1.0, TY_OFFSET],
		[0.0, 0.0, 1.0],
	]
	
	# Multiply matrices in order: translate * shear * rotate * scale
	# This creates a composite transformation
	composite = multiply_matrices(translate_matrix, shear_matrix)
	composite = multiply_matrices(composite, rotate_matrix)
	composite = multiply_matrices(composite, scale_matrix)
	
	# Apply composite transformation to all vertices
	composite_rect = transform_shape(BASE_RECT, composite)
	glColor3f(1.0, 0.5, 0.0)  # orange for composite transformed rectangle
	draw_rectangle(composite_rect)

	glFlush()


def init_view():
	glClearColor(0.0, 0.0, 0.0, 0.0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(-110.0, 110.0, -110.0, 110.0)


def main():
	glutInit()
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	glutInitWindowSize(700, 700)
	glutInitWindowPosition(200, 100)
	glutCreateWindow(b"Homogeneous Translation Demo")
	init_view()
	glutDisplayFunc(display)
	glutMainLoop()


if __name__ == "__main__":
	main()

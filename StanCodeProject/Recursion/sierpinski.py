"""
File: sierpinski.py
Name: 吳禹
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 6                  # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	TODO:
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	:param order:
	:param length:
	:param upper_left_x:
	:param upper_left_y:
	:return:
	"""
	if order == 0:
		pass
	else:
		# draw triangle
		line_1 = GLine(upper_left_x, upper_left_y, upper_left_x+0.5*length, upper_left_y+0.866*length)
		line_1_x1 = upper_left_x+0.5*length
		line_1_y1 = upper_left_y+0.866*length
		line_2 = GLine(upper_left_x, upper_left_y, upper_left_x+length, upper_left_y)
		line_2_x1 = upper_left_x+length
		line_3 = GLine(line_1_x1, line_1_y1, line_2_x1, upper_left_y)
		window.add(line_1)
		window.add(line_2)
		window.add(line_3)

		# do recursion
		# up_left triangle
		sierpinski_triangle(order-1, length/2, upper_left_x, upper_left_y)

		# up_right triangle
		sierpinski_triangle(order-1, length/2, upper_left_x+length/2, upper_left_y)

		# bottom triangle
		sierpinski_triangle(order-1, length/2, upper_left_x+0.5*length/2, upper_left_y+0.866*length/2)

		# pause
		# pause(1000)


if __name__ == '__main__':
	main()

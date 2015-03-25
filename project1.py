"""Draws a spirograph based on user inputs.

Liam Jones, 10523527

A Spirograph is a geometric drawing toy that uses interlocking gears of
different sizes to draw repeating shapes. It works by tracing a point in
one circle as it rotates along the inside (or sometimes the outside) of the
perimeter of another circle.

    Tasks

    You are required to write the following Python functions. Make sure you understand where each function fits into the system described above.

    docstring # (20%)
    The docstring is the comment at the start of the Python file. Your docstring should include:
    Your name and student number
    A short description of a Spirograph
    A description of how you calculated the hypotrochoid
    Instructions on how to interact with your project
    References to any resources used

    getInputs(): # (10%)
    This function should prompt the user for the values of the drawing parameters, and return these values to the calling program.

    getNumberOfPoints(R, r, prec): # R, r, prec>0 (10%)
    This function should determine the number of points (x,y coordinates) to calculate, assuming that every rotation of the rolling circle consists of prec points. To calculate this, you should write an extra function to calculate the greatest common divisor of two numbers.

    getPoints(R, r, d, prec): #R, r, d, prec>0 (20%)
    This function should return a list of pairs of floating point numbers. The first number in each pair should be the x-coordinate of the next point to draw, and the second number should be the y-coordinate of the next point to draw.

    draw(points): #points is a list of pairs of floating point numbers (30%)
    This function should display a window and draw the curve corresponding to the list of points. The window should stay visible until the user closes it. Marks will also be awarded for the presentation, so consider the background, colours and scaling of the picture.

    main(): #(10%)
    This function should call all the other functions and control the flow of the program. Once the user has drawn the picture, the program should give the user the option to continue or quit.
    There will be bonus marks (up to 10%) available for the following challenges:
    Use varying colour schemes to make the hypotrochoid look more appealing.
    Allow the user to choose to draw either a hypotrochoid (http://en.wikipedia.org/wiki/Hypotrochoid) or an epitrochoid (http://en.wikipedia.org/wiki/Epitrochoid).
    Allow the user to set parameters and draw figures using a graphical user interface
"""

import graphics


def getInputs():  # (10%)
    pass


def getNumberOfPoints(R, r, prec):  # R, r, prec > 0 (10%)
    pass


def getPoints(R, r, d, prec):  # R, r, d, prec > 0 (20%)
    pass


def draw(points):  # points is a list of pairs of floating point numbers (30%)
    pass


def main():
    pass
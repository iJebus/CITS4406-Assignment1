__author__ = 'Liam'
"""Drawing testing"""
# convert_gui.pyw
# Program to convert Celsius to Fahrenheit using a simple
# graphical interface.
from random import randint
from math import *
from time import sleep

from graphics import *


def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x


def getPoints(R, r, d, prec):  # R, r, d, prec > 0 (20%)
    """This function should return a list of pairs of floating point numbers
    relating to a Hypotrochoid. The first number in each pair should be the
    x-coordinate of the next point to draw, and the second number should be the
    y-coordinate of the next point to draw.
    """
    points = []
    for t in range(prec):
        points.append([(R - r) * cos(t) + d * cos(((R - r) / r) * t),
                       (R - r) * sin(t) - d * sin(((R - r) / r) * t)])
    return points


def getNumberOfPoints(R, r, prec):
    return prec * (r // gcd(R, r))


def main():
    R, r, d = 32, 10, 7
    win = GraphWin('Spyrograph Display', 500, 500)
    win.setBackground("#343434")
    # Line(Point(0, 250), Point(500, 250)).draw(win)  # x-axis
    # Line(Point(250, 0), Point(250, 500)).draw(win)  # y-axis

    prec = getNumberOfPoints(R, r, 360)
    points = getPoints(R, r, d, prec)

    print(len(points))

    x = [i for i, j in points]
    y = [j for i, j in points]

    win.setCoords(min(x) - 2, min(y) - 2, max(x) + 2, max(y) + 2)

    for i in points:
        p = Point(i[0], i[1])
        p.setFill(color_rgb(randint(0, 255), randint(0, 255), randint(0, 255)))
        p.draw(win)
        sleep(0.001)

    # win.setCoords(mini[0], mini[1], maxi[0], maxi[1])

    win.getMouse()
    win.close()


main()
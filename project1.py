"""Draws a spirograph based on user inputs.

Liam Jones, 10523527

Description of a Spirograph:
A Spirograph is a geometric drawing toy that uses interlocking gears of
different sizes to draw repeating shapes. It works by tracing a point in
one circle as it rotates along the inside (or sometimes the outside) of the
perimeter of another circle.

Description of how the hypotroidchoid was calculated:
First, 'prec' variable is created with a value of 360, or the number of degrees
in a circle.

Then, the radius' of the fixed and the rolling circle are collected from the
user, along with the distance of the pen from the center of the rolling circle.

Using these values, we can then calculate the total number of revolutions the
rolling circle will make until the pen begins to repeat the pattern. This is
multiplied against 'prec' to give us the total number of points that will exist
on the graph.

Knowing this, we can then run the parametric equations on that range to find
the coordinates for each point on the graph. It's literally then a matter of
'joining the dots' to create our image.

Instructions:
    CLI version:
        Enter the desired values as prompted. An example of a valid input is
        "5, 3, 5", without the quotation marks.

        Watch as your graph is displayed.

References:
http://en.wikipedia.org/wiki/Hypotrochoid
https://www.python.org/dev/peps/pep-0257/
http://stackoverflow.com/questions/11175131/code-for-greatest-common-divisor-in-python
https://docs.python.org/dev/library/fractions.html#fractions.gcd

    There will be bonus marks (up to 10%) available for the following challenges:
        Use varying colour schemes to make the hypotrochoid look more appealing.
        Allow the user to choose to draw either a hypotrochoid (http://en.wikipedia.org/wiki/Hypotrochoid) or an epitrochoid (http://en.wikipedia.org/wiki/Epitrochoid).
        Allow the user to set parameters and draw figures using a graphical user interface
        sam - try do it with a fragment shader

    Your task for this project is to write a Spyrograph (a python simulation of a Spirograph). The program should allow the user to enter the parameters for a Spirograph drawing, and then produce the corresponding picture in a window. The picture created by the Spirograph (a hypotrochoid) depends on three parameters:

    R the radius of the fixed circle.
    r the radius of the rolling circle
    d the distance of the pen from the center of the rolling circle

    The points of the hypotrochoid are the described by the parametric equations:

    x(t) = (R-r) * (cos * t) + (d * cos) * (t * ((R-r) / r))
    y(t) = (R-r) * (sin * t) + (d * sin) * (t * ((R-r) / r))

    Here, t can be thought of as the time parameter, and (assuming you are using radians)
    every 2 * pi the rolling circle will go around the fixed circle once. Assuming R
    and r are positive integers, the number of times the rolling circle goes around
    the fixed circle before it starts to repeat itself is r/gcd(R, r) (that is the
    radius of the rolling circle divided by the greatest common divisor of the rolling
    circle and the fixed circle).

    time / Theta? = t
    One complete revolution of small circle inside large circle = 2 * pi - Is this irrelevant?
    Revolutions until pattern starts repeating = r / gcd(R, r)
    Points of the Hypotrochoid:
        x(t) = (R-r) * (cos * t) + (d * cos) * (t * ((R-r) / r))
        y(t) = (R-r) * (sin * t) + (d * sin) * (t * ((R-r) / r))
    Radius of the fixed circle = R
    Radius of the rolling circle = r
    Distance of the pen from the center of the rolling circle = d

    Let's try an example
    R = 5, r = 3, d = 5

    Revolutions until pattern repeats: 3 / gcd(5, 3) = 3
    Theta max: 3 * 360 = 1080

    points = []
    for t in range(1080):
        points.append([(R - r) * cos(t) + (d * cos) * (t * ((R - r) / r)),
                       (R - r) * sin(t) - (d * sin) * (t * ((R - r) / r))])
    return points

"""

from graphics import GraphWin, Point
# from fractions import gcd
from math import *


def getInputs():  # (10%)
    """This function should prompt the user for the values of the drawing
    parameters, and return these values to the calling program.
    """
    return list(map(int, input('Please enter the radius of the fixed circle,'
                               ' the radius of the rolling circle and the '
                               'distance of the pen from the center of the '
                               'rolling circle.\nFor example; 5, 3, 5 is a '
                               'valid input.\n>> ').split(",")))


def gcd(x, y):
    """Or use fractions.gcd(x, y); wait for Tim's feedback."""
    while y != 0:
        (x, y) = (y, x % y)
    return x


def getNumberOfPoints(R, r, prec):  # R, r, prec > 0 (10%)
    """This function should determine the number of points (x, y coordinates) to
    calculate, assuming that every rotation of the rolling circle consists of
    prec points. To calculate this, you should write an extra function to
    calculate the greatest common divisor of two numbers.
    """
    return prec * (r // gcd(R, r))


def getPoints(R, r, d, prec):  # R, r, d, prec > 0 (20%)
    """This function should return a list of pairs of floating point numbers.
    The first number in each pair should be the x-coordinate of the next point
    to draw, and the second number should be the y-coordinate of the next point
    to draw.
    """
    points = []
    for t in range(prec):
        points.append([(R - r) * cos(t) + d * cos(((R - r) / r) * t),
                       (R - r) * sin(t) - d * sin(((R - r) / r) * t)])
    print(max(points))
    return points


def draw(points):  # points is a list of pairs of floating point numbers (30%)
    """This function should display a window and draw the curve corresponding
    to the list of points. The window should stay visible until the user closes
    it. Marks will also be awarded for the presentation, so consider the
    background, colours and scaling of the picture.
    """
    win = GraphWin('Spyrograph', 300, 300)
    for i in points:
        p = Point((i[0] + 10) * 15, (i[1] + 10) * 15)
        p.draw(win)
    win.mainloop()


def main():  # (10%)
    """This function should call all the other functions and controls the flow
    of the program. Once the user has drawn the picture, the program should
    give the user the option to continue or quit.
    """
    prec = 360
    R, r, d = getInputs()
    prec = getNumberOfPoints(R, r, prec)
    points = getPoints(R, r, d, prec)
    draw(points)


main()
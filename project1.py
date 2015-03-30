"""Draws a spirograph based on user inputs.

Liam Jones, 10523527

Description of a Spirograph:
A Spirograph is a geometric drawing toy that uses interlocking gears of
different sizes to draw repeating shapes. It works by tracing a point in
one circle as it rotates along the inside (or sometimes the outside) of the
perimeter of another circle.

Description of how the graph values are calculated:
First, 'prec' variable is created with a value of 360, or the number of degrees
in a circle.

Then, the radius' of the fixed and the rolling circle are collected from the
user, along with the distance of the pen from the center of the rolling circle.

Using these values, we can then calculate the total number of revolutions the
rolling circle will make until the pen begins to repeat the pattern. This is
multiplied against 'prec' to give us the total number of points that will exist
on the graph.

Knowing this, we can then run the parametric equations on that range to find
the coordinates for each point on the graph. These equations differ slightly
depending on whether an Epitrochoid or a Hypotrochoid is being displayed.
It's literally then a matter of 'joining the dots' to create our image.


Instructions:
    Select the interface type desired (CLI or GUI) and then enter desired
    values as prompted.

    Watch as your graph is displayed!

    Click your graph to end the program.

References:
http://en.wikipedia.org/wiki/Hypotrochoid
http://en.wikipedia.org/wiki/Epitrochoid
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
from random import randint
from math import *

from graphics import GraphWin, Point, color_rgb, Text, Rectangle, Entry, Line



# from fractions import gcd


def get_input_method():
    """This function prompts the user as to whether they want to draw a GUI or
    the CLI. The function will loop until valid input is achieved.
    """
    types = ['CLI', 'GUI']
    while True:
        selection = input('Would you prefer a CLI or GUI?\n>> ')
        if selection in types:
            print('{} selected.'.format(selection))
            return selection
        else:
            print('You didn\'t correctly select :( '
                  'Please type either CLI or GUI when prompted.')


def get_type():
    """This function prompts the user as to whether they want to draw an
    Epitrochoid or a Hypotrochoid. The function will loop until valid input is
    achieved.
    """
    types = ['Epitrochoid', 'Hypotrochoid']
    while True:
        selection = input('Please tell me if you\'d like to draw an '
                          'Epitrochoid or a Hypotrochoid.\n>> ')
        if selection in types:
            print('{} selected'.format(selection))
            return selection
        else:
            print('You didn\'t correctly select :( Please write either '
                  'Epitrochoid or Hypotrochoid when prompted.')


def getInputs():  # (10%)
    """This function should prompt the user for the values of the drawing
    parameters, and return these values to the calling program.
    """
    return list(map(float, input('Please enter the radius of the fixed circle,'
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
    """This function should return a list of pairs of floating point numbers
    relating to a Hypotrochoid. The first number in each pair should be the
    x-coordinate of the next point to draw, and the second number should be the
    y-coordinate of the next point to draw.
    """
    points = []
    for t in range(prec):
        points.append([(R - r) * cos(t) + d * cos(((R - r) / r) * t),
                       (R - r) * sin(t) - d * sin(((R - r) / r) * t)])
    print(max(points))
    return points


def get_points_epitrochoid(R, r, d, prec):
    """This function should return a list of pairs of floating point numbers
    relating to an Epitrochoid. The first number in each pair should be the
    x-coordinate of the next point to draw, and the second number should be the
    y-coordinate of the next point to draw.
    """
    points = []
    for t in range(prec):
        points.append([(R + r) * cos(t) - d * cos(((R + r) / r) * t),
                       (R + r) * sin(t) - d * sin(((R + r) / r) * t)])
    return points


def draw(points):  # points is a list of pairs of floating point numbers (30%)
    """This function should display a window and draw the curve corresponding
    to the list of points. The window should stay visible until the user closes
    it. Marks will also be awarded for the presentation, so consider the
    background, colours and scaling of the picture.

    win = GraphWin('Spyrograph Display', 400, 400)
    win.setBackground("#343434")
    for i in zip(points[1:], points):
        p = Point((i[0] + 14) * 15, (i[1] + 14) * 15)
        p.setFill(color_rgb(randint(0, 255), randint(0, 255), randint(0, 255)))
        p.draw(win)
    win.getMouse()
    win.close()
    """
    win = GraphWin('Spyrograph Display', 500, 500)
    win.setBackground("#343434")
    Line(Point(250, 0), Point(250, 500)).draw(win)
    Line(Point(0, 250), Point(500, 250)).draw(win)
    for a, b in zip(points, points[1:]):
        p = Line(Point((a[0] + 250) * 20, (a[1] + 250) * 20),
                 Point((b[0] + 250) * 20, (b[1] + 250) * 20))
        p.setFill(color_rgb(randint(0, 255), randint(0, 255), randint(0, 255)))
        # p.setWidth(1)
        p.draw(win)
    win.getMouse()
    win.close()


def gui_interface():
    """This function provides a GUI via graphics.py for the user to enter
    the required information for their Spyrograph.
    """
    gui = GraphWin("Spyrograph Menu", 400, 400)
    gui.setCoords(0.0, 0.0, 10, 12)

    Text(Point(5, 11), "Type: Epitrochoid or Hypotrochoid?").draw(gui)
    type_graph = Entry(Point(5, 10), 12)
    type_graph.draw(gui)

    Text(Point(5, 9), "Radius of the outer circle?").draw(gui)
    outer_circle_r_graph = Entry(Point(5, 8), 4)
    outer_circle_r_graph.setText("0.0")
    outer_circle_r_graph.draw(gui)

    Text(Point(5, 7), "Radius of the inner circle?").draw(gui)
    inner_circle_r_graph = Entry(Point(5, 6), 4)
    inner_circle_r_graph.setText("0.0")
    inner_circle_r_graph.draw(gui)

    Text(Point(5, 5), "Distance value?").draw(gui)
    distance_graph = Entry(Point(5, 4), 4)
    distance_graph.setText("0.0")
    distance_graph.draw(gui)

    button = Text(Point(5, 2), "Display!")
    button.draw(gui)
    Rectangle(Point(3, 1), Point(7, 3)).draw(gui)

    gui.getMouse()
    button.setText("Displaying!")

    return [str(type_graph.getText()),
            eval(outer_circle_r_graph.getText()),
            eval(inner_circle_r_graph.getText()),
            eval(distance_graph.getText())]


def main():  # (10%)
    """This function should call all the other functions and controls the flow
    of the program. Once the user has drawn the picture, the program should
    give the user the option to continue or quit.
    """
    prec = 360
    if get_input_method() == 'CLI':
        graph_type = get_type()
        R, r, d = getInputs()
        prec = getNumberOfPoints(R, r, prec)
        if graph_type == 'Epitrochoid':
            points = get_points_epitrochoid(R, r, d, int(prec))
        else:
            points = getPoints(R, r, d, int(prec))
        print("Click the graph to quit.")
        draw(points)

    else:
        graph_type, R, r, d = gui_interface()
        prec = getNumberOfPoints(R, r, prec)
        if graph_type == 'Epitrochoid':
            points = get_points_epitrochoid(R, r, d, int(prec))
        else:
            points = getPoints(R, r, d, int(prec))
        draw(points)

main()
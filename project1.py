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
We can then map out these points to create our image.

Instructions:
    Select the interface type desired (CLI or GUI) and then enter desired
    values as prompted.

    Watch as your graph is displayed!

    Click your graph to end the program.

References:
http://en.wikipedia.org/wiki/Hypotrochoid
http://en.wikipedia.org/wiki/Epitrochoid
https://www.python.org/dev/peps/pep-0257/
http://www.cs.duke.edu/~ola/patterns/plopd/loops.html#loop-and-a-half
http://stackoverflow.com/questions/11175131/code-for-greatest-common-divisor-in-python
http://stackoverflow.com/questions/4004550/converting-string-series-to-float-list-in-python
"""
from random import randint
from math import *
from time import sleep

from graphics import GraphWin, Point, color_rgb, Text, Rectangle, Entry


def get_input_method():
    """This function prompts the user as to whether they want to use a GUI or
    the CLI. The function will loop until valid input is achieved. It uses the
    'loop and a half' method to allow users to correct invalid input.
    """
    types = ['CLI', 'GUI']
    while True:
        selection = input('Would you prefer a CLI or GUI?\n>> ').upper()
        if selection in types:
            print('{0} selected.\n'.format(selection))
            return selection
        print('You didn\'t correctly select :( Please type either CLI or GUI '
              'when prompted.\n')


def get_type():
    """This function prompts the user as to whether they want to draw an
    Epitrochoid or a Hypotrochoid. The function will loop until valid input is
    achieved. Again, the 'loop and a half' method was used.
    """
    types = ['Epitrochoid', 'Hypotrochoid']
    while True:
        selection = input('Please tell me if you\'d like to draw an '
                          'Epitrochoid or a Hypotrochoid.\n>> ')
        if selection in types:
            print('{} selected'.format(selection))
            return selection
        print('You didn\'t correctly select :( Please write either '
              'Epitrochoid or Hypotrochoid when prompted.\n')


def getInputs():
    """This function prompts the user for the values of the drawing parameters,
     and return these values to the calling program. Again, the 'loop and a
     half' method was used.
    """
    while True:
        inputs = input('Please enter the radius of the fixed circle, the '
                       'radius of the rolling circle and the distance of the '
                       'pen from the center of the rolling circle.\nFor '
                       'example, "5, 3, 5" is a valid input.\n>> ').split(', ')
        if len(inputs) == 3 and [i.isdigit() for i in inputs]:
            inputs = [float(x) for x in inputs]
            return inputs
        print('Sorry, error :( You probably either provided too many or '
              'too few inputs, or you haven\'t used commas to separate them.\n'
              'Also, if you\'re using the example , don\'t include the quote'
              ' marks.\n')


def gcd(x, y):
    """This function returns the greatest common denominator of x and y."""
    while y != 0:
        (x, y) = (y, x % y)
    return x


def getNumberOfPoints(R, r, prec):
    """This function calculates the number of points (x, y coordinates),
    assuming that every rotation of the rolling circle consists of
    prec points. It makes use of the gcd function.
    """
    return prec * (r // gcd(R, r))


def getPoints(R, r, d, prec):
    """This function returns a list of pairs of floating point numbers
    relating to a Hypotrochoid. The first number in each pair is the
    x-coordinate of the next point to draw, and the second number is the
    y-coordinate of the next point to draw.
    """
    points = []
    for t in range(int(prec)):
        points.append([(R - r) * cos(t) + d * cos(((R - r) / r) * t),
                       (R - r) * sin(t) - d * sin(((R - r) / r) * t)])
    return points


def get_points_epitrochoid(R, r, d, prec):
    """This function returns a list of pairs of floating point numbers
    relating to an Epitrochoid. The first number in each pair is the
    x-coordinate of the next point to draw, and the second number is the
    y-coordinate of the next point to draw.
    """
    points = []
    for t in range(int(prec)):
        points.append([(R + r) * cos(t) - d * cos(((R + r) / r) * t),
                       (R + r) * sin(t) - d * sin(((R + r) / r) * t)])
    return points


def draw(points):
    """This function display a window and marks the points corresponding
    to the list of points. The window is visible until the user closes
    it.
    """
    win = GraphWin('Spyrograph Display', 500, 500)
    win.setBackground("#343434")
    for i in points:
        p = Point((i[0] + 15.625) * 16, (i[1] + 15.625) * 16)
        p.setFill(color_rgb(randint(0, 255), randint(0, 255), randint(0, 255)))
        p.draw(win)
        sleep(0.001)
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
    gui.close()

    return [str(type_graph.getText()),
            eval(outer_circle_r_graph.getText()),
            eval(inner_circle_r_graph.getText()),
            eval(distance_graph.getText())]


def main():  # (10%)
    """This function calls all the other functions and controls the flow
    of the program. Once the user has drawn the picture, the program gives the
    user the option to continue or quit.
    """
    prec = 360
    count = 0

    while True:
        if count == 0:
            finished = input('Would you like to draw a Spyrograph? Yes or no, '
                             'please.\n>> ').upper()
        else:
            finished = input('How fun! I\'m not keeping score, but, that\'s {}'
                             ' now. Would you like to go again? Yes or no, '
                             'please.\n>> '.format(count)).upper()

        if finished in ['NO', 'N']:
            print('Alright, seeya later. Cheers!')
            raise SystemExit

        if finished in ['YES', 'Y']:
            count += 1
            if get_input_method() == 'CLI':
                graph_type = get_type()
                R, r, d = getInputs()
                prec = getNumberOfPoints(R, r, prec)
                if graph_type == 'Epitrochoid':
                    points = get_points_epitrochoid(R, r, d, prec)
                else:
                    points = getPoints(R, r, d, prec)
                print("Click the graph to quit.")
                draw(points)
            else:
                graph_type, R, r, d = gui_interface()
                prec = getNumberOfPoints(R, r, prec)
                if graph_type == 'Epitrochoid':
                    points = get_points_epitrochoid(R, r, d, prec)
                else:
                    points = getPoints(R, r, d, prec)
                draw(points)



main()
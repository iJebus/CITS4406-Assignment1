__author__ = 'Liam'
"""Drawing testing"""
# convert_gui.pyw
# Program to convert Celsius to Fahrenheit using a simple
# graphical interface.
from graphics import *


def main():
    win = GraphWin("Spyrograph Menu", 400, 400)
    win.setCoords(0.0, 0.0, 10, 12)

    # Draw the interface
    # Text(Point(1, 3), "Spyrograph").draw(win)
    Text(Point(5, 11), "Type: Epitrochoid or Hypotrochoid?").draw(win)
    type_graph = Entry(Point(5, 10), 12)
    type_graph.draw(win)
    Text(Point(5, 9), "Radius of the outer circle?").draw(win)
    outer_circle_r_graph = Entry(Point(5, 8), 4)
    outer_circle_r_graph.setText("0.0")
    outer_circle_r_graph.draw(win)
    Text(Point(5, 7), "Radius of the inner circle?").draw(win)
    inner_circle_r_graph = Entry(Point(5, 6), 4)
    inner_circle_r_graph.setText("0.0")
    inner_circle_r_graph.draw(win)
    Text(Point(5, 5), "Distance value?").draw(win)
    distance_graph = Entry(Point(5, 4), 4)
    distance_graph.setText("0.0")
    distance_graph.draw(win)
    button = Text(Point(5, 2), "Display!")
    button.draw(win)
    Rectangle(Point(3, 1), Point(7, 3)).draw(win)

    # wait for a mouse click
    win.getMouse()

    graph = GraphWin("Spyrograph Graph", 400, 400)
    Text(Point(1, 1), "NEW WINDOW!").draw(graph)

    win.getMouse()
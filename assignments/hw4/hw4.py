"""
Name: <Sam Marshall Buck>
<hw4>.py

Problem: <This assignment had us solve the problem of getting user input with mouse clicks
and substituting them to get the graphics to work in the windows also while using for loops.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.>
"""

import math
from graphics import GraphWin, Circle, Point, Text, Rectangle


def squares():
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Clicks", width, height)

    # number of times user can move rectangle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to move square")
    instructions.draw(win)

    # builds a rectangle
    shape = Rectangle(Point(50, 50), Point(100, 100))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the square
    for _ in range(num_clicks):
        click = win.getMouse()
        center = shape.getCenter()  # center of square

        # move amount is distance from center of square to the
        # point where the user clicked
        change_x = click.getX() - center.getX()
        change_y = click.getY() - center.getY()

        # clones the square and draws it
        shape = shape.clone()
        shape.draw(win)
        shape.move(change_x, change_y)

    win.getMouse()
    win.close()


def rectangle():
    width = 400
    height = 400
    win = GraphWin("Rectangle", width, height)

    user_clicks = 1

    for _ in range(user_clicks):
        point_1 = win.getMouse()
        point_2 = win.getMouse()
        shape = Rectangle(point_1, point_2)
        shape.setOutline("green")
        shape.setFill("green")
        shape.draw(win)

    inst_1 = Point(width / 2, height - 200)
    instructions = Text(inst_1, "Click again to close")
    instructions.draw(win)

    length = abs(point_1.x - point_2.x)
    width = abs(point_1.y - point_2.y)
    perimeter = (2 * length) + (2 * width)
    area = length * width

    inst_2 = Point(200, 300)
    instructions_2 = Text(inst_2, "Perimeter")
    instructions_2.draw(win)

    calc_1 = Point(200, 325)
    calc_instructions_1 = Text(calc_1, perimeter)
    calc_instructions_1.draw(win)

    inst_3 = Point(200, 350)
    instructions_3 = Text(inst_3, "Area")
    instructions_3.draw(win)

    calc_2 = Point(200, 375)
    calc_instructions_2 = Text(calc_2, area)
    calc_instructions_2.draw(win)

    win.getMouse()
    win.close()


def circle():
    width = 400
    height = 400
    win = GraphWin("Circle", width, height)

    user_clicks = 1

    for _ in range(user_clicks):
        center = win.getMouse()
        edge = win.getMouse()
        calc_1 = (edge.getX() - center.getX())**2 + (edge.getY() - center.getY())**2
        radius = math.sqrt(calc_1)
        shape = Circle(center, radius)
        shape.setOutline("blue")
        shape.setFill("blue")
        shape.draw(win)

    inst_1 = Point(width / 2, height - 200)
    instructions = Text(inst_1, "Click again to close")
    instructions.draw(win)

    inst_2 = Point(width / 2, height - 75)
    instructions_2 = Text(inst_2, "Radius")
    instructions_2.draw(win)

    inst_3 = Point(width / 2, height - 50)
    instructions_3 = Text(inst_3, radius)
    instructions_3.draw(win)

    win.getMouse()
    win.close()


def pi2():
    user_input = eval(input("enter the number of terms to sum: "))
    my_sum = 0
    my_total = 0
    for i in range(1, user_input + 1):
        sequence = (-1) ** i / (2 * i - 1)
        my_sum = my_sum + sequence
        my_total = my_sum * (-4)

    print("pi approximation:", my_total)
    accuracy = math.pi - my_total
    print("accuracy: ", accuracy)


if __name__ == '__main__':
    pass

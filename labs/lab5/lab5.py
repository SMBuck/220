import math
from graphics import *


def triangle():
    width = 500
    height = 500
    win = GraphWin("Triangle", width, height)

    user_clicks = 1

    for i in range(user_clicks):
        p_1 = win.getMouse()
        p_2 = win.getMouse()
        p_3 = win.getMouse()
        shape = Polygon(p_1, p_2, p_3)
        shape.setFill("red")
        shape.setOutline("black")
        shape.draw(win)

    inst_1 = Point(width / 2, height - 200)
    instructions = Text(inst_1, "Click again to close")
    instructions.draw(win)

    x_1 = p_1.getX()
    y_1 = p_1.getY()
    x_2 = p_2.getX()
    y_2 = p_2.getY()
    x_3 = p_3.getX()
    y_3 = p_3.getY()
    da = x_2 - x_1
    db = y_2 - y_1
    dc = x_3 - x_2
    dd = y_3 - y_2
    de = x_3 - x_1
    df = y_3 - y_1
    value_1 = (da ** 2) + (db ** 2)
    value_2 = (dc ** 2) + (dd ** 2)
    value_3 = (de ** 2) + (df ** 2)
    length_side1 = math.sqrt(value_1)
    length_side2 = math.sqrt(value_2)
    length_side3 = math.sqrt(value_3)
    perimeter = length_side1 + length_side2 + length_side3
    s = (length_side1 + length_side2 + length_side3) / 2
    area = s * (s-length_side1) * (s-length_side2) * (s-length_side3)
    total_area = math.sqrt(area)

    inst_2 = Point(width / 2, height - 100)
    instructions_2 = Text(inst_2, "Perimeter")
    instructions_2.draw(win)

    inst_3 = Point(width / 2, height - 75)
    instructions_3 = Text(inst_3, perimeter)
    instructions_3.draw(win)

    inst_4 = Point(width / 2, height - 50)
    instructions_4 = Text(inst_4, "Area")
    instructions_4.draw(win)

    inst_5 = Point(width / 2, height - 25)
    instructions_5 = Text(inst_5, total_area)
    instructions_5.draw(win)

    win.getMouse()
    win.close()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")
    red_text_input = Entry(Point(win_width / 2 - 5, win_height / 2 + 40), 5)
    red_text_input.setText("0")
    red_text_input.draw(win)


    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")
    green_text_input = red_text_input.clone()
    green_text_input.move(0, 30)
    green_text_input.draw(win)

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")
    blue_text_input = red_text_input.clone()
    blue_text_input.move(0, 60)
    blue_text_input.draw(win)


    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    for i in range(5):
        red = eval(red_text_input.getText())
        green = eval(green_text_input.getText())
        blue = eval(blue_text_input.getText())
        rgb = color_rgb(red, green, blue)
        shape.setFill(rgb)
        win.getMouse()


    # prompts user to click to close window
    msg_2 = "Click again to close"
    inst_1 = Text(Point(win_width / 2, win_height - 50), msg_2)
    inst_1.draw(win)

    # Wait for another click to exit
    win.getMouse()
    win.close()


def process_string():
    user_input = input("enter string here: ")
    first_character = user_input[0]
    length = len(user_input)
    last_character = user_input[-1]
    series_input = user_input[2:6]
    cat = first_character + last_character
    repeat = user_input[0:4] * 10
    print(first_character)
    print(last_character)
    print(series_input)
    print(cat)
    print(repeat)
    for i in user_input:
        print(i)
    print(length)


def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    x1 = values[1] + values[3]
    print(x1)
    x2 = values[0] + values[2]
    print(x2)
    x3 = values[1] * 5
    print(x3)
    x4 = values[2:5]
    print(x4)
    x5 = values[2]
    print(x5)
    x6 = values[2], values[0], float(values[5])
    print(x6)
    x7 = values[0] + values[2] + float(values[5])
    print(x7)
    x8 = len(values)
    print(x8)


def another_series():
    user_input = eval(input("enter number of terms:"))
    my_sum = 0
    sequence = 0
    for i in range(1, user_input + 1):
        sequence = (sequence % 6)
        sequence = sequence + 2
        my_sum = my_sum + sequence
        print(sequence, end=" ")
    print("\n sum=", my_sum)


def target():
    width = 500
    height = 500
    win = GraphWin("Target", width, height)

    shape_5 = Circle(Point(width / 2, height / 2), width / 10 + 195)
    shape_5.setFill("black")
    shape_5.setOutline("black")
    shape_5.draw(win)

    shape_4 = Circle(Point(width / 2, height / 2), width / 10 + 150)
    shape_4.setFill("white")
    shape_4.setOutline("black")
    shape_4.draw(win)

    shape_3 = Circle(Point(width / 2, height / 2), width / 10 + 100)
    shape_3.setFill("red")
    shape_3.setOutline("black")
    shape_3.draw(win)

    shape_2 = Circle(Point(width / 2, height / 2), width / 10 + 50)
    shape_2.setFill("blue")
    shape_2.setOutline("black")
    shape_2.draw(win)

    shape_1 = Circle(Point(width / 2, height / 2), width / 10)
    shape_1.setFill("yellow")
    shape_1.setOutline("Black")
    shape_1.draw(win)

    msg = "Click again to close"
    instructions = Text(Point(width / 2, height - 20), msg)
    instructions.setTextColor("white")
    instructions.draw(win)

    win.getMouse()
    win.close()



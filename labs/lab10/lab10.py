from button import Button
from door import Door
from graphics import *


def main():
    width = 700
    height = 700
    win = GraphWin("secret door", width, height)

    button_p1 = Point(100, 50)
    button_p2 = Point(600, 150)
    shape_1 = Button(Rectangle(button_p1, button_p2), "Exit")
    shape_1.draw(win)

    door_p1 = Point(200, 250)
    door_p2 = Point(500, 700)
    shape_2 = Door(Rectangle(door_p1, door_p2), "Closed")
    shape_2.draw(win)
    shape_2.color_door("red")

    user_click = win.getMouse()

    while not shape_1.is_clicked(user_click):
        if shape_2.is_clicked(user_click):
            status = shape_2.get_label()
            if status == "Open":
                shape_2.close("red", "Closed")
            else:
                shape_2.open("white", "Open")
        user_click = win.getMouse()

    win.close()


if __name__ == "__main__":
    main()

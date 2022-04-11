from lab10.button import Button
from lab10.door import Door
from graphics import *
from random import randint


def main():
    width = 1000
    height = 1000
    win = GraphWin("Three Door Game", width, height)

    button_p1 = Point(750, 50)
    button_p2 = Point(950, 100)
    button_1 = Button(Rectangle(button_p1, button_p2), "Quit")
    button_1.draw(win)

    door_p1 = Point(100, 250)
    door_p2 = Point(300, 700)
    door_1 = Door(Rectangle(door_p1, door_p2), "Door 1")
    door_1.draw(win)
    door_1.color_door("saddle brown")

    door_p3 = Point(400, 250)
    door_p4 = Point(600, 700)
    door_2 = Door(Rectangle(door_p3, door_p4), "Door 2")
    door_2.draw(win)
    door_2.color_door("saddle brown")

    door_p5 = Point(700, 250)
    door_p6 = Point(900, 700)
    door_3 = Door(Rectangle(door_p5, door_p6), "Door 3")
    door_3.draw(win)
    door_3.color_door("saddle brown")

    win_p1 = Point(50, 50)
    win_p2 = Point(150, 100)
    win_column = Rectangle(win_p1, win_p2)
    win_center = win_column.getCenter()
    win_text = Text(win_center, "0")
    win_text.draw(win)
    win_column.draw(win)

    win_txt = "Wins"
    winning = Text(Point(100, 25), win_txt)
    winning.draw(win)

    loss_p1 = Point(150, 50)
    loss_p2 = Point(250, 100)
    loss_column = Rectangle(loss_p1, loss_p2)
    loss_center = loss_column.getCenter()
    loss_text = Text(loss_center, "0")
    loss_text.draw(win)
    loss_column.draw(win)

    loss_txt = "Losses"
    losses = Text(Point(200, 25), loss_txt)
    losses.draw(win)

    inst_1 = "There is a secret door somewhere"
    instructions_1 = Text(Point(500, 750), inst_1)
    instructions_1.draw(win)

    inst_2 = "Click to guess which is the secret door!"
    instructions_2 = Text(Point(500, 150), inst_2)
    instructions_2.draw(win)

    doors = [door_1, door_2, door_3]

    win_acc = 0
    loss_acc = 0
    user_click = win.getMouse()
    while not button_1.is_clicked(user_click):
        secret = randint(0, 2)
        doors[secret].set_secret(True)
        for door in doors:
            if door.is_clicked(user_click):
                if door.is_secret():
                    door.color_door("green")
                    win_acc += 1
                    win_text.setText(str(win_acc))
                else:
                    door.color_door("red")
                    loss_acc += 1
                    loss_text.setText(str(loss_acc))
            elif door.is_secret():
                door.color_door("green")
        instructions_1.setText("Click anywhere to play again")
        user_click = win.getMouse()
        if button_1.is_clicked(user_click):
            break
        doors[secret].set_secret(False)
        for door in doors:
            door.color_door("saddle brown")
        instructions_1.setText("There is a secret door somewhere")
        user_click = win.getMouse()

    win.close()


if __name__ == '__main__':
    main()

import time

from graphics import GraphWin, Circle, Point, Text, Rectangle, Polygon, Line

def valentine_day():
    width = 800
    length = 800
    win = GraphWin("Valentines Day", width, length)
    p_1 = Point(width / 2, 700)
    p_2 = Point(width / 4, 300)
    p_3 = Point(width / 3, 200)
    p_4 = Point(width / 2, 300)
    p_5 = Point(533, 200)
    p_6 = Point(600, 300)

    heart = Polygon(p_1, p_2, p_3, p_4, p_5, p_6)
    heart.setOutline("black")
    heart.setFill("red")

    arrow = Line(Point(25, 790), Point(300, 550))
    arrow.setOutline("black")
    arrow.setFill("black")
    arrow.draw(win)

    arrow_tip = Polygon(Point(290, 540), Point(310, 560), Point(305, 545))
    arrow_tip.setOutline("black")
    arrow_tip.setFill("black")
    arrow_tip.draw(win)
    heart.draw(win)

    inst_1 = Point(width / 2, length - 400)
    instructions = Text(inst_1, "Happy Valentines Day!")
    instructions.draw(win)

    for i in range(55):
        arrow.move(15, -15)
        arrow_tip.move(15, -15)
        time.sleep(.1)

    inst_2 = Point(width / 2, length - 50)
    instructions_2 = Text(inst_2, "Click anywhere to close")
    instructions_2.draw(win)

    win.getMouse()
    win.close()

valentine_day()
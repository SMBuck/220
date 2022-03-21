import math
from graphics import *
from random import randint
import time

def bumper():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)

    center = Point(300, 500)
    circle_ball = Circle(center, 30)
    circle_ball.setFill('#{}'.format(get_random_color()))
    circle_ball.draw(win)

    center_2 = Point(500, 500)
    circle_ball_2 = Circle(center_2, 30)
    circle_ball_2.setFill('#{}'.format(get_random_color()))
    circle_ball_2.draw(win)

    x_velocity = get_random(8)
    y_velocity = get_random(8)
    x_2_velocity = get_random(8)
    y_2_velocity = get_random(8)

    while True:
        circle_ball.move(x_velocity, y_velocity)
        circle_ball_2.move(x_2_velocity, y_2_velocity)
        if did_collide(circle_ball, circle_ball_2):
            x_velocity = x_velocity * -1
            x_2_velocity = x_2_velocity * -1
            y_velocity = y_velocity * -1
            y_2_velocity = y_2_velocity * -1
        if hit_vertical(circle_ball, win):
            x_velocity = x_velocity * -1
        if hit_vertical(circle_ball_2, win):
            x_2_velocity = x_2_velocity * -1
        if hit_horizontal(circle_ball, win):
            y_velocity = y_velocity * -1
        if hit_horizontal(circle_ball_2, win):
            y_2_velocity = y_2_velocity * -1
        time.sleep(.02)



def get_random(move_amount):
    random_num = randint(-move_amount, move_amount)
    return random_num


def did_collide(circle_ball, circle_ball_2):
    center_x_value = (circle_ball_2.getCenter().getX() - circle_ball.getCenter().getX()) ** 2
    center_y_value = (circle_ball_2.getCenter().getY() - circle_ball.getCenter().getY()) ** 2
    center_distance = math.sqrt(center_x_value + center_y_value)
    radius_1 = circle_ball.getRadius()
    radius_2 = circle_ball_2.getRadius()
    radius_sum = radius_2 + radius_1
    if center_distance <= radius_sum:
        return True
    return False


def hit_vertical(circle_ball, win):
    if (circle_ball.getCenter().getX() + circle_ball.getRadius()) >= win.getWidth():
        return True
    if (circle_ball.getCenter().getX() - circle_ball.getRadius()) <= 0:
        return True
    return False


def hit_horizontal(circle_ball, win):
    if (circle_ball.getCenter().getY() + circle_ball.getRadius()) >= win.getHeight():
        return True
    if (circle_ball.getCenter().getY() - circle_ball.getRadius()) <= 0:
        return True
    return False


def get_random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return ('{:02X}' * 3).format(r, g, b)







if __name__ == '__main__':
    pass
    bumper()
    # print(get_random(10))

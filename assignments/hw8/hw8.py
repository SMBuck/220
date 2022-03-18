"""
Name: <Sam Marshall Buck>
<hw8>.py

Problem: <We used a list for an input and had to alter that list in different ways,
and combining the list to get the desired output as well as using if statements and bools.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.

"""
import math
from graphics import *


def add_ten(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10


def square_each(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2


def sum_list(nums):
    my_sum = 0
    for i in nums[::]:
        my_sum = i + my_sum
    return my_sum


def to_numbers(nums):
    for i in range(len(nums)):
        nums[i] = float(nums[i])


def sum_of_squares(nums):
    my_new_list = []
    for index in nums[::]:
        splitter = index.split(",")
        to_numbers(splitter)
        square_each(splitter)
        numbers = list(splitter)
        total = [sum_list(numbers)]
        my_new_list = my_new_list + total
    return my_new_list


def starter(weight, wins):
    if 150 <= weight < 160 and wins >= 5:
        return True
    if weight > 199 or wins > 20:
        return True
    return False


def leap_year(year):
    if (year % 400 == 0 or year % 100 != 0) and year % 4 == 0:
        return True
    return False


def circle_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    center = win.getMouse()
    circumference_point = win.getMouse()
    radius = math.sqrt(
        (center.getX() - circumference_point.getX()) ** 2 + (center.getY() - circumference_point.getY()) ** 2)
    circle_one = Circle(center, radius)
    circle_one.setFill("light blue")
    circle_one.draw(win)

    center = win.getMouse()
    circumference_point = win.getMouse()
    radius = math.sqrt(
        (center.getX() - circumference_point.getX()) ** 2 + (center.getY() - circumference_point.getY()) ** 2)
    circle_two = Circle(center, radius)
    circle_two.setFill("light green")
    circle_two.draw(win)

    inst_1 = "Click Anywhere to Close Window"
    instructions_1 = Text(Point(5, 1), inst_1)
    instructions_1.draw(win)

    win.getMouse()
    win.close()


def did_overlap(circle_one, circle_two):
    if circle_one == circle_two:
        return True
    return False



if __name__ == '__main__':
    pass
    # nums = ["3, 7.2, 9", "2, 4, 6", "3, 6.6, 9"]
    # nums = [1, 2, 3, 4, 5]
    # weight = 190
    # weight = 200
    # wins = 19
    # wins = 21
    # year = 2000
    # year = 1900
    # add_ten(nums)
    # square_each(nums)
    # sum_list(nums)
    # to_numbers(nums)
    # print(sum_of_squares(nums))
    # starter(weight, wins)
    # leap_year(year)
    # circle_overlap()
    # did_overlap()

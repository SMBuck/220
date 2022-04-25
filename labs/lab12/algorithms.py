from graphics import *


def read_data(file_name):
    reading = open(file_name, "r")
    first_list = reading.read().replace('\n', " ").split(" ")
    my_list = []
    i = 0
    while i < len(first_list):
        my_list.append(eval(first_list[i]))
        i += 1
    return my_list


def is_in_linear(search_val, values):
    i = 0
    while i < len(values):
        if search_val == values[i]:
            return True
        i += 1
    return False


def is_in_binary(search_val, values):
    left_index = 0
    right_index = len(values) - 1
    while left_index <= right_index:
        middle = (left_index + right_index) // 2
        if values[middle] < search_val:
            left_index = middle + 1
        elif values[middle] > search_val:
            right_index = middle - 1
        else:
            return True
    return False


def selection_sort(values):
    for i in range(len(values)):
        index = i
        for j in range(i + 1, len(values)):
            if values[index] > values[j]:
                index = j
        values[i], values[index] = values[index], values[i]


def calc_area(rect):
    x1 = rect.getP1().getX()
    x2 = rect.getP2().getX()
    y1 = rect.getP1().getY()
    y2 = rect.getP2().getY()
    length = abs(x1 - x2)
    width = abs(y1 - y2)
    area = length * width
    return area


def rect_sort(rectangles):
    my_list = []
    for rectangle in rectangles:
        area = calc_area(rectangle)
        my_list.append(area)

    for i in range(len(rectangles)):
        minimum = i
        for j in range(i, len(my_list)):
            if my_list[minimum] > my_list[j]:
                minimum = j
        rectangles[i], rectangles[minimum] = rectangles[minimum], rectangles[i]
        my_list[i], my_list[minimum] = my_list[minimum], my_list[i]


if __name__ == "__main__":
    # values = [58, 32, 3, 6, 1, 39, 69, 70, 4, -6]
    # selection_sort(values)
    # print(values)

    rectangles = [Rectangle(Point(5, 6), Point(7, 8)), Rectangle(Point(1, 3), Point(2, 4))]
    rect_sort(rectangles)
    print(rectangles)

    # file_name = "data_sorted.txt"
    # print(read_data(file_name))
    # values = read_data(file_name)
    # search_val = 111
    # print(is_in_linear(search_val, values))

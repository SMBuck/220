from algorithms import *


def trade_alert(file_name):
    in_file = open(file_name, "r")
    my_list = []
    line = in_file.read().split(" ")

    for i in line:
        my_list.append(float(i))
    for i in range(len(my_list)):
        if my_list[i] > 830:
            print("WARNING exceeds 830! at ", i + 1, "seconds. \n")
        elif my_list[i] == 500:
            print("ALERT equals 500! at ", i + 1, "seconds. \n")
    in_file.close()


if __name__ == '__main__':
    trade_alert("trades.txt")
    values = [58, 32, 3, 6, 1, 39, 69, 70, 4, -6]
    selection_sort(values)
    print(values)
    rectangles = [Rectangle(Point(5, 6), Point(7, 8)), Rectangle(Point(1, 3), Point(2, 4))]
    rect_sort(rectangles)
    print(rectangles)
    file_name = "data_sorted.txt"
    print(read_data(file_name))
    values = read_data(file_name)
    search_val = 111
    print(is_in_linear(search_val, values))

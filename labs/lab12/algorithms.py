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


if __name__ == "__main__":
    pass
    # file_name = "data_sorted.txt"
    # print(read_data(file_name))
    # values = read_data(file_name)
    # search_val = 111
    # print(is_in_linear(search_val, values))

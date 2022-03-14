def weighted_average(in_file_name, out_file_name):
    in_file = open(in_file_name, "r")
    out_file = open(out_file_name, "w")
    class_accumulator = 0
    student_accumulator = 0
    for line in in_file.readlines():
        lines = line.split(":")
        names = lines[0]
        numbers = lines[1].split()
        w_var = numbers[0::2]
        g_var = numbers[1::2]
        my_accumulator = 0
        my_sum = 0
        for i in range(len(w_var)):
            my_equation = int(w_var[i]) * int(g_var[i])
            my_accumulator = my_accumulator + my_equation
            my_sum = int(w_var[i]) + my_sum
        my_division = my_accumulator / 100

        if my_sum == 100:
            print("{}'s average: {}".format(names, my_division), file=out_file)
            class_accumulator = my_division + class_accumulator
            student_accumulator = student_accumulator + 1
        elif my_sum < 100:
            print("{}'s average: Error: The weights are less than 100.".format(names), file=out_file)
        else:
            print("{}'s average: Error: The weights are more than 100.".format(names), file=out_file)
    my_total = class_accumulator / student_accumulator
    print("Class average: {}".format(my_total), file=out_file)

    in_file.close()
    out_file.close()


if __name__ == "__main__":
    weighted_average("grades.txt", "avg.txt")

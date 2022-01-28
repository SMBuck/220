"""
Name: <Sam Marshall Buck>
<hw2>.py

Problem:
<This assignment was more difficult because we had to figure out the problem while using loops.
I only used the math library once for one of the problems and that one was the easiest.
The nested loop for the multiplication table was tricky and the power function was as well,
they took me the longest to figure out. >

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""
import math


def sum_of_threes():
    user_input = eval(input("What is the upper bound?: "))
    my_sum = 0
    for i in range(3, user_input + 1, 3):
        my_sum = my_sum + i
    print("sum of threes is", my_sum)



def multiplication_table():
    for i in range(1, 11):
        for j in range(1, 11):
            print(i*j, end="\t")
        print("\n")



def triangle_area():
    side_a = eval(input("Enter side a length: "))
    side_b = eval(input("Enter side b length: "))
    side_c = eval(input("Enter side c length: "))
    all_sides = side_a + side_b + side_c
    total = all_sides / 2
    area = total * (total-side_a) * (total-side_b) * (total-side_c)
    total_area = math.sqrt(area)
    print("area is", total_area)


def sum_squares():
    lower_range = eval(input("Enter lower range: "))
    upper_range = eval(input("Enter upper range: "))
    my_sum = 0
    for i in range(lower_range, upper_range + 1):
        my_sum = my_sum + (i * i)
    print(my_sum)


def power():
    base = eval(input("Enter base:"))
    exponent = eval(input("Enter exponent:"))
    my_total = 1
    for _ in range(exponent):
        my_total = my_total * base
    print(base, "^", exponent, "=", my_total)




if __name__ == '__main__':
    pass

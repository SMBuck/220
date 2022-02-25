"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""
import math


def cash_converter():
    user_input = eval(input("enter and integer: "))
    value = "That is ${:.2f}".format(user_input)
    print(value.rstrip())


def encode():
    user_input = input("enter a message: ")
    key = eval(input("enter a key: "))
    for letter in user_input:
        secret = ord(letter)
        secret_enc = secret + key
        uncovered_enc = chr(secret_enc)
        print(uncovered_enc, end=" ")


def sphere_area(radius):
    area = 4 * math.pi * radius ** 2
    return area


def sphere_volume(radius):
    volume = (4 * math.pi * radius ** 3) / 3
    return volume


def sum_n(number):
    my_sum = 0
    for num in range(1, number + 1):
        my_sum = num + my_sum
    return my_sum


def sum_n_cubes(number):
    my_sum = 0
    for num in range(1, number + 1):
        cubed = num ** 3
        my_sum = my_sum + cubed
    return my_sum


def encode_better():
    message = input("enter a message: ")
    key = input("enter a key: ")
    # for letters in message:
    #     secrets_1 = ord(letters.upper())
    #     secrets_2 = ord(letters)
    #     cipher_1 = (secrets_1 % 32) - 1 # upper case letter changed to 0-25 for ace
    #     cipher_2 = (secrets_2 % 32) + 31
    #     cipher_shift = cipher_2 + cipher_1
    #     cipher_new = chr(cipher_shift)
    #     print(cipher_2, end=" ")
    print(cipher_change)








if __name__ == '__main__':
    # cash_converter()
    encode()
    # res = sphere_area(13)
    # print(res)
    # res = sphere_volume(13)
    # print(res)
    # res = sum_n(100)
    # print(res)
    # res = sum_n_cubes(13)
    # print(res)
    # encode_better()
    pass

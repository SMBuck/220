from random import randint


def find_and_remove_first(my_list, value):
    i = 0
    while i < len(my_list):
        if my_list[i] == value:
            my_list.pop(i)
            my_list.insert(i, "Marshall")
            i = len(my_list)
        else:
            i += 1


def good_input():
    user_input = eval(input("Enter value between 1-10: "))
    while user_input > 10 or user_input < 1:
        print("Value is out of Range")
        user_input = eval(input("Enter value between 1-10:"))
    print("Good Input")


def num_digits():
    user_input = eval(input("Enter a positive integer: "))
    while user_input > 0:
        count = 0
        while user_input > 0:
            user_input = user_input // 10
            count += 1
        print(count, "is how many digits are in the number")
        user_input = eval(input("Enter a positive integer:"))


def hi_lo_game():
    number = randint(1, 100)
    guesses = 0
    winner = False
    while not winner and guesses <= 7:
        user_input = eval(input("Guess a number between 1-100:"))
        guesses += 1
        if user_input == number:
            print("Congrats you won in {} guesses!".format(guesses))
            winner = True
        elif guesses >= 7:
            print("Oh no sorry! You loose! The number was {}".format(number))
            winner = True
        elif user_input < number:
            print("Too Low!")
        else:
            print("Too High!")


if __name__ == "__main__":
    # my_list = [100, 2, 35, 49, 500, 61, 79, 800]
    # # my_list = [100, 2, 35, 49, 34, 61, 79, 800]
    # value = 500
    # find_and_remove_first(my_list, value)
    # print(my_list)
    # good_input()
    num_digits()
    # hi_lo_game()

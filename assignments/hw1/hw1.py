"""
Name: <Sam Marshall Buck >
<hw1>.py

Problem: <The computer is able to solve math problems for us, but it takes time to
figure out how to write out the problem correctly and logically, so
the program can solve it for us like the exercises we did in the HW.
Once the problem is solved then the computer is
able to convert/complete the arithmatic required to get your answer. >

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.

"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)

def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Volume =", volume)


def shooting_percentage():
    totalshots = eval(input("Enter the player's total shots: "))
    shotsmade = eval(input("Enter how many shots the player made: "))
    shootingpercentage = shotsmade / totalshots * 100
    print("Shooting Percentage: ", shootingpercentage, "%")


def coffee():
    poundsofcoffee = eval(input("How many pounds of coffee would you like? "))
    totalprice = 10.50 * poundsofcoffee + 0.86 * poundsofcoffee + 1.50
    print("Your total is: ", totalprice)


def kilometers_to_miles():
    kilometerstraveled = eval(input("How many kilometers did you travel? "))
    mileconversion = kilometerstraveled / 1.61
    print("That's ", mileconversion, "miles!")


if __name__ == '__main__':
    pass

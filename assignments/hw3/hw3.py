"""
Name: <Sam Marshall Buck>
<hw3>.py

Problem: <This assignment was detailed in making us use an accumulator
for most of the problems but using for loops as well.I figured it out mostly but
the last problem i got close but could not figure it out>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is my own work, but I discussed it with: <Bradley>
"""



def average():
    total_grades = eval(input("how many grades will you enter? "))
    my_sum = 0
    for _ in range(1, total_grades + 1):
        grades = eval(input("Enter grade: "))
        my_sum = my_sum + grades
    mean_grade = my_sum / total_grades
    print("average is", mean_grade)


def tip_jar():
    my_sum = 0
    for _ in range(1, 6):
        donate = eval(input("how much would you like to donate? "))
        my_sum = my_sum + donate
    print("total tips: ", my_sum)


def newton():
    variable = eval(input("what number do you want to square root? "))
    improve = eval(input("how many times should we improve the approximation? "))
    guess = variable
    for _ in range(1, improve + 1):
        guess = (guess + variable/guess)/2
    print("the square root is approximately", guess)


def sequence():
    user_input = eval(input("how many terms would you like? "))
    for i in range(1, user_input + 1):
        print((i - 1) + (i % 2), end=" ")


def pi():
    user_input = eval(input("how many terms in the series? "))
    product = 1
    for i in range(1, user_input + 1):
        product = (2 * i) / (2 * i - 1) * (2 * i) / (2 * i + 1)
        final_product = product * product
        answer = final_product * 2
        print(answer)






if __name__ == '__main__':
    pass

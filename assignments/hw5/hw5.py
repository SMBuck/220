"""
Name: <Sam Buck>
<hw5>.py

Problem: <This assignment was about learning how to use the index of lists
to piece together functions. I also had to figure out how to get them to work within a loop.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.>
"""


def name_reverse():
    user_input = input("enter a name (first last): ")
    name_order = user_input.split()
    first_name = name_order[0]
    last_name = name_order[1]
    print(last_name, first_name, sep=", ")


def company_name():
    user_input = input("enter a domain: ")
    domain_split = user_input.split(".")
    domain_name = domain_split[1]
    print(domain_name)


def initials():
    user_input = eval(input("how many students are in the class? "))
    for i in range(1, user_input + 1):
        student_names = input("What is the name of student " + str(i) + "?")
        student_first, student_last = student_names.split()
        student_initial = student_first[0] + str(student_last[0])
        print(student_initial)


def names():
    user_input = input("enter a list of names: ")
    name_list = user_input.split(" ")
    for initial in name_list:
        initial = initial[0]
        print(initial, sep="", end="")


def thirds():
    user_input = eval(input("enter the number of sentences: "))
    fragment = ""
    for i in range(1, user_input + 1):
        sentences = input("enter sentence " + str(i) + ": ")
        length = len(sentences)
        fragment = fragment + sentences[0:length:3] + "\n"
    print(fragment)


def word_average():
    user_input = input("enter a sentence: ")
    words = user_input.split(" ")
    length = len(words)
    letters = "".join(words)
    length_2 = len(letters)
    letter_average = length_2 / length
    print(letter_average)


def pig_latin():
    user_input = input("enter a sentence to convert to pig latin: ")
    words = user_input.split()
    pig = "ay"
    for word in words:
        latin = word[1:] + word[0]
        pig_l = latin + pig
        latin_pig = pig_l.lower()
        final = latin_pig.rstrip()
        print(final, end=" ")


if __name__ == '__main__':
    # name_reverse()
    # company_name()
    # initials()
    # names()
    # thirds()
    # word_average()
    pig_latin()
    pass

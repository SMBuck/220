"""
Name: <Sam Marshall Buck>
<hw7>.py

Problem: <This assignment was difficult to say the least, we had to use files and combine
them with encryption to get the desired outputs.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Bradly>
"""
import encryption


def number_words(in_file_name, out_file_name):
    in_file = open(in_file_name, "r")
    out_file = open(out_file_name, "w")
    message = in_file.read()
    new_message = message.replace("\n", " ")
    new_words = new_message.split()
    length = len(new_words)
    for i in range(length):
        form = i + 1
        new = new_words[i]
        print(form, new, file=out_file)


def hourly_wages(in_file_name, out_file_name):
    in_file = open(in_file_name, "r")
    out_file = open(out_file_name, "w")
    for line in in_file.readlines():
        message = line.split()
        form = float(message[2]) + 1.65
        weekly = form * float(message[3])
        formatting = "{0:.2f}".format(weekly)
        new_list = message[0] + " " + message[1]
        final_pay = new_list + " " + str(formatting)
        print(final_pay, file=out_file)


def calc_check_sum(isbn):
    isbn = isbn.replace("-", "")
    total = 0
    for i in range(10):
        total = total + int(isbn[i]) * (10 - i)
    return total


def send_message(file_name, friend_name):
    first_file = open(file_name, "r")
    content = first_file.read()
    updated = content.rstrip()
    friend_file = friend_name + ".txt"
    output_file = open(friend_file, "w")
    print(updated, file=output_file)


def encode(message, key):
    for letter in message:
        secret = ord(letter)
        secret_enc = secret + key
        uncovered_enc = chr(secret_enc)
        return uncovered_enc


def send_safe_message(file_name, friend_name, key):
    first_file = open(file_name, "r")
    content = first_file.read()
    message = content.rstrip()
    friend_file = friend_name + ".txt"
    output_file = open(friend_file, "w")
    words = ""
    for letters in message:
        encrypt = encryption.encode(letters, key)
        words = words + encrypt
        print(words, file=output_file)


def send_uncrackable_message(file_name, friend_name, pad_file_name):
    first_file = open(file_name, "r")
    content = first_file.readlines()
    second_file = open(pad_file_name, "r")
    key_content = second_file.read()
    friend_file = friend_name + ".txt"
    output_file = open(friend_file, "w")
    words = ""
    for letters in content:
        encrypt = encryption.encode_better(letters, key_content)
        words = words + encrypt
        print(words, file=output_file)


if __name__ == '__main__':
    pass
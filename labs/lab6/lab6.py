import math
from graphics import *


def vigenere():
    width = 500
    length = 500
    win = GraphWin("Vigenere", width, length)
    win.setBackground("white")

    msg_code = "Message to code"
    msg_code_inst = Text(Point(100, 70), msg_code)
    msg_code_inst.draw(win)
    msg_input = Entry(Point(300, 70), 25)
    msg_input.draw(win)

    key_code = "Enter a keyword"
    key_code_inst = Text(Point(100, 110), key_code)
    key_code_inst.draw(win)
    key_input = Entry(Point(300, 110), 15)
    key_input.draw(win)

    shape = Rectangle(Point(200, 140), Point(300, 200))
    shape_msg = "Execute"
    shape_inst = Text(Point(250, 170), shape_msg)
    shape_inst.draw(win)
    shape.draw(win)

    win.getMouse()
    msg_entry = msg_input.getText()
    msg_entry = msg_entry.replace(" ", "").upper()
    key_entry = key_input.getText()
    key_entry = key_entry.replace(" ", "").upper()
    msg_length = len(msg_entry)
    length_2 = len(key_entry)
    my_string = ""
    for i in range(msg_length):
        letters = msg_entry[i]
        cipher = i % length_2
        cipher_message = key_entry[cipher]
        encrypt_1 = ord(letters) - 65
        encrypt_2 = ord(cipher_message) - 65
        full_encrypt = encrypt_1 + encrypt_2
        unknown = (full_encrypt % 26) + 65
        discovered = chr(unknown)
        my_string = my_string + discovered

    shape.undraw()
    shape_inst.undraw()

    res_1 = "Resulting Message \n"
    shape_inst.setText(res_1 + my_string)
    shape_inst.draw(win)

    inst_1 = "Click Anywhere to Close Window"
    instructions_1 = Text(Point(width / 2, length - 50), inst_1)
    instructions_1.draw(win)

    win.getMouse()
    win.close()


vigenere()

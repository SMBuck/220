# shape and text are the same and the extra variable secret is a boolean. self.secret = false
from graphics import *


class Door:
    def __init__(self, shape, label):
        self.shape = shape
        self.text = Text(shape.getCenter(), label)
        self.secret = False

    def get_label(self):
        return self.text.getText()

    def set_label(self, label):
        self.text.setText(label)

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, point):
        x_range = (self.shape.getP1().getX() <= point.getX() <= self.shape.getP2().getX())
        y_range = (self.shape.getP1().getY() <= point.getY() <= self.shape.getP2().getY())
        return x_range and y_range

    def color_door(self, color):
        self.shape.setFill(color)

    def open(self, color, label):
        self.shape.setFill(color)
        self.text.setText(label)

    def close(self, color, label):
        self.shape.setFill(color)
        self.text.setText(label)

    def is_secret(self):
        return self.secret

    def set_secret(self, secret):
        self.secret = secret


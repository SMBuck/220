from graphics import *


class Face:
    def __init__(self, window, center, size):
        eye_size = 0.15 * size
        eye_off = size / 3.0
        mouth_size = 0.8 * size
        mouth_off = size / 2.0
        self.window = window
        self.head = Circle(center, size)
        self.head.draw(window)
        self.left_eye = Circle(center, eye_size)
        self.left_eye.move(-eye_off, -eye_off)
        self.right_eye = Circle(center, eye_size)
        self.right_eye.move(eye_off, -eye_off)
        self.left_eye.draw(window)
        self.right_eye.draw(window)
        point_1 = center.clone()
        point_1.move(-mouth_size / 2, mouth_off)
        point_2 = center.clone()
        point_2.move(mouth_size / 2, mouth_off)
        self.mouth = Line(point_1, point_2)
        self.mouth.draw(window)

    def smile(self, window, center, size):
        self.mouth.undraw()
        mouth_size = 0.8 * size
        mouth_off = size / 2.0
        point_1 = center.clone()
        point_1.move(-mouth_size / 2, mouth_off)
        point_2 = center.clone()
        point_2.move(mouth_size / 2, mouth_off)
        point_3 = center.clone()
        point_3.move(mouth_size, mouth_off)
        self.mouth = Polygon(point_1, point_2, point_3)
        self.mouth.draw(window)

    def shock(self, window, center, size):
        self.mouth.undraw()
        self.mouth = self.left_eye
        mouth_size = 0.8 * size
        mouth_off = size / 2.0
        self.mouth.move(mouth_size, mouth_off)

    def wink(self):
        self.left_eye.undraw()

import math
class Sphere:

    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def surface_area(self):
        return 4 * math.pi * (self.radius ** 2)

    def volume(self):
        numerator = 4 * math.pi * (self.radius ** 3)
        return numerator / 3

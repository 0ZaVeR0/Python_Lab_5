from shapes3d import Shape3d
from memory import remember


class Cube(Shape3d):
    @remember
    def __init__(self, side: int):
        Shape3d.__init__(self, side, side, side)

    def __str__(self):
        return f"Class: Cube. Side: {self.width}."

    def __mul__(self, other):
        return Cube(self.width * other.width)
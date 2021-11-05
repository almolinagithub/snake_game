
from turtle import *

class PointWriter(Turtle):
    def __init__(self):
        super().__init__()
        self.clear()

    def write_points(self,pts):
        self.pts = pts
        self.color("white")
        self.hideturtle()
        self.write(pts, move=False, align='center', font="Arial")


from turtle import *

class PointWriter(Turtle):
    def __init__(self):
        super().__init__()
        self.clear()

    def write_points(self):
        self.pts = pts
        self.color("white")
        self.write(6, move=False, align='center', font="Arial", fontaname=12, fonttype="normal")

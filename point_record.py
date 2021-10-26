import turtle
from turtle import *

initial_points = 0

class Points(Turtle):
    def __init__(self):
        super().__init__()
        self.write_points()

    def write_points(self):
        turtle.write(initial_points)
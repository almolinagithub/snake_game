from turtle import *


class Points(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.fillcolor('white')

    def write_points(self, points):
        self.begin_fill()
        self.penup()
        self.goto(0, 270)
        self.pendown()
        self.write(points)
        self.end_fill()

    def clear(self):
        self.clear()

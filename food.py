import random
from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.refresh()

    def refresh(self):
        x = randint(-300, 300)
        y = randint(-300, 300)
        self.goto(x, y)



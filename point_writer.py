
from turtle import *


class PointWriter(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.clear()
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.color("white")
        self.write(f" SCORE {self.score}", move=False, align="center", font=("Verdana", 20, "normal"))

    def increase_score(self):
        self.score += 1
        self.write(f" SCORE {self.score}", move=False, align="center", font=("Verdana", 20, "normal"))

    def game_over(self):
         self.write(f"Game Over! Final points = {self.score}", move=False, align="center", font=("Verdana", 20, "normal"))



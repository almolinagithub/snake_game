# TODO 0: CREATE THE SNAKE BODY
import turtle
from turtle import  Turtle, Screen

STILL_PLAYING = True

screen = Screen()
screen.setup(width=600, height=600)
screen.title(titlestring= "My snake game")
screen.bgcolor("black")
turtle = Turtle()
speed = 1

turtle.shape("square")
turtle.color("white")


def move_fw():
    turtle.forward(40)

# TODO 1: MOVE THE SNAKE ALWAYS FORWARD


while STILL_PLAYING:
    turtle.penup()
    turtle.speed(speed)
    turtle.forward(40)


# TODO 2: CONTROL THE SNAKE WITH ARROWS

# TODO 3: DETECT COLLISION WITH FOOD

# TODO 4: CREATE A SCOREBOARD

# TODO 5: DETECT COLLISION WITH THE WALL

# TODO 6: COLLISION WITH THE TAIL


screen.exitonclick()

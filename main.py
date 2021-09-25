# TODO 0: CREATE THE SNAKE BODY
import turtle
from turtle import Turtle, Screen

STILL_PLAYING = True
postions = [(0, 0), (-20, 0), (-40, 0)]
segments = []

screen = Screen()
screen.setup(width=600, height=600)
screen.title(titlestring= "My snake game")
screen.bgcolor("black")

for pos in postions:
    new_segment = Turtle()
    new_segment.shape("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(pos)
    segments.append(new_segment)

while STILL_PLAYING:
    for seg in segments:
        seg.pendown()
        seg.stamp()
        seg.speed(100)
        seg.forward(10)



# TODO 1: MOVE THE SNAKE ALWAYS FORWARD

screen.exitonclick()




# TODO 2: CONTROL THE SNAKE WITH ARROWS





# TODO 3: DETECT COLLISION WITH FOOD

# TODO 4: CREATE A SCOREBOARD

# TODO 5: DETECT COLLISION WITH THE WALL

# TODO 6: COLLISION WITH THE TAIL




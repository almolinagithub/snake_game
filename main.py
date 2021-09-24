# TODO 0: CREATE THE SNAKE BODY
import turtle
from turtle import  Turtle, Screen

STILL_PLAYING = True
segment_body = []
segment_length = 3

screen = Screen()
screen.setup(width=600, height=600)
screen.title(titlestring= "My snake game")
screen.bgcolor("black")
segment = Turtle()

segment.penup()
speed = 1
x_pos = 0
y_pos = 0
segment.setpos(x_pos, y_pos)


for _ in range(segment_length):
    segment.clone()
    segment.shape("square")
    segment.color("white")
    segment.setpos(x_pos, y_pos)
    segment_body.append(segment)
    print(segment)
    x_pos -= 20

# TODO 1: MOVE THE SNAKE ALWAYS FORWARD

screen.exitonclick()




# TODO 2: CONTROL THE SNAKE WITH ARROWS





# TODO 3: DETECT COLLISION WITH FOOD

# TODO 4: CREATE A SCOREBOARD

# TODO 5: DETECT COLLISION WITH THE WALL

# TODO 6: COLLISION WITH THE TAIL




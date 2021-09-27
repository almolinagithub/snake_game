# TODO 0: CREATE THE SNAKE BODY

import time
from turtle import Turtle, Screen

STILL_PLAYING = True
x = 0
y = 0
positions = [(x, y), (x - 20, y), (x - 40, y)]
segments = []

screen = Screen()
screen.setup(width=600, height=600)
screen.title(titlestring="My snake game")
screen.bgcolor("black")
screen.tracer(0)

for pos in positions:
    new_segment = Turtle()
    new_segment.shape("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(pos)
    segments.append(new_segment)

#TODO 1: MOVE THE SNAKE ALWAYS FORWARD

while STILL_PLAYING:
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(segments)-1, 0, -1):
        new_x = segments[seg_num-1].xcor()
        new_y = segments[seg_num-1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)




screen.exitonclick()




# TODO 2: CONTROL THE SNAKE WITH ARROWS





# TODO 3: DETECT COLLISION WITH FOOD

# TODO 4: CREATE A SCOREBOARD

# TODO 5: DETECT COLLISION WITH THE WALL

# TODO 6: COLLISION WITH THE TAIL




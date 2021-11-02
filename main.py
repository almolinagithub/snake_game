# TODO 0: CREATE THE SNAKE BODY
import food
import time
import turtle
import random

import point_record
from point_record import *
from point_record import  *

from snake import Snake
from food import *
from turtle import Screen


STILL_PLAYING = True

snake = Snake()
points = Points()
punti = 0

apple = Food()
screen = Screen()
screen.setup(width=600, height=600)
screen.title(titlestring="My snake game")
screen.bgcolor("black")
screen.tracer(0)
point_writer = point_record.Points()

#TODO 1: MOVE THE SNAKE ALWAYS FORWARD




while STILL_PLAYING:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    turtle.onkey(snake.turn_right, "d")
    turtle.onkey(snake.turn_left, "a")
    if snake.head.distance(apple) < 15:
        apple.refresh()
        point_writer.write_points()


    turtle.listen()


screen.exitonclick()




# TODO 2: CONTROL THE SNAKE WITH ARROWS





# TODO 3: DETECT COLLISION WITH FOOD

# TODO 4: CREATE A SCOREBOARD

# TODO 5: DETECT COLLISION WITH THE WALL

# TODO 6: COLLISION WITH THE TAIL




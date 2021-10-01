# TODO 0: CREATE THE SNAKE BODY

import time
import turtle
import food

from snake import Snake
from food import Apple
from turtle import Turtle, Screen


STILL_PLAYING = True

snake = Snake()
apple = Apple()
screen = Screen()
screen.setup(width=600, height=600)
screen.title(titlestring="My snake game")
screen.bgcolor("black")
screen.tracer(0)


#TODO 1: MOVE THE SNAKE ALWAYS FORWARD

while STILL_PLAYING:
    screen.update()
    time.sleep(0.1)


    snake.move_snake()
    turtle.onkey(snake.turn_right, "d")
    turtle.onkey(snake.turn_left, "a")

    turtle.listen()




screen.exitonclick()




# TODO 2: CONTROL THE SNAKE WITH ARROWS





# TODO 3: DETECT COLLISION WITH FOOD

# TODO 4: CREATE A SCOREBOARD

# TODO 5: DETECT COLLISION WITH THE WALL

# TODO 6: COLLISION WITH THE TAIL




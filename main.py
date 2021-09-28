# TODO 0: CREATE THE SNAKE BODY

import time
from snake import Snake
from turtle import Turtle, Screen


STILL_PLAYING = True

snake = Snake()
screen = Screen()
screen.setup(width=600, height=600)
screen.title(titlestring="My snake game")
screen.bgcolor("black")
screen.tracer(0)


#TODO 1: MOVE THE SNAKE ALWAYS FORWARD

while STILL_PLAYING:
    screen.update()
    time.sleep(0.1)
    snake.create_snake()





screen.exitonclick()




# TODO 2: CONTROL THE SNAKE WITH ARROWS





# TODO 3: DETECT COLLISION WITH FOOD

# TODO 4: CREATE A SCOREBOARD

# TODO 5: DETECT COLLISION WITH THE WALL

# TODO 6: COLLISION WITH THE TAIL




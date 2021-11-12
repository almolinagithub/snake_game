# TODO 0: CREATE THE SNAKE BODY
import food
import time
import turtle
from point_writer import *
from snake import Snake
from food import *
from turtle import Screen

STILL_PLAYING = True

snake = Snake()
initial_points = 0


apple = Food()
screen = Screen()
screen.setup(width=600, height=600)
screen.title(titlestring="My snake game")
screen.bgcolor("black")
screen.tracer(0)
point_writer = PointWriter()



points = 0
while STILL_PLAYING:

    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    turtle.onkey(snake.turn_right, "d")
    turtle.onkey(snake.turn_left, "a")

    if snake.head.distance(apple) < 15:
        apple.refresh()
        snake.elongate_snake()
        points += 1
        point_writer.clear()
        point_writer.increase_score()
        print(points)

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        point_writer.clear()
        point_writer.game_over()
        STILL_PLAYING = False

    turtle.listen()


screen.exitonclick()

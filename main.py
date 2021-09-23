# TODO 0: CREATE THE SNAKE BODY
import turtle
from turtle import  Turtle, Screen

STILL_PLAYING = True
turtle_body = []
turtle_lenght = 3

screen = Screen()
screen.setup(width=600, height=600)
screen.title(titlestring= "My snake game")
screen.bgcolor("black")
turtle = Turtle()
turtle.penup()
speed = 1
x_pos = 0
y_pos = 0
turtle.setpos(x_pos, y_pos)


for _ in range(turtle_lenght):
    turtle.shape("square")
    turtle.color("white")
    turtle.setpos(x_pos - 20, y_pos)
    turtle_body.append(turtle)
    print(turtle)

# TODO 1: MOVE THE SNAKE ALWAYS FORWARD

screen.exitonclick()




# TODO 2: CONTROL THE SNAKE WITH ARROWS





# TODO 3: DETECT COLLISION WITH FOOD

# TODO 4: CREATE A SCOREBOARD

# TODO 5: DETECT COLLISION WITH THE WALL

# TODO 6: COLLISION WITH THE TAIL




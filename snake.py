from turtle import Turtle

x = 0
y = 0
STARTING_POSITIONS = [(x, y), (x - 20, y), (x - 40, y)]


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            new_segment = Turtle()
            new_segment.shape("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(pos)
            self.segments.append(new_segment)

    def move_snake(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(30)



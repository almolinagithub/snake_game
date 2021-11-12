from turtle import Turtle

x = 0
y = 0
STARTING_POSITIONS = [(x, y), (x+20, y), (x+40,y)]


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.segment = self.segments[1]

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            self.add_segment()


    def move_snake(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)

    def turn_right(self):
        self.head.right(90)
        self.add_segment()

    def turn_left(self):
        self.head.left(90)

    def add_segment(self):
        new_segment = Turtle()
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        self.segments.append(new_segment)

    def elongate_snake(self):
        self.add_segment()




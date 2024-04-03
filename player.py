from turtle import Turtle
MOVE_FORWARD = 10


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("red")
        self.penup()
        self.setheading(90)
        self.goto(x=0, y=-280)

    def move_up(self):
        self.forward(MOVE_FORWARD)

    def start_point(self):
        self.goto(0, -280)
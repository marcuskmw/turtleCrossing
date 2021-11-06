from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.color("green")
        self.goto(STARTING_POSITION)
        self.showturtle()

    def move_up(self):
        if self.ycor() < FINISH_LINE_Y:
            self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)
        else:
            self.goto(STARTING_POSITION)
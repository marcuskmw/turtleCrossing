from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        # self.hideturtle()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.color("green")
        self.go_to_start()

    def move_up(self):
        # if self.ycor() < FINISH_LINE_Y:
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)
        # else:
        #     self.goto(STARTING_POSITION)


    def reset(self) :
       self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        return self.ycor() > FINISH_LINE_Y

    def go_to_start(self):
        self.goto(STARTING_POSITION)
from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)
        self.color('green')

    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def check_finish_line(self):
        return self.ycor() == FINISH_LINE_Y

    def reset_position(self):
        self.penup()
        self.goto(STARTING_POSITION)

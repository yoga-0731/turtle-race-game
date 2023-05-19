from turtle import Turtle
FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-280, 260)
        self.level = 0
        self.hideturtle()
        self.print_level()

    def print_level(self):
        self.clear()
        self.write(f"LEVEL: {self.level}", font=FONT)

    def print_game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", font=('Courier', 10, 'bold'))

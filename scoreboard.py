from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(x=-280, y=260 )
        self.write(f"Level: {self.level}", font=FONT, align="left")

    def level_up(self):
        self.clear()
        self.level += 1
        self.write(f"Level:{self.level}", font=FONT, align="left")

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.hideturtle()
        self.write("Game Over", font=FONT, align="center")

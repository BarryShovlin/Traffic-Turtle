from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 0
        self.increase_level()

    def increase_level(self):
        self.clear()
        self.goto(-220, 250)
        self.level += 1
        self.write(f"Level: {self.level}", align="center", font=("courier", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align="center", font=("goudy_oldstyle", 80, "bold"))

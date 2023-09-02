from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.display_scoreboard()

    def display_scoreboard(self):
        self.write(arg=f"Score : {self.current_score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER!", move=False, align=ALIGNMENT, font=FONT)

    def score_refresher(self):
        self.current_score += 1
        self.clear()
        self.display_scoreboard()

from turtle import Turtle
ALIGMENT = "center"
FONT = ("Courier", 18, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0, 240)
        self.color("white")
        self.score_num_left = 0
        self.score_num_right = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score\n {self.score_num_left}:{self.score_num_right}", move=False, align=ALIGMENT, font=FONT)

# Da se to nejak sloucit abych mel jen jednu funkci score_point?
    def score_point_left(self):
        self.score_num_left += 1
        self.update_scoreboard()

    def score_point_right(self):
        self.score_num_right += 1
        self.update_scoreboard()

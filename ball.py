from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.center_ball()
        self.game_speed = 0.03
        self.x_move = 5
        self.y_move = 5

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move

        self.setx(new_x)
        self.sety(new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def center_ball(self):
        self.goto(0, 0)
        self.game_speed = 0.03
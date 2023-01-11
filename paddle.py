from turtle import Turtle

MOVE_DISTANCE = 50

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__() #neni nutne tento radek psat
        self.shape("square")
        self.color("white")
        self.penup()
        self.right(90)
        self.turtlesize(1,5)
        self.setposition(position)

    def up(self):
            self.fd(-MOVE_DISTANCE)

    def down(self):
            self.fd(MOVE_DISTANCE)


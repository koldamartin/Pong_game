from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_on = True
while game_on:
    screen.update()
    time.sleep(ball.game_speed)
    ball.move()

    #detect collision with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330:
        ball.bounce_x()
        if ball.game_speed > 0.015:
            ball.game_speed -= 0.005

    #detect collision with l_paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()
        if ball.game_speed > 0.015:
            ball.game_speed -= 0.005

    #detect if it goes outta right bounds
    if ball.xcor() > 380:
        scoreboard.score_point_left()
        ball.center_ball()
        ball.bounce_x()

    #detect if it goes outta left bounds
    if ball.xcor() < -380:
        scoreboard.score_point_right()
        ball.center_ball()
        ball.bounce_x()

screen.exitonclick()
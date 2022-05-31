from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

# Set up the screen
screen = Screen()
screen.title("PONG")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

paddle_r = Paddle(350, 0)
paddle_l = Paddle(-350, 0)

ball = Ball()
score = Score()
screen.listen()

screen.onkey(paddle_r.up, "Up")
screen.onkey(paddle_r.down, "Down")

screen.onkey(paddle_l.up, "w")
screen.onkey(paddle_l.down, "s")

game_is_on = True
level_of_speed = 0.1
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision to wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    # Detect collision with paddles
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 \
            or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_paddle()


    # Detect right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.add_points_to("left")


    # Detect left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        score.add_points_to("right")


screen.exitonclick()

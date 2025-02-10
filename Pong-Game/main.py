from turtle import Screen
from paddles import Paddle
from ball import Ball
import time

# Makes the screen and modifies it.
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

# Makes paddles.
left_paddle = Paddle(-350)
right_paddle = Paddle(350)

# Makes the ball.
ball = Ball()

# Takes user key presses to move paddles.
screen.listen()
screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")
screen.onkeypress(right_paddle.move_up, "a")
screen.onkeypress(right_paddle.move_down, "d")

# Main Game Loop
game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detects the collision with the wall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detects the collision with paddles.
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detects right paddle miss.
    if ball.xcor() > 380:
        ball.reset()

    # Detects left paddle miss.
    if ball.xcor() < -390:
        ball.reset()

# Exits the program with mouse click.
screen.exitonclick()

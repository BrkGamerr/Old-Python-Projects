from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x_move = 10
        self.y_move = 10

    # Moves the ball.
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # Bounces off the wall.
    def bounce_y(self):
        self.y_move *= -1

    # Bounces off the paddle.
    def bounce_x(self):
        self.x_move *= -1

    # Resets the balls position back to center after someone gets point.
    def reset(self):
        self.goto(0, 0)
        self.bounce_x()

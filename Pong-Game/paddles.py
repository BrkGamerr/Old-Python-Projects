from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_coordinate):
        super().__init__()
        self.x = x_coordinate
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setposition(x=self.x, y=0)

    # Moves the paddle up the Y axis.
    def move_up(self):
        self.goto(x=self.x, y=self.ycor() + 20)

    # Move the paddle down the Y axis.
    def move_down(self):
        self.goto(x=self.x, y=self.ycor() - 20)

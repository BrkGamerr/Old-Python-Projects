from turtle import Turtle

# Constants
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setposition(x=0, y=-280)
        self.setheading(90)

    # Moves the turtle up
    def move(self):
        self.forward(MOVE_DISTANCE)

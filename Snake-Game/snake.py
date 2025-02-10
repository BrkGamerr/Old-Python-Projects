from turtle import Turtle

# Constants
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
RIGHT, UP, LEFT, DOWN = 0, 90, 180, 270


class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    # Creates the snake.
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_body_part(position)

    # Adds body part (new square) to snake body.
    def add_body_part(self, position):
        body = Turtle(shape="square")
        body.color("white")
        body.penup()
        body.goto(position)
        self.snake_body.append(body)

    def reset(self):
        for seg in self.snake_body:
            seg.goto(1000, 1000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]

    # Extends the snakes body when it eats the food.
    def extend(self):
        self.add_body_part(self.snake_body[-1].position())

    # Moves the snake.
    def move(self):
        for snake_part in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[snake_part - 1].xcor()
            new_y = self.snake_body[snake_part - 1].ycor()
            self.snake_body[snake_part].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    # Moves the snake right.
    def right(self):
        # If the snake is moving right, it can't go left. (Back through itself)
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    # Moves the snake up.
    def up(self):
        # If the snake is moving down, it can't go up. (Back through itself)
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    # Moves the snake left.
    def left(self):
        # If the snake is moving left, it can't go right. (Back through itself)
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    # Moves the snake down.
    def down(self):
        # If the snake is moving up, it can't go down. (Back through itself)
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

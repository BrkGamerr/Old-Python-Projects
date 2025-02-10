import time
from turtle import Screen
from scoreboard import Scoreboard
from snake import Snake
from food import Food

# Makes the screen, sets it's dimensions and other attributes.
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

# Makes the snake and food object.
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Game takes keyboard inputs to move the snake.
screen.listen()
screen.onkey(snake.right, "d")
screen.onkey(snake.up, "w")
screen.onkey(snake.left, "a")
screen.onkey(snake.down, "s")

# Main Code
game_on = True
while game_on:
    # For making the snake move smoothly.
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detects collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detects collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # Detects collision with tail.
    for snake_part in snake.snake_body[1:]:
        if snake.head.distance(snake_part) < 10:
            scoreboard.reset()
            snake.reset()

# Exit the screen with mouse click.
screen.exitonclick()

# Snake-game
# This game plays 'snake' by allowing the user to control a 'snake' with the arrow
# keys and grow as the 'snake' eats 'food' randomly placed in the field of play.
# Rules
# -The snake cannot do a 180 by changing in the opposite direction
# -The score increases by 1 whenever the snake eats (runs over) 'food'
# -The game ends whenever the snake eats itself or hits a wall
# -A High Score is kept on screen with the highest score achieved

from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

FOOD_PROXIMITY = 15
WALL_PROXIMITY = 280
TAIL_PROXIMITY = 10

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Map snake nav keys to arrow keys
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < FOOD_PROXIMITY:
        # print("nom nom nom")
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > WALL_PROXIMITY or snake.head.xcor() < -WALL_PROXIMITY or snake.head.ycor() > WALL_PROXIMITY or snake.head.ycor() < -WALL_PROXIMITY:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    # for segment in snake.segments:
    #     if segment != snake.head and snake.head.distance(segment) < TAIL_PROXIMITY:
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < TAIL_PROXIMITY:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()

#Snake game, made by Mofe, using Turtle
from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time


#Setup
snake = Snake()
food = Food()
score = Score()

screen = Screen()
screen.update()

screen.listen()
screen.setup(width=600, height=600)
screen.colormode(255)
screen.bgcolor(36, 37, 41)
screen.title("Snake Game")
screen.tracer(0)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

#Gameplay
playing = True
while playing:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.squares[0].distance(food) < 20:
        food.relocate()
        snake.grow()
        score.increase_score()
        print("yummy")

    if snake.squares[0].xcor() > 290 or snake.squares[0].xcor() < -290 or snake.squares[0].ycor() > 290 or snake.squares[0].ycor() < -290:
        playing = False
        score.finish()

    for i in snake.squares[1:]:
        if snake.squares[0].distance(i) < 10:
            playing = False
            score.finish()
screen.exitonclick()


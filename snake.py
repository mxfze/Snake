from turtle import Screen, Turtle
import time

screen = Screen()
SETUP = [(0, 0), (-20, 0), (-40, 0)]
SPEED = 22

class Snake:

    def __init__(self):
        self.squares = []
        self.create_snake()

    def create_snake(self):
        for pos in SETUP:
            self.append_square(pos)

    def move(self):
        for i in range(len(self.squares) - 1, 0, -1):
            new_x = self.squares[i - 1].xcor()
            new_y = self.squares[i - 1].ycor()
            self.squares[i].goto(new_x, new_y)
        self.squares[0].forward(SPEED)
##############################################################################
##############################################################################
    def up(self):
        direction = self.squares[0].heading()
        if direction != 270:
            self.squares[0].setheading(90)
        else:
            pass

    def down(self):
        direction = self.squares[0].heading()
        if direction != 90:
            self.squares[0].setheading(270)
        else:
            pass

    def right(self):
        direction = self.squares[0].heading()
        if direction != 180:
            self.squares[0].setheading(0)
        else:
            pass

    def left(self):
        direction = self.squares[0].heading()
        if direction != 0:
            self.squares[0].setheading(180)
        else:
            pass
########################################################################
    def append_square(self, pos):
        square = Turtle("square")
        square.color("white")
        square.penup()
        square.goto(pos)
        self.squares.append(square)


    def grow(self):
        self.append_square(self.squares[-1].position())

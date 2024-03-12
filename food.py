from turtle import Screen, Turtle
from colours import colours
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(0.8,0.8)
        self.speed("fastest")
        self.relocate()

    def relocate(self):
        self.color(random.choice(colours))
        ran_x = random.randint(-275, 275)
        ran_y = random.randint(-275, 275)
        self.goto(ran_x, ran_y)
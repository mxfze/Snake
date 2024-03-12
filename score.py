from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.update()
        self.hideturtle()


    def update(self):
        self.goto(0, 260)
        self.write(f'Score: {self.score}', True, align="center", font=("Fredoka", 24, "normal"))

    def increase_score(self):
        self.score +=1
        self.clear()
        self.update()

    def finish(self):
        self.clear()
        self.goto(0, 0)
        self.write(f'Game Over', True, align="center", font=("Fredoka", 24, "normal"))
        self.goto(0, -30)
        self.write(f'Your score was: {self.score}', True, align="center", font=("Fredoka", 24, "normal"))


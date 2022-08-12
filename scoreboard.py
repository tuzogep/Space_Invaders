from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-325, 200)
        self.write(self.score, align="center", font=("Courier", 60, "normal"))

    def point(self):
        self.score += 10
        self.update_scoreboard()

class Lives(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 3
        self.update_lives()

    def update_lives(self):
        self.clear()
        self.goto(325, 200)
        self.write(self.score, align="center", font=("Courier", 60, "normal"))

    def loose_life(self):
        self.score -= 1
        self.update_lives()
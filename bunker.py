from turtle import Turtle


class Bunker(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=0.25)
        self.goto(position)

    def destroy(self):
        self.goto(-1000, -1000)
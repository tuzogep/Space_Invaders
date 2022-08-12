from turtle import Turtle


class Cannon(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.goto(position)

    def go_left(self):
        new_x = self.xcor() - 40
        self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = self.xcor() + 40
        self.goto(new_x, self.ycor())

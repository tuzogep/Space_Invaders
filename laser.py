from turtle import Turtle


class Laser(Turtle):

    def __init__(self, ):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("classic")
        self.y_move = 5
        self.move_speed = 2
        self.goto(-10000,0)
        self.setheading(90)
        self.shapesize(stretch_wid=0.5, stretch_len=2)

    def move(self):
        self.forward(self.y_move)

    def shoot(self, position):
        self.goto(position)

    def reset(self):
        self.goto(10000, 10000)
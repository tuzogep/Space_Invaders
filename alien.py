from turtle import Turtle


class Alien(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("turtle")
        self.color("orange")
        self.shapesize(stretch_wid=2, stretch_len=1)
        self.penup()
        self.goto(position)
        self.right(90)
        self.x_step = 20
        self.y_step = 5

    def hit(self):
        self.goto(1000, 1000)

    def move_right(self):
        new_x = self.xcor() + self.x_step
        self.goto(new_x, self.ycor())

    def move_left(self):
        new_x = self.xcor() - self.x_step
        self.goto(new_x, self.ycor())

    def move_down(self):
        new_y = self.ycor() - self.y_step
        self.goto(self.xcor(), new_y)


class AlienShot(Turtle):
    def __init__(self, ):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("triangle")
        self.y_move = 5
        self.move_speed = 2
        self.goto(-10000, -900)
        self.setheading(-90)
        self.shapesize(stretch_wid=0.25, stretch_len=1.5)

    def move(self):
        self.forward(self.y_move)

    def shoot(self, position):
        self.goto(position)

    def reset(self):
        self.goto(10000, 10000)
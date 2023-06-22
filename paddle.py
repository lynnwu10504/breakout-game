from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=10)
        self.color("white")
        self.penup()
        self.setposition(x=0, y=-270)

    def go_left(self):
        if self.xcor() >= -300:
            new_x = self.xcor() - 60
            self.goto(new_x, self.ycor())

    def go_right(self):
        if self.xcor() <= 300:
            new_x = self.xcor() + 60
            self.goto(new_x, self.ycor())

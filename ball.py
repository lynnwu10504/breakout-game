import time
from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.setposition(x=0, y=-250)
        self.x_move = -15
        self.y_move = 10
        self.left_side = self.xcor() - 5
        self.right_side = self.xcor() + 5
        self.top_side = self.ycor() + 5
        self.bottom_side = self.ycor() - 5
        self.move_speed = 0.05
        self.hits = 0

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self, direction):
        if direction == 'h':
            self.x_move *= -1
        elif direction == 'v':
            self.y_move *= -1
            self.move_speed *= 0.95
            if self.move_speed <= 0.02:
                self.move_speed = 0.02

    def reset_position(self):
        time.sleep(0.1)
        self.move_speed = 0.05
        self.goto(0, -250)
        self.bounce('v')


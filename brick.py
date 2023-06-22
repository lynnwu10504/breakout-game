from turtle import Turtle
import random

COLOR_LIST = ['green', 'yellow', 'red']

weights = [1, 2, 3]

# class Brick(Turtle) is responsible for constructing each brick

# class Bricks is responsible for the structure of the bricks

# Brick is 50 x 20

colors = ['yellow', 'orange', 'red', 'skyblue', 'brown', 'navy', 'violet']


class Brick(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shape("square")
        self.color('black', random.choice(colors))
        self.shapesize(stretch_wid=2.5, stretch_len=5)
        self.penup()
        self.setposition(x=x_cor, y=y_cor)
        self.left_side = self.xcor() - 25
        self.right_side = self.xcor() + 25
        self.top_side = self.ycor() + 12.5
        self.bottom_side = self.ycor() - 12.5


class Bricks:

    def __init__(self):
        self.y_start = 0
        self.y_end = 270
        self.bricks = []
        self.create_all_lanes()

    def create_lane(self, y_cor):
        for i in range(-340, 340, 108):
            brick = Brick(x_cor=i, y_cor=y_cor)
            self.bricks.append(brick)

    def create_all_lanes(self):
        for i in range(self.y_start, self.y_end, 55):
            self.create_lane(i)







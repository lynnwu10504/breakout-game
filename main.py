from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from brick import Bricks
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=760, height=600)
screen.title("Breakout")
screen.tracer(0)

paddle = Paddle()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")

ball = Ball()
bricks = Bricks()

game_is_on = True
while game_is_on:

    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.xcor() < -370 or ball.xcor() > 370:
        ball.bounce('h')
    if ball.ycor() > 270:
        ball.bounce('v')

    # Detect collision with paddle
    if ball.distance(paddle) < 140 and -255 < ball.ycor() < -245:
        ball.bounce('v')

    for item in bricks.bricks:
        # Detect ball missing the paddle
        if ball.ycor() < -310:
            ball.reset_position()
            scoreboard.reset_scoreboard()

        if ball.distance(item) < 60:
            item.clear()
            item.goto(3000, 3000)
            bricks.bricks.remove(item)
            scoreboard.add_point()
            ball.hits += 1

            # Detect collision from the left
            if ball.xcor() < item.left_side:
                ball.bounce('h')
            # Detect collision from the right
            elif ball.xcor() > item.right_side:
                ball.bounce('h')
            # Detect collision from the top
            elif ball.ycor() > item.top_side:
                ball.bounce('v')
            # Detect collision from the bottom
            elif ball.ycor() < item.bottom_side:
                ball.bounce('v')

    if ball.hits == 35:
        ball.hideturtle()
        scoreboard.final_score()

screen.exitonclick()

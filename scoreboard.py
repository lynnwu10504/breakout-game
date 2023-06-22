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
        self.goto(-355, 255)
        self.write(f"Score: {self.score}", font=("Arial", 26, "normal"))

    def add_point(self):
        self.score += 1
        self.update_scoreboard()

    def reset_scoreboard(self):
        self.score = 0
        self.update_scoreboard()

    def final_score(self):
        self.clear()
        self.goto(-280, 0)
        self.write(f"Congrats on finishing the game!\n Your final score is: {self.score}", font=("Arial", 40, "normal"))
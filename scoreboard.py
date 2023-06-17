from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.score = 0
        with open("highscore.txt", mode="r") as highscore_file:
            self.high_score = int(highscore_file.read())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscore.txt", mode="w") as highscore_file:
                highscore_file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def score_up(self):
        self.score += 1
        self.update_scoreboard()





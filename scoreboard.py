from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        with open("highscore.txt") as file:
            highscore = int(file.read())
            self.highscore = highscore
        self.goto(-230, 250)
        self.score = 0
        self.update_scoreboard()
        self.hideturtle()



    def plus(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"your score is: {self.score}, high score: {self.highscore}", move=False, align='left', font=('Arial', 24, 'normal'))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_scoreboard()
    # def end_of_game(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", move=False, align='center', font=('Arial', 30, 'normal'))

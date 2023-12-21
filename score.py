import turtle
class Score(turtle.Turtle):
    def __init__(self,side):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.score = 0
        if side == "left":
            self.goto(-330,250)
        elif side == "right":
            self.goto(330,250)
        self.write(f"Score:{self.score}", align='center', font=('Arial', 20, 'normal'))
    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score:{self.score}", align='center', font=('Arial', 20, 'normal'))


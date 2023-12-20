import turtle


class Paddle(turtle.Turtle):
    def __init__(self,position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(5, 1)
        self.color('white')
        self.goto(position)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(-350,new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(-350, new_y)

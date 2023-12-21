import turtle

class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color('white')
        self.x_move = 0.1
        self.y_move = 0.1
    def move(self):
        x_cord = self.xcor() + self.x_move
        y_cord = self.ycor() + self.y_move
        self.goto(x_cord, y_cord)

    def increase_speed(self):
        self.x_move *= 1.0001
        self.y_move *= 1.0001


    def bounce(self):
        self.y_move *= -1


    def padbounce(self):
        self.x_move *= -1
import turtle
import paddle
import ball
import score
import time

screen = turtle.Screen()
screen.setup(800,600)
screen.tracer(0)
screen.bgcolor('black')
screen.title('Pong')

r_paddle= paddle.Paddle((350,0))
l_paddle= paddle.Paddle((-350,0))
score_r = score.Score('right')
score_l = score.Score('left')
ball = ball.Ball()
is_game_cont = True
while is_game_cont:
    screen.listen()
    screen.onkeypress(key='w',fun=l_paddle.up)
    screen.onkeypress(key='s',fun=l_paddle.down)
    screen.onkeypress(key='Up',fun=r_paddle.up)
    screen.onkeypress(key='Down',fun=r_paddle.down)
    ball.move()
    screen.update()
    ball.increase_speed()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    if ball.distance(r_paddle) < 80 and ball.xcor() > 320:
        ball.padbounce()
    if ball.distance(l_paddle) < 80 and ball.xcor() < -320:
        ball.padbounce()
    if ball.xcor() > 380:
        score_l.increase_score()
        ball.goto(0,0)
        ball.x_move = 0.1
        ball.y_move = 0.1
    elif ball.xcor() < -380:
        score_r.increase_score()
        ball.goto(0,0)
        ball.x_move = 0.1
        ball.y_move = 0.1


screen.exitonclick()
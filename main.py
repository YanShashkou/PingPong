import turtle
import paddle

screen = turtle.Screen()
screen.setup(800,600)
screen.tracer(0)
screen.bgcolor('black')
screen.title('Pong')

r_paddle= paddle.Paddle((350,0))
l_paddle= paddle.Paddle((-350,0))
is_game_cont = True
while is_game_cont:
    screen.listen()
    screen.onkeypress(key='w',fun=l_paddle.up)
    screen.onkeypress(key='s',fun=l_paddle.down)
    screen.update()








screen.exitonclick()
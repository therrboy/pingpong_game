from turtle import Turtle, Screen


screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Ping Pong Game")


ball = Turtle()
ball.shape("circle")
ball.shapesize(1, 1)
ball.speed(1)
ball.color("white")
ball.goto(0, 0)

juego = True
puntos = 0

while juego:
    y = ball.ycor()
    x = ball.xcor()
    new_y = y + 1
    new_x = x + 1
    ball.setposition(new_x, new_y)
    puntos += 1
if puntos >= 100:
    juego = False
else:
    print("Hola")


screen.exitonclick()

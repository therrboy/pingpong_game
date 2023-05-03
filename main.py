from turtle import Screen
from raqueta_paddle import Paddle
from pelota import Ball
from puntos import Puntos
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(950, 750)
screen.title("Ping Pong Game")
screen.tracer(0)  # Se usa con ScreenUpdate para funcionar

cordenadas = [(-350, 0), (350, 0)]

paddle1 = Paddle(cordenadas[0])
paddle2 = Paddle(cordenadas[1])

screen.listen()
screen.onkeypress(paddle1.up, "w")
screen.onkeypress(paddle1.down, "s")
screen.onkeypress(paddle2.up, "Up")
screen.onkeypress(paddle2.down, "Down")

juego_prendido = True
pelota = Ball()
puntos = Puntos()
puntos.tablero()

while juego_prendido:
    time.sleep(0.0000000000001)
    screen.update()  # Se usa con Tracer para poder funcionar
    pelota.move()

    # Colision con pared
    if pelota.ycor() > 290 or pelota.ycor() < -290:
        pelota.rebote_y()

    # Contacto con los paddle
    if pelota.distance(paddle2) < 50 and pelota.xcor() > 330:
        pelota.rebote_x()

    if pelota.distance(paddle1) < 50 and pelota.xcor() < -330:
        pelota.rebote_x()

    # Puntos y reset de pelota
    if pelota.xcor() == 380:
        pelota.reset_position()
        puntos.puntos_1()

    if pelota.xcor() == -380:
        pelota.reset_position()
        puntos.puntos_2()

    print(pelota.xcor())
screen.exitonclick()

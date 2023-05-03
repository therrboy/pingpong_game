from pelota import Ball
from turtle import Screen

screen = Screen()


class Puntos(Ball):
    def __init__(self):
        super().__init__()
        self.puntos_juego_1 = 0
        self.puntos_juego_2 = 0
        self.hideturtle()


    def tablero(self):
        self.penup()
        self.goto(-40, 320)
        self.hideturtle()
        self.write("Puntos", font=("Arial", 18, "normal"))
        self.update()

    def puntos_1(self):
        self.puntos_juego_1 += 1
        self.update()

    def puntos_2(self):
        self.puntos_juego_2 += 1
        self.update()

    def update(self):
        self.clear()
        self.goto(-300, 300)
        self.write(f"Player 1 puntos:{self.puntos_juego_1}", font=("Arial", 18, "normal"))
        self.goto(200, 300)
        self.write(f"Player 2 puntos:{self.puntos_juego_2}", font=("Arial", 18, "normal"))

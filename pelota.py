from turtle import Turtle


class Ball(Turtle):  # Si utilizamos el llamado de Turtle aqui, no necesitamos llamarlo abajo con un nombre
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.speed(0)
        self.shapesize(1, 1)
        self.color("white")
        self.limite_pantalla()
        self.setposition(0, 0)
        self.xmove = 1
        self.ymove = 1

    def move(self):
        x = self.xcor() + self.xmove
        y = self.ycor() + self.ymove
        self.goto(x, y)

    def rebote_x(self):
        self.xmove *= -1

    def rebote_y(self):
        self.ymove *= -1

    def limite_pantalla(self):
        self.penup()
        self.goto(-400, 300)
        self.pendown()
        for i in range(2):
            self.forward(800)
            self.right(90)
            self.forward(600)
            self.right(90)
        self.penup()
        self.goto(0, 300)
        self.pendown()
        self.right(90)
        self.forward(600)
        self.penup()

    def reset_position(self):
        self.goto(0, 0)
        self.rebote_x()
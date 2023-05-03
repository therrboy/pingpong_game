from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, posicion):
        super().__init__()
        self.shapesize(5, 1)
        self.color("white")
        self.shape("square")
        self.penup()
        self.goto(posicion)

    def up(self):
        if self.ycor() <= 240:
            self.setpos(self.xcor(), self.ycor() + 10)


    def down(self):
        if self.ycor() >= -240:
            self.setpos(self.xcor(), self.ycor() - 10)


import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__(shape='circle')
        self.penup()
        self.resizemode('user')
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color('blue')
        # self.speed(10)
        self.screen.tracer(0)
        self.move_food()

    def move_food(self):
        x_cor = random.uniform(-290, 290)
        y_cor = random.uniform(-290, 290)
        self.goto(x_cor, y_cor)
        self.screen.update()


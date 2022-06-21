import time
from turtle import Turtle

START_POS = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.default = None
        self.head = None
        self.snakes = []
        
        self.create_snake()

    def create_snake(self):
        for position in START_POS:
            self.add_segment(position)
        self.head = self.snakes[0]

    def add_segment(self, position):
        new_snake = Turtle(shape='square')
        new_snake.penup()
        new_snake.color('white')
        new_snake.goto(position)
        self.snakes.append(new_snake)

    def reset(self):

        for snake in self.snakes:
            snake.goto(10000, 0)
        self.snakes = []
        self.create_snake()
        time.sleep(1)
        self.head = self.snakes[0]

    def extend(self):
        self.add_segment(self.snakes[-1].pos())

    def move(self):
        for element in range(len(self.snakes)-1, 0, -1):
            new_position = self.snakes[element-1].pos()
            self.snakes[element].goto(new_position)
        self.head.forward(DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

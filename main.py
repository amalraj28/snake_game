from food import Food
import time
from turtle import Screen
from snake import Snake
from score import Score


snake = Snake()
food = Food()
screen = Screen()
score = Score()


screen.setup(width=600, height=600)
screen.title('Snake Xenzia_Python')
screen.bgcolor('black')
screen.tracer(0)

screen.listen()

screen.onkey(key='Up', fun=snake.up)
screen.onkey(key='Down', fun=snake.down)
screen.onkey(key='Left', fun=snake.left)
screen.onkey(key='Right', fun=snake.right)

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        score.increment_score()

        food.move_food()
        snake.extend()

    if snake.head.xcor() < -298 or snake.head.xcor() > 298 or snake.head.ycor() < -298 or snake.head.ycor() > 298:
        score.reset()
        snake.reset()

    for each_snake in snake.snakes[1:]:
        if snake.head.distance(each_snake) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()

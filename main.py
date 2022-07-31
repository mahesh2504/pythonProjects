from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('snakeGame')
screen.tracer(0)
snake = Snake()




is_gameOn = True
while is_gameOn:
    screen.update()
    time.sleep(0.1)
    snake.move()









screen.exitonclick()


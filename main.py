from turtle import Turtle,Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('snakeGame')
positions = [0, 20, 40]
for i in range(3):
    new_square = Turtle()
    new_square.color("white")
    new_square.shape('square')
    new_square.penup()
    new_square.goto(positions[i-1], 0)







screen.exitonclick()


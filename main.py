from turtle import Turtle,Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('snakeGame')
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
for position in starting_positions:
    new_square = Turtle()
    new_square.color("white")
    new_square.shape('square')
    new_square.penup()
    new_square.goto(position)








screen.exitonclick()


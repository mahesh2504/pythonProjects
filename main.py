from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('snakeGame')
screen.tracer(0)
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []
for position in starting_positions:
    new_square = Turtle()
    new_square.color("white")
    new_square.shape('square')
    new_square.penup()
    new_square.goto(position)
    segments.append(new_square)


is_gameOn = True
while is_gameOn:
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(segments)-1, 0, -1):
        new_x = segments[seg_num-1].xcor()
        new_y = segments[seg_num-1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)
    segments[0].left(90)










screen.exitonclick()


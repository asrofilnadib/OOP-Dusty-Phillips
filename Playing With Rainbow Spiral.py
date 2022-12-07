import turtle
from turtle import *

colors = 'red', 'purple', 'green', 'blue', 'pink', 'orange'

t = turtle.Pen()
t.speed(0)
bgcolor("black")

for i in range(360):
    t.pencolor(colors[i % 6])
    # t.pensize(i / 100 + 1)
    t.forward(i)
    t.lt(59)

done()

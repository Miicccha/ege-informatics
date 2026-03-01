from turtle import *
speed(0)
left(90)
k =20
tracer(0)
for x in range (-20,20):
    for y in range(-20,20):
        goto(x, y)
        dot(3)

pendown()

for i in range(2):
    forward(14*k)
    left(270)
    forward(12*k)
    right(90)
penup()

forward(9*k)
right(90)
forward(7*k)
left(90)
pendown()

for i in range(2):
    forward(13*k)
    right(90)
    forward(6*k)
    right(90)
done()
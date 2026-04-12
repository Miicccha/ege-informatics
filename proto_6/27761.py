from turtle import *
speed(0)
k=20
tracer(0)

for i in range(2):
    forward(1*k)
    left(270)
    forward(16*k)
    right(90)

up()
backward(4*k)
right(90)
forward(10*k)
left(90)
down()

for i in range(2):
    forward(17*k)
    right(90)
    forward(7*k)
    right(90)
up()

for i in range(-20,20):
    for j in range(-20,20):
        goto(i*k,j*k)
        dot(3)
screensize(1000,1000)
done()
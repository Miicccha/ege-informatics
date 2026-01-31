from turtle import *
k=35
tracer(0)
down()
right(90)
pencolor("black")
for i in range(6):
    forward(33*k)
    right(90)
    forward(20*k)
    right(90)
up()
forward(3*k)
right(90)
forward(9*k)
left(90)
down()
pencolor("red")
for i in range(6):
    forward(24*k)
    right(90)
    forward(25*k)
    right(90)  
up()
for i in range(-40,40):
    for j in range(-40,40):
        goto(i*k,j*k)
        dot(3)
screensize(3000,3000)
done()
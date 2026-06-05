from turtle import*
k=20
tracer(0)
down()
right(90)
for i in range(3):
    forward(32*k)
    right(90)
    forward(38*k)
    right(90)
up()

forward(25*k)
right(90)
forward(21*k)
left(90)
down()

for i in range(3):
    forward(29*k)
    right(90)
    back(18*k)
    right(90)
up()
for i in range(-60,60):
    for j in range(-62,60):
        goto(i*k,j*k) 
        dot(4)
screensize(3000,3000)
exitonclick()
from turtle import*
k=35
tracer(0)
down
right(180)

for i in range(7):
    forward(11*k)
    right(45)
    forward(8*k)
    right(135)
up()
for i in range(-40,40):
    for j in range(-40,40):
        goto(i*k,j*k)
        dot(3)
screensize(3000,3000)
done()
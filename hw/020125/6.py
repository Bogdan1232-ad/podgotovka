from turtle import *

lt(90)
tracer(0)
m = 10
screensize(2000, 2000)

for i in range(9):
    fd(15 * m)
    rt(90)
    fd(25 * m)
    rt(90)
up()
backward(10 * m)
rt(90)
down()
for i in range(8):
    fd(15 * m)
    lt(90)
    fd(25 * m)
    lt(90)
up()
fd(6 * m)
lt(90)
down()
for i in range(7):
    fd(15 * m)
    rt(90)
    fd(25 * m)
    rt(90)

up()
for x in range(-40, 40):
    for y in range(-40, 40):
        goto(x*m, y*m)
        dot(2, 'darkred')
done()
from turtle import *

left(90)
m = 10
tracer(0)

for i in range(2):
    down()
    for j in range(2):
        fd(8 * m)
        rt(90)
        fd(8 * m)
        rt(90)
    up()
    fd(6 * m)
    rt(90)
    fd(6 * m)
    lt(90)

rt(180)
fd(4 * m)

down()
for i in range(4):
    fd(8 * m)
    rt(270)

up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*m, y*m)
        dot(3, 'darkred')
update()
done()
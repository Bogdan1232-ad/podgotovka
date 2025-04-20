from turtle import *

screensize(2000, 2000)
m = 80
lt(90)
tracer(0)

for i in range(15):
    fd(4 * m)
    rt(60)

up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * m, y * m)
        dot(3, 'darkred')
update()
done()

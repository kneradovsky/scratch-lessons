import turtle
import sys

t = turtle
x=0
y=0
a=0
t.setpos(0,0)
t.tracer(0,5)
for j in range(100):
    t.pu()
    t.home()
    t.seth(a % 360)
    t.fd(30)
    t.pd()
    a+=17
    for i in range(4) :
        t.fd(25)
        t.rt(90)
    t.update()

sys.stdin.read()
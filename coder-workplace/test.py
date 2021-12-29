import turtle
import sys

t = turtle
x=0
y=0
a=0
t.setpos(0,0)
t.tracer(0,5)
t.colormode(255)
for j in range(200):
    t.pu()
    t.home()
    t.seth(a % 360)
    t.fd(30)
    t.pd()
    if j>72 : a+=-5
    else : a+=5
    for i in range(4) :
        t.fd(25)
        t.rt(90)
        t.pencolor((j%10*20,j%128*2,j%64*4))

    t.update()

sys.stdin.readline()    
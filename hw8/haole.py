from turtle import *
speed(10)
def square():
    pencolor('blue')
    for i in range(4):
        forward(100)
        left(90)
        
def cir(r):
    pencolor('red')
    up()
    goto(0,-r)
    down()
    circle(r)
    up()
    goto(0,0)
    down()
    
    
cir(50)
cir(70)
cir(90)
cir(110)
for i in range(0,90,6):
    left(i)
    square()
Screen().exitonclick()


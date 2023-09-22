import turtle as t
import random

import math
import time 


t.getscreen()
t.speed(0)
p1= t.Turtle()
p1.color("green")
p1.shape("turtle")
p1.penup()
p2= t.Turtle()
p2.color("red") 
p2.shape("turtle")
p2.penup()
t.penup()
t.goto(300, 50)
t.pendown()
t.circle(50)
t.penup()
t.goto(300, -150)
t.pendown()
t.circle(50)
p1.goto(-450,100)
p2.goto(-450,-100)


#while p1.position() <= (200, 200) or p2.position() <= (200, 200):
#    input('Player1 : Press enter to play... ')
#    rand1 = 10*random.randint(1, 6)
#    p1.forward(rand1)
#
#    input('Player2 : Press enter to play... ')
#    rand2 = 10*random.randint(1, 6)
#    p2.forward(rand2)    


def up():
    x0=t.position()[0] 
    x1=t.position()[1]
    x1 +=10
    t.goto(x0,x1)

def down():
    x0=t.position()[0] 
    x1=t.position()[1]
    x1 -=10
    t.goto(x0,x1)

def left():
    x0=t.position()[0]
    x1=t.position()[1]
    x0 -=10
    t.goto(x0,x1)

def right():
    x0=t.position()[0]
    x1=t.position()[1]
    x0 +=10
    t.goto(x0,x1)

def walk1():
    if p1.position() <= (200, 200):
        x0=p1.position()[0]
        x1=p1.position()[1]
        x0 +=10 + random.randint(1, 5)
        p1.goto(x0,x1)
    else:
        print('P1 is winner')

def walk2():
    if p2.position() <= (200, 200):
        x0=p2.position()[0]
        x1=p2.position()[1]
        x0 +=10 + random.randint(1, 5)
        p2.goto(x0,x1)
    else:
        print('P2 is winner')



t.listen()
#t.onkey(up, "Up")
#t.onkey(left, "Left")
#t.onkey(down, "Down")
#t.onkey(right, "Right")
t.onkey(walk1, "a")
t.onkey(walk2, "l")
t.mainloop()
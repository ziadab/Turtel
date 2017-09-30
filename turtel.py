from turtle import Turtle
from random import randint
from time import sleep

ziad = Turtle()
ziad.color('red')
ziad.shape('turtle')
ziad.penup()
ziad.goto(-260, 100)
ziad.pendown()
sleep(1)


dead = Turtle()
dead.color('blue')
dead.shape('turtle')
dead.penup()
dead.goto(-260, 70)
dead.pendown()
sleep(1)


me = Turtle()
me.color('green')
me.shape('turtle')
me.penup()
me.goto(-260, 40)
me.pendown()
sleep(1)

x = Turtle()
x.color('pink')
x.shape('turtle')
x.penup()
x.goto(-260, 10)
x.pendown()

for movement in range(180):
    ziad.forward(randint(1,5))
    dead.forward(randint(1,5))
    me.forward(randint(1,5))
    x.forward(randint(1,5))




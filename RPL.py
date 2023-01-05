'''Program menulis "RPL" menggunakan Turtle'''

import turtle

t = turtle.Turtle()

t.speed(2)
t.pencolor("black")
t.pensize(5)

t.penup()
t.goto(-135, 35)
t.pendown()

#R
t.left(90)
t.forward(150)
t.right(90)
t.forward(75)
t.right(90)
t.forward(75)
t.right(90)
t.forward(75)
t.left(135)
t.forward(110)

#memindahkan turtle
t.penup()
t.goto(-35,35)
t.pendown()

#P
t.left(135)
t.forward(150)
t.right(90)
t.forward(75)
t.right(90)
t.forward(75)
t.right(90)
t.forward(75)

#memindahkan turtle
t.penup()
t.goto(65,185)
t.pendown()

#L
t.left(90)
t.forward(150)
t.left(90)
t.forward(75)

turtle.done()
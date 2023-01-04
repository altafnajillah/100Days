'''Program menggambar kotak di python menggunakan Turtle'''

import turtle

t = turtle.Turtle()
t.speed(1)
t.color("black")

t.penup()
t.goto(-100, 100)
t.pendown()

t.forward(200)
t.right(90)
t.forward(200)
t.right(90)
t.forward(200)
t.right(90)
t.forward(200)

turtle.done()
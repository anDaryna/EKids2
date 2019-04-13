#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Техническое задание:
На основе цветочка из квадратов, сделанного в первой итерации,
нарисовать картину из этого цветочка и солнышка.
Солнышко такое как тут, подойдет https://docs.python.org/3.7/library/turtle.html
В будущем ожидаю увидеть поле из разных цветов. Может, сделать цветок красивее.
"""

import turtle

turtle.penup()
turtle.speed(40)
turtle.goto(-200, 200)
a = abs(turtle.pos())
turtle.pendown()
turtle.begin_fill()
turtle.color('red', 'yellow')
while True:
    turtle.forward(150)
    turtle.left(170)
    b = abs(turtle.pos())
    if (a - 1 < b < a + 1):
        break
turtle.end_fill()
turtle.penup()


def draw_square(color,x,y,size):
    turtle.goto(x/60*size,y/60*size)
    turtle.begin_fill()
    turtle.pendown()
    turtle.color(color, 'red')
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.fillcolor(color)
    turtle.penup()
    turtle.end_fill()

def draw_circle(x,y,size):
    t = turtle.Turtle()
    t.penup()
    t.setpos(35 + x, -15 + y)
    t.begin_fill()
    t.pendown()
    t.color("yellow")
    t.circle(50)
    t.penup()
    t.end_fill()


def draw_flower(x,y,size):
    draw_square('purple',60+x, 60+y, size)
    draw_square('orange',-60+x, -60+y, size)
    draw_square('pink',-60+x, 60+y, size)
    draw_square('blue',60+x, -60+y, size)
    draw_circle(x,y)


draw_flower(0,30,60)
draw_flower(-200,-200,50)


turtle.shape("turtle")

turtle.hideturtle()

turtle.exitonclick()
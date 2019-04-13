#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Техническое задание:
На основе цветочка из квадратов, сделанного в первой итерации,
нарисовать картину из этого цветочка и солнышка.
Солнышко такое как тут, подойдет https://docs.python.org/3.7/library/turtle.html
В будущем ожидаю увидеть поле из разных цветов. Может, сделать цветок красивее.
"""

import turtle as t

t.penup()
t.speed(40)
t.goto(-200, 200)
a = abs(t.pos())
t.pendown()
t.begin_fill()
t.color('red', 'yellow')
while True:
    t.forward(150)
    t.left(170)
    b = abs(t.pos())
    if (a - 1 < b < a + 1):
        break
t.end_fill()
t.penup()


def draw_square(color, x, y, size):
    t.goto(x / 60 * size, y / 60 * size)
    t.goto(x, y)
    t.begin_fill()
    t.pendown()
    t.color(color, 'red')
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.fillcolor(color)
    t.penup()
    t.end_fill()


def draw_flower(x,y,size):
    draw_square('purple', 60+x, 60+y, size)
    draw_square('orange', -60+x, -60+y, size)
    draw_square('pink', -60+x, 60+y, size)
    draw_square('blue', 60+x, -60+y, size)
    draw_square('yellow', x, y, size)
    t.shape("turtle")
    t.hideturtle()

draw_flower(0, -100, 60)

draw_flower(0, -300, 70)

draw_flower(200, -100, 50)

draw_flower(200, -300, 70)

draw_flower(-200, -100, 30)

draw_flower(-200, -300, 60)

draw_flower(-400, -100, 50)

draw_flower(-400, -300, 30)

draw_flower(-600, -100, 40)

draw_flower(-600, -300, 60)

draw_flower(400, -100, 50)

draw_flower(400, -300, 40)

t.exitonclick()
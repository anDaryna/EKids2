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


def draw_square(color, x=0, y=0, size=70):
    t.goto(x,y)
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

def draw_flower(x, y, size=60):
    draw_square('purple', x - size, y - size, size)
    draw_square('orange', x - size, y + size, size)
    draw_square('pink', x + size, y + size, size)
    draw_square('blue', x + size, y - size, size)
    draw_square('yellow', x, y, size)

matrix = [
          [-200, 100, 20],
          [0, 100, 20],
          [200, 100, 20],
          [-200, 0, 30],
          [0, 0, 30],
          [200, 0, 30],
          [-200, -170, 60],
          [0, -170, 60],
          [200, -170, 60]
           ]


for row in range(len(matrix)):
    draw_flower(matrix[row][0],matrix[row][1],matrix[row][2])


t.color('blue')
t.shape("turtle")
t.hideturtle()

t.exitonclick()
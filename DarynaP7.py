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

def draw_flower(strong, x, y, size=60):
    draw_square((int(255*strong), int(153*strong), int(153*strong)), x - size, y - size, size)
    draw_square((int(179*strong), int(0*strong), int(179*strong)), x - size, y + size, size)
    draw_square((int(255*strong), int(204*strong), int(255*strong)), x + size, y + size, size)
    draw_square((int(0*strong), int(255*strong), int(255*strong)), x + size, y - size, size)
    draw_square((int(225*strong), int(225*strong), int(128*strong)), x, y, size)

t.colormode(255)
t.bgcolor((0, 255, 0))

for number in range(5):
    draw_flower(0.5, (number)*100 + 50, number*10, 20)
    draw_flower(0.5, (number)*-100 - 50, number*10, 20)

for number in range(6):
    draw_flower(0.8, (number)*100 + 50, number*10 - 95, 30)
    draw_flower(0.8, (number)*-100 - 50, number*10 - 95, 30)

for number in range(5):
    draw_flower(1, (number)*150 + 75, number*10 - 230, 45)
    draw_flower(1, (number)*-150 - 75, number*10 - 230, 45)


t.color('blue')
t.shape("turtle")
t.hideturtle()

t.exitonclick()
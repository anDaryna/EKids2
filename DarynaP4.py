#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Техническое задание:
Нарисовать цветочек из квадратов,
чтоб серединка была желтой,
а лепестки других цветов
"""

import turtle as t



def draw_square():
    t.begin_fill()
    t.forward(30)
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(30)
    t.left(90)
    # t.color('red')
    t.forward(30)
    t.left(90)
    t.end_fill()

# 1 kvadrat
t.color('orange')
draw_square()

# zmina kursora
t.setx(30)
t.color('white')
t.setx(50)

# 2 kvadrat
t.color('blue')
draw_square()

# zmina kursora
t.sety(30)
t.color('white')
t.sety(50)

# 3 kvadrat
t.color('red')
draw_square()


# zmina kursora
t.color('white')
t.setx(0)
# t.sety(50)

# 4 kvadrat
t.color('pink')
draw_square()


# zmina kursora
# t.color('')
t.setx(25)
t.sety(25)

# 4 kvadrat
t.color('yellow')
draw_square()

t.shape("turtle")
t.hideturtle()

t.speed(30)

t.exitonclick()

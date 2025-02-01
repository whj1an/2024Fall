# ITI 1120
# Assignment 0
# Wang, Haojian
# 300411829

import turtle
s=turtle.Screen()
t=turtle.Turtle(shape='turtle')

t.penup()
t.goto(-300,0)
t.pendown()
t.setheading(-45)
t.circle(50,90)

# your code should go right after this line

t.penup()
t.goto(-100,200)
t.pendown()
t.circle(50)

# Waves; tips: root2 * 100 = 70.71067, that is the disstance of circle center between each other.
# method 1
t.penup()
t.goto(-229.28933,0)
t.pendown()
t.setheading(-45)
t.circle(50,90)

t.penup()
t.goto(-158.57864,0)
t.pendown()
t.setheading(-45)
t.circle(50,90)

t.penup()
t.goto(-87.86796,0)
t.pendown()
t.setheading(-45)
t.circle(50,90)

t.penup()
t.goto(-17.15728,0)
t.pendown()
t.setheading(-45)
t.circle(50,90)

t.penup()
t.goto(53.55339,0)
t.pendown()
t.setheading(-45)
t.circle(50,90)

"""
# Method 2: Loop
for i in range (1,7):
    t.penup()
    t.goto(70.71067*i-300,0)
    t.pendown()
    t.setheading(-45)
    t.circle(50,90)
"""

# Move the tutle
t.penup()
t.goto(0,-50)
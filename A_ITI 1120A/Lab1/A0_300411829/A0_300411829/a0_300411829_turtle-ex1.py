# ITI 1120
# Assignment 0
# Wang, Haojian
# 300411829

import turtle
s=turtle.Screen()
t=turtle.Turtle()

# Place your code after this line

# draw the first circles
t.circle(10)

# draw the second circle
t.penup()
t.goto(0,-30)
t.pendown()
t.circle(40)

# draw the third circle
t.penup()
t.goto(0,-40)
t.pendown()
t.circle(50)
    
# draw the forth circle
t.penup()
t.goto(0,-50)
t.pendown()
t.circle(60)

# -----------------draw the lines--------------------
# Line 1
t.penup()
t.goto(-170,10)
t.pendown()
t.forward(340)

# Line 2
t.penup()
t.goto(-150,-140)

t.setheading(45)

t.pendown()
t.forward(420)

# Line 3
t.penup()
t.goto(0, -160)

t.setheading(90)

t.pendown()
t.forward(340)

# Line 4
t.penup()
t.goto(-150,160)

t.setheading(315)

t.pendown()
t.forward(420)

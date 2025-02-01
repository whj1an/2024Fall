# Wang Haojian
# 300411829
# ITI 1120 Assignment Number 1
# Vida

import math
import turtle
###################################################################
# Question 1
###################################################################
def mh2kh(s):
    '''
    speed(s) -> int number
    '''
    k = s*1.609344
    return k

###################################################################
# Question 2
###################################################################
def pythagorean_pair(a,b):
    '''
    a -> int
    b -> int
    '''
    c = (math.sqrt(a**2+b**2)%1 == 0)
    return c

###################################################################
# Question 3
###################################################################
def in_out(xs,ys,side):
    '''
    xs -> int
    ys -> int
    side -> int, should be non-negative number
    '''
    x = float(input("Enter a number for the x coordinate of a query point:"))
    y = float(input("Enter a number for the y coordinate of a query point:"))
    a1 = (xs <= x <= (xs+side)) and (ys <= y <= (ys+side))
    return a1

###################################################################
# Question 4
###################################################################
def safe(n):
    '''
    n -> any two non-negative int with two decimal
    '''
    a = ("9" not in str(n)) and ((n % 9) != 0)
    return a

###################################################################
# Question 5
###################################################################
def quote_maker(quote,name,year):
    '''
    quote -> string
    name -> string
    year -> non-negative int
    '''
    print(f"In {year}, a person called {name} said:\"{quote}")
    return

###################################################################
# Question 6
###################################################################
def quote_displayer():
    '''
    quote -> string, and you need to cover it by "
    name -> string, and you need to cover it by "
    year -> non-negative int
    '''
    quote = input("Give me a quote:")
    name = input("Who said that?")
    year = input("What year did she/he say that?")
    print(f"In {year}, a person called {name} said:\"{quote}")
    return

###################################################################
# Question 7
###################################################################
def rps_winner():
    '''
    p1,p2 -> String String
    Compare p1 and p2 are same or not, then return True or False
    '''
    p1 = str(input("What choice did player 1 make? \n Typer one of the following options: rock, paper, scissors: "))
    p2 = str(input("What choice did player 2 make? \n Typer one of the following options: rock, paper, scissors:"))
    a = (p1 == "paper" and p2 == "rock") or (p1 == "rock" and p2 == "scissors") or (p1 == "scissors" and p2 == "paper")
    b = (p1 != p2)
    print("Player 1 win. That is ", a)
    print("It is a tie. That is not", b)
    return

###################################################################
# Question 8
###################################################################
def fun(x):
    '''
    (number) -> (number)
    postive
    '''
    y = math.log10((x+3)**0.25)
    return y


###################################################################
# Question 9
###################################################################
def ascii_name_plaque(name):
    '''
    name -> string
    it should be covered by "
    '''
    length=(len(name) + 6)
    print("*" * length)
    print("*" + " "*(length - 2) + "*")
    print(f"* _{name}_ *")
    print("*" + " "*(length - 2) + "*")
    print("*" * length)
    return

###################################################################
# Question 10
###################################################################
def draw_court():
    s=turtle.Screen()
    t=turtle.Turtle(shape='turtle')
    t.speed(0)
    s.bgcolor()

    # Edge
    t.penup()
    t.goto(-400,-200)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    t.forward(800)
    t.left(90)
    t.forward(400)
    t.left(90)
    t.forward(800)
    t.left(90)
    t.forward(400)
    t.end_fill()

    # Left Square
    t.penup()
    t.goto(-400,100)
    t.pendown()
    t.left(90)
    t.forward(150)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(150)

    t.fillcolor("orange")
    t.begin_fill()
    t.penup()
    t.goto(-400,90)
    t.pendown()
    t.left(180)
    t.forward(150)
    t.right(90)
    t.forward(180)
    t.right(90)
    t.forward(150)
    t.right(90)
    t.forward(180)
    t.end_fill()

    # Right Square
    t.penup()
    t.goto(400,100)
    t.pendown()
    t.left(90)
    t.forward(150)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(150)

    t.fillcolor("orange")
    t.begin_fill()
    t.penup()
    t.goto(400,90)
    t.pendown()
    t.left(180)
    t.forward(150)
    t.left(90)
    t.forward(180)
    t.left(90)
    t.forward(150)
    t.left(90)
    t.forward(180)
    t.end_fill()
    t.penup()

    t.home()

    # Left Circle 1
    t.penup()
    t.goto(-250,-90)
    t.pendown()
    t.circle(90,180)

    # Left Circle 2
    t.penup()
    t.circle(90,15)
    t.pendown()
    t.circle(90,15)
    t.penup()
    t.circle(90,15)
    t.pendown()
    t.circle(90,15)
    t.penup()
    t.circle(90,15)
    t.pendown()
    t.circle(90,15)
    t.penup()
    t.circle(90,15)
    t.pendown()
    t.circle(90,15)
    t.penup()
    t.circle(90,15)
    t.pendown()
    t.circle(90,15)
    t.penup()
    t.circle(90,15)
    t.pendown()
    t.circle(90,15)

    # Three-point Line
    t.penup()
    t.goto(-400,-180)
    t.pendown()
    t.forward(60)

    t.circle(180,180)

    t.forward(60)

    # Right Circle 1
    t.penup()
    t.goto(250,90)
    t.pendown()
    t.circle(90,180)

    # Right Circle 2
    t.penup()
    t.circle(90,15)
    t.pendown()
    t.circle(90,15)
    t.penup()
    t.circle(90,15)
    t.pendown()
    t.circle(90,15)
    t.penup()
    t.circle(90,15)
    t.pendown()
    t.circle(90,15)
    t.penup()
    t.circle(90,15)
    t.pendown()
    t.circle(90,15)
    t.penup()
    t.circle(90,15)
    t.pendown()
    t.circle(90,15)
    t.penup()
    t.circle(90,15)
    t.pendown()
    t.circle(90,15)

    # Right Three-point Line
    t.penup()
    t.goto(400,180)
    t.pendown()
    t.forward(60)

    t.circle(180,180)

    t.forward(60)

    # Center Circle
    t.fillcolor("orange")
    t.begin_fill()
    t.penup()
    t.goto(0,90)
    t.pendown()
    t.right(180)
    t.circle(90)
    t.end_fill()
    t.penup()

    # Center Line
    t.penup()
    t.goto(0,200)
    t.pendown()
    t.left(90)
    t.forward(400)

    # Left ?
    t.penup()
    t.goto(-370,40)
    t.pendown()
    t.forward(80)
    t.penup()
    t.goto(-370,0)
    t.left(90)
    t.pendown()
    t.forward(10)
    t.dot(10)

    # Right ?
    t.penup()
    t.goto(370,40)
    t.right(90)
    t.pendown()
    t.forward(80)
    t.penup()
    t.goto(370,0)
    t.right(90)
    t.pendown()
    t.forward(10)
    t.dot(10)

    # Finish
    t.penup()
    t.goto(200,-250)


###################################################################
# Question 11
###################################################################
def alogical(n):
    '''
    n -> any float number grreat then or equals to 1
    '''
    return math.ceil(math.log2(n))

###################################################################
# Question 12
###################################################################
def cad_cashier(price,payment):
    '''
    (number,number) -> two non-negative floatingt-point number with two decimal places, and the second decimal in payment is 0 or 5.
    where payment >= price
    '''
    a = payment - price
    return(round((round(a * 20) / 20),2))

###################################################################
# Question 13
###################################################################
def min_CAD_coins(price,payment):
    '''
    (number,number) -> two non-negative floatingt-point number with two decimal places, and the second decimal in payment is 0 or 5.
    where payment >= price
    It will return five int for the numbers of 2$, 1$, 25cents, 10cents, and 5cents.
    '''
    c = cad_cashier(price,payment)
    cents = int(round(c * 100)) #round means to ensure that the final cents is always an integer
    
    t = cents//200
    cents = cents % 200
    
    l = cents // 100
    cents = cents % 100
    
    q = cents // 25
    cents = cents % 25
    
    d = cents // 10
    cents = cents % 10
    
    n = cents //5
    
    return(t,l,q,d,n)
    





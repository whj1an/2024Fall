1. Write a function mh2kh(s) that given the speed, s, expressed in miles/hour returns the same speed expressed in `kilometres/hour`.

```python
def mh2kh(s):
    '''
    speed(s) -> int number
    '''
    k = s*1.609344
    return k
```

2. Two numbers a and b are called Pythagorean pair if both a and b are integers and 
there exists an integer c such that $a^2 + b^2 = c^2$. Write a function `pythagorean_pair(a,b)` that 
takes two integers a and b as input and returns True if a and b are Pythagorean pair and False 
otherwise.

```python
def pythagorean_pair(a,b):
    '''
    a -> int
    b -> int
    '''
    c = (math.sqrt(a**2+b**2)%1 == 0)
    return c
```
3. Write a function `in_out(xs,ys,side)` that takes three numbers as input, where side is 
non-negative. Here `xs` and `ys` represent the x and y coordinates of the bottom left corner of a 
square; and side represents the length of the side of the square. (Notice that xs, ys, and side 
completely define a square and its position in the plane). Your function should first prompt the 
user to enter two numbers that represent the x and y coordinates of some query point. Your 
function should print True if the given query point is inside of the given square, otherwise it 
should print False. A point on the boundary of a square is considered to be inside the square.
> 编写一个函数 `in_out(xs,ys,side)`，以三个数字作为输入，其中 side 为非负数。这里 `xs` 和 `ys` 表示正方形左下角的 x 和 y 坐标；side 表示正方形边的长度。（请注意，xs、ys 和 side 完全定义了正方形及其在平面中的位置）。您的函数应首先提示用户输入两个数字，分别表示某个查询点的 x 和 y 坐标。如果给定的查询点位于给定正方形内，则您的函数应打印 True，否则应打印 False。正方形边界上的点被认为位于正方形内。
```python
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
```

4. Write a function safe(n) that takes a non-negative integer n as input where n has at most 2 digits. The function determines if n is a safe number. A number is not safe if it contains a 9 as a digit, or if it can be divided by 9. The function should test if n is safe and return True if n is safe and False otherwise.
>编写一个函数 safe(n)，以非负整数 n 作为输入，其中 n 最多有 2 位数字。该函数确定 n 是否为安全数字。如果数字中包含 9 作为数字，或者可以被 9 整除，则该数字不安全。该函数应测试 n 是否安全，如果 n 安全则返回 True，否则返回 False。

```python
def safe(n):
    '''
    n -> any two non-negative int with two decimal
    '''
    a = ("9" not in str(n)) and ((n % 9) != 0)
    return a
```
5. Write a function `quote_maker(quote, name, year)` that returns a sentence, i.e. a string of the following form: In year, a person called name said: “quote” See the next Section 2 below for some examples of how your function must behave.
>编写一个函数 `quote_maker(quote, name, year)`，返回一个句子，即以下形式的字符串：在 year 中，一个叫 name 的人说：“quote”。请参阅下面的第 2 节，了解函数必须如何运行的一些示例

```python
def quote_maker(quote,name,year):
    '''
    quote -> string
    name -> string
    year -> non-negative int
    '''
    print(f"In {year}, a person called {name} said:\"{quote}")
    return
```

6. Write a function `quote_displayer()` that prompts the user for a quote, name, and year. The function should then print a sentence using the same format as specified in the previous question. (To do that, your solution must make a call to `quote_maker` function from the previous question to obtain a string that you then print).
>编写一个函数 `quote_displayer()`，提示用户输入引言、姓名和年份。然后，该函数应使用与上一个问题中指定的相同格式打印一个句子。（为此，您的解决方案必须调用上一个问题中的 `quote_maker` 函数来获取然后打印的字符串）。

```python
def quote_displayer():
    '''
    quote -> string, and you need to cover it by "
    name -> string, and you need to cover it by "
    year -> non-negative int
    '''
    quote = input("Give me a quote:")
    name = input("Who said that?")
    year = input("What year did she/he say that?")
    return quote_maker(quote,name,year)
```

7. In this question you will write a function that determines and prints the result of a rock, paper, scissors game given choices of player 1 and player 2. In particular, write a function `rps_winner()` that prompts the user for choice of player 1 and then choice of player 2, and then it displays the result for player 1 as indicated in the examples given in Section 2. You may assume that the user will only enter words: rock, paper or scissors in lower case. Recall that paper beats rock, rock beats scissors and scissors beat paper. If both players make the same choice, we have a draw
>在本题中，你将编写一个函数，根据玩家 1 和玩家 2 的选择，确定并打印石头、剪刀、布游戏的结果。具体来说，编写一个函数 `rps_winner()`，提示用户选择玩家 1，然后选择玩家 2，然后显示玩家 1 的结果，如第 2 节中的示例所示。你可以假设用户只会输入小写的单词：石头、布或剪刀。回想一下，布胜过石头，石头胜过剪刀，剪刀胜过布。如果两个玩家做出相同的选择，我们就打成平局

```python
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
```

8. Write a function `fun(x)` that takes as input a positive number x and solves the following equation for y and returns y. The equation is $10^{4y}=x+3$
>编写一个函数`fun(x)`，以正数 x 作为输入，求解下列方程中的 y 并返回 y。该方程为 $10^{4y}=x+3$

```python
def fun(x):
    '''
    (number) -> (number)
    postive
    '''
    y = math.log10((x+3)**0.25)
    return y
```

9. Write a function `ascii_name_plaque(name)` that takes as input a string representing a person’s name and draws (using print function) a name plaque as shown in the examples given in Section 2 below. Recall that you may not use loops nor if/branching statements.
```python
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
```

10. Write a function `draw_court()` that draws with Turtle graphics a basketball court as in this image. You do not have to use these same colours, but you must use at least 2 distinct colours to fill some regions of the court. Your figure does not have to be identical to mine, but it should be close enough.
>编写一个函数“draw_court()”，使用 Turtle 图形绘制篮球场，如图所示。您不必使用相同的颜色，但必须使用至少 2 种不同的颜色来填充球场的某些区域。您的图形不必与我的完全相同，但应该足够接近。
```python
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
```

11. Write a function` alogical(n)` , that takes as input a number, n, where n is bigger or equal to 1, and returns the minimum number of times that n needs to be divided by 2 in order to get a number equal or smaller than 1. For example 5.4/2=2.7. Since 2.7 is bigger than 1, dividing 5.4 once by 2 is not enough, so we continue. 2.7/2=1.35 thus dividing 5.4 twice by 2 is not enough since 1.35 is bigger than 1. So we continue. 1.35/2=0.675. Since 0.675 is less than 1, the answer is 3. In particular, these calculations determine that 5.4 needs to be divided by 2 three times minimum in order to get a number that is less than or equal to 1. See Section 2 for more examples. Recall that you may not use loops nor if/branching statements
>编写一个函数 ` alogical(n)` ，以数字 n 作为输入，其中 n 大于或等于 1，并返回为得到小于或等于 1 的数字，n 需要除以 2 的最少次数。例如 5.4/2=2.7。由于 2.7 大于 1，将 5.4 除以 2 一次是不够的，因此我们继续。2.7/2=1.35，因此将 5.4 除以 2 两次是不够的，因为 1.35 大于 1。因此我们继续。1.35/2=0.675。由于 0.675 小于 1，所以答案是 3。具体来说，这些计算确定 5.4 需要至少除以 2 三次才能得到小于或等于 1 的数字。有关更多示例，请参阅第 2 节。回想一下，你不能使用循环或 if/分支语句

```python
def alogical(n):
    '''
    n -> any float number grreat then or equals to 1
    '''
    return math.ceil(math.log2(n))
```

12. Write a function `cad_cashier(price,payment)` that takes two real non-negative numbers with two decimal places as input, where payment>=price and where the second decimal in payment is 0 or 5. They represent a price and payment in Canadian dollars. The function should return a real number with 2 decimal places representing the change the customer should get in Canadian dollars. Recall that in Canada, while the prices are expressed in pennies, the change is based on rounding to the closest 5 cents. See the examples in Section 2 for clarification and examples on how your function must behave
>编写一个函数“`cad_cashier(price,payment)`”，该函数接受两个带有两位小数的非负实数作为输入，其中 `payment>=price`，payment 中的第二位小数为 0 或 5。它们表示以加元表示的价格和付款。该函数应返回一个带有 2 位小数的实数，表示客户应得到的加元零钱。回想一下，在加拿大，虽然价格以美分表示，但零钱是基于四舍五入到最接近的 5 美分。请参阅第 2 节中的示例，以了解您的函数必须如何表现

```python
def cad_cashier(price,payment):
    '''
    (number,number) -> two non-negative floatingt-point number with two decimal places, and the second decimal in payment is 0 or 5.
    where payment >= price
    '''
    a = payment - price
    return(round((round(a * 20) / 20),2))
```

13. Suppose that a cashier in Canada owes a customer some change and that the cashier only has coins `ie. toonies`, loonies, quarters, dimes, and nickels. Write a function that determines the minimum number of coins that the cashier can return. In particular, write a function `min_CAD_coins(price,payment)` that returns five numbers (t,l,q,d,n) that represent the smallest number of coins (toonies, loonies, quarters, dimes, and nickels) that add up to the amount owed to the customer (here price and payment are defined as in the previous question). You program must first call cad_cashier function, from question 13, to determine the amount of change that needs to be returned. Then before doing anything else, you may want to convert this amount entirely to cents (that should be of type int). Once you have the total number of cents here are some hints on how to find the minimum number of coins
>假设加拿大的收银员欠客户一些零钱，而收银员只有硬币，即两元硬币、一元硬币、四分之一元硬币、一角硬币和五分硬币。编写一个函数来确定收银员可以退还的最小硬币数量。具体来说，编写一个函数 `min_CAD_coins(price,payment)`，返回五个数字 (t,l,q,d,n)，这些数字代表加起来等于欠客户的金额的最小硬币数量（两元硬币、一元硬币、四分之一元硬币、一角硬币和五分硬币）（此处 price 和 payment 的定义与上一个问题相同）。您的程序必须首先调用问题 13 中的 cad_cashier 函数来确定需要退还的零钱数量。然后在做任何其他事情之前，您可能需要将此金额完全转换为美分（应该是 int 类型）。一旦您有了美分总数，以下是一些关于如何找到最小硬币数量的提示

```python
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
```


## Reference\
Question10:Python笔记之通过turtle库绘制图形（详细介绍turtle库的函数方法）!https://blog.csdn.net/qq_44437695/article/details/104762815
mine: t.fillcolor("yellow")

Question 11: `ChatGPT`
```python
return math.ceil(math.log2(n))
```

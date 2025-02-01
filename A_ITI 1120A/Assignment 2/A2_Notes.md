# Part1_1
## 1.1.1
`elementary_school_quiz`: This function has two parameters, namely an integer flag that takes only values 0 or 1 and an integer n that takes only values 1 or 2. If flag is 0, `elementary_school_quiz` helps practice the inverse of exponentiation i.e. logarithm. But if flag is 1, `elementary_school_quiz` helps practice exponentiation. In both cases only questins with base 2 will be asked. The function, `elementary_school_quiz` then generates n math problems that a pupil must answer in turn. For each question, it generates one random number between 0 and 10 inclusively (check out python’s random module to see if there’s a useful function in there) and asks the pupil for the 2 answer to the math problem with the random number. Specifically, if flag is 0 and random number generated is, for example, 5 the question asked should be: “2 to what is 32 i.e. what is the result of log2 (32)?”. (The reason 32 is picked is because 25 = 32. See section 3 for more examples. If flag is 1 and random number generated is, for example, 6 the question asked should be: “What is the result of 26?” `elementary_school_quiz` then prompts the pupil for the answer, and checks if her answer is correct. At the end of n questions, `elementary_school_quiz` returns the number of questions answered correctly
>`elementary_school_quiz`：该函数有两个参数，一个是整数 `flag`，它只接受值 0 或 1，另一个是整数 `n`，它只接受值 1 或 2。如果 `flag` 为 0，`elementary_school_quiz` 帮助练习指数的逆运算，即对数。但如果 `flag` 为 1，`elementary_school_quiz` 帮助练习指数运算。无论哪种情况，问题的底数都为 2。函数 `elementary_school_quiz` 然后生成 `n` 个数学问题，学生需要依次作答。对于每个问题，函数生成一个介于 0 到 10（含 0 和 10）之间的随机数（可以查阅 Python 的 `random` 模块，看看里面是否有有用的函数），并让学生回答与该随机数相关的数学问题。具体来说，如果 `flag` 为 0，并且生成的随机数是 5，那么问题应该是：“2 的多少次方等于 32，即 log₂(32) 的结果是多少？”。（选取 32 的原因是因为 2⁵ = 32。请参阅第 3 节获取更多示例。）如果 `flag` 为 1，并且生成的随机数是 6，那么问题应该是：“2⁶ 的结果是多少？”。`elementary_school_quiz` 然后提示学生输入答案，并检查其答案是否正确。在 `n` 道题结束后，`elementary_school_quiz` 返回学生答对的题目数。
```python
# Copyright Haojian Wang all reserved
# 第一种方式
import random
def elementary_school_quiz(flag,n):
    random_num1 = random.randrange(0,10)
    random_num2 = random.randrange(0,10)
    correct = 0
    
    if n == 1:
        if flag == 0:
            answer1 = int(input(f"Question 1: \n 2 to what is {2**random_num1} i.e. what is the result of log_2({2**random_num1})?"))
            if answer1 == random_num1:
                correct = correct + 1

        elif flag == 1:
            answer2 = int(input(f"Question 1: \n What is the result of 2^{random_num1}?"))
            if answer2 == 2**random_num1:
                correct = correct + 1

    if n == 2:
        if flag == 0:
            answer1 = int(input(f"Question 1: \n 2 to what is {2**random_num1} i.e. what is the result of log_2({2**random_num1})?"))
            answer2 = int(input(f"Question 2: \n 2 to what is {2**random_num2} i.e. what is the result of log_2({2**random_num2})?"))
            if (answer1 == random_num1 and answer2 == random_num2):
                correct = correct + 2
            elif (answer1 == random_num1 or answer2 == random_num2):
                correct = correct + 1
            else:
                correct = 0
                

        if flag == 1:
            answer1 = int(input(f"Question 1: \n What is the result of 2^{random_num1}?"))
            answer2 = int(input(f"Question 2: \n What is the result of 2^{random_num2}?"))
            if (answer1 == (2**random_num1) and answer2 == (2**random_num2)):
                correct = correct + 2
            elif (answer1 == (2**random_num1) or answer2 == (2**random_num2)):
                correct = correct + 1
            else:
                correct = 0
                
    return correct

```


```python
# Copyright Haojian Wang all reserved
# 第二种方式
def elementary_school_quiz(flag, n):
'''
flag->number of 0 or 1
n->number of 1 or 2
correct->int, this is to account how many questions you answer correctly
'''
# Your code for elementary_school_quiz function goes here (instead of keyword pass)
# Your code should include  dosctrings and the body of the function
#
# Preconditions: flag is 0 or 1, n is 1 or 2
correct = 0
question_number = 1
for _ in range(n):
    a1 = random.randrange(0,10)
    if flag == 0:
        answer1 = int(input(f"Question {question_number}: \n 2 to what is {2**a1} i.e. what is the result of log_2({2**a1})?"))
        if answer1 == a1:
            correct = correct + 1
    elif flag == 1:
        answer2 = int(input(f"Question {question_number}: \n What is the result of 2^{a1}?"))
        if answer2 == 2**a1:
            correct = correct + 1
    question_number += 1

    return correct
    pass
```
## 1.1.2
`high_school_quiz`: This function has three parameters representing three real numbers for the coefficients of the quadratic equation ax2 + bx + c = 0. The function displays/prints the equation frist and then prints its solutions. The function must display correct and meaningful solutions given any three real numbers for coefficients a, b and c. See examples in Section 3 to understand what that means. Please consider the examples to be a part of the function/program specifications that must be followed. Do not use Python’s complex numbers class to solve this problem
>`high_school_quiz`：此函数有三个参数，代表二次方程 ax2 + bx + c = 0 的系数的三个实数。该函数首先显示/打印方程，然后打印其解。给定系数 a、b 和 c 的任意三个实数，该函数必须显示正确且有意义的解。请参阅第 3 节中的示例以了解其含义。请将示例视为必须遵循的函数/程序规范的一部分。请勿使用 Python 的复数类来解决这个问题

- 先判断是否有解
	- 是：则输出是两个解还是一个解
	- 否：判断是否有复数根


```python
# Copyright Haojian Wang all reserved
import math

def high_school_quiz(a, b, c):
    # 如果 a = 0，处理为线性或特殊情况
    if a == 0:
        if b == 0:
            if c == 0:
                print(f"The quadratic equation {a}·x + {b} = {c} is satisfied for all numbers x")
            else:
                print(f"The quadratic equation {a}·x + {c} = 0 is satisfied for no number x")
        else:
            # 线性方程: bx + c = 0
            root = -c / b
            print(f"The quadratic equation {b}·x + {c} = 0 has the following real root: {root}")
        return
    
    # 计算判别式
    delta = b**2 - 4*a*c
    
    # 打印方程
    print(f"The quadratic equation {a}·x^2 + {b}·x + {c} = 0", end=" ")
    
    # 判断判别式
    if delta > 0:
        # 两个不同的实数根
        root1 = (-b + math.sqrt(delta)) / (2 * a)
        root2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"has the following real roots: {root1} and {root2}")
    elif delta == 0:
        # 一个实根
        root = -b / (2 * a)
        print(f"has only one solution, a real root: {root}")
    else:
        # 复数根
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-delta) / (2 * a)
        print(f"has the following two complex roots: {real_part} + i {imaginary_part} and {real_part} - i {imaginary_part}")

```

# Part1_2
Now that you have the two functions that perform the core functionality, you want to make it more user friendly for the pupils (after all, alas, the pupil may not know how to write code and call functions in Python shell). In the main part of your program, write your code in speciﬁed places. You code must follow the behaviour indicated in the example runs in Section 3. For example, for elementary school pupils, called Mia, you will ﬁrst ask her whether she would like to practice
exponentiation or its inverse. Then ask her how many practice questions she’d like (if she says 0, then your code should not ask her to solve any math questions). Using her responses, call the `elementary_school_quiz` function with the appropriate values. When it returns the number of correct answers, display a message to the pupil:
• If she go all questions correctly display on screen: Congratulations Mia! You’ll probably get an A tomorrow. Good bye Mia!
• If she got half of them correctly display on screen: You did ok Mia, but I know you can do better. Goodbye Mia!
• If she did all incorrectly, display on screen: I think you need some more practice Mia. Good bye Mia!
For high school pupils, in the main part of your program in the speciﬁed places, you need to write some code that asks the pupil for the coeﬃcients a, b and c. Then you need to make the call to `high_school_quiz` to display the solutions. After that your program should ask the pupil if they would like another quadratic equation solved. If the pupil says anything but yes the program terminates by printing a good bye message as in the examples. Otherwise, as long as pupil answers yes (and any form of typing yes should be acceptable, including with lots of white space before and after, and with capital letters and lower case letter etc), she should be asked for the coeﬃcients again and the resulting new quadratic equation should be solved. Since you have not seen while loops yet, I provided the code for that in a2_part1_xxxxxx.py. The rest of the speciﬁcations for your program in Part 1 can be inferred from examples in Section 3. You will notice
that the program is required to display greetings surrounded with stars. You may write a separate function for that.
>现在您有了两个执行核心功能的函数，您希望让学生对它更加友好（毕竟，学生可能不知道如何在 Python shell 中编写代码和调用函数）。在程序的主要部分，在指定的位置编写代码。您的代码必须遵循第 3 节中示例运行中指示的行为。例如，对于名叫 Mia 的==小学生==，您将首先询问她是否愿意练习
指数运算或其逆运算。然后问她想要多少练习题（如果她说 0，那么您的代码就不应该要求她解答任何数学问题）。使用她的回答，使用适当的值调用 `elementary_school_quiz` 函数。当它返回正确答案的数量时，向学生显示一条消息：
• 如果她正确回答了所有问题，屏幕上会显示：恭喜 Mia！明天你可能会得到 A。再见 Mia！
• 如果她答对了一半，屏幕上会显示：你还行，米娅，但我知道你可以做得更好。再见，米娅！
• 如果她全部答错，屏幕上会显示：我觉得你需要多练习一下，米娅。再见，米娅！
对于==高中生==，在程序主体部分指定的位置，你需要编写一些代码，要求学生输入系数 a、b 和 c。然后你需要调用 `high_school_quiz` 来显示解决方案。之后，你的程序应该询问学生是否想要求解另一个二次方程。如果学生没有回答“是”，程序就会像示例中那样打印一条再见消息并终止。否则，只要学生回答“是”（任何形式的“是”输入都应该可以接受，包括前后留有大量空白，以及使用大写字母和小写字母等），就应该再次要求她输入系数，并求解由此产生的新二次方程。由于您还没有看到 while 循环，我在 a2_part1_xxxxxx.py 中提供了该循环的代码。第 1 部分中程序的其余规范可以从第 3 节中的示例推断出来。您会注意到
程序需要显示用星星包围的问候语。您可以为此编写一个单独的函数。

```python
# Copyright Haojian Wang receives
# main

# your code for the welcome tmessage goes here
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

ascii_name_plaque("Welcome to my math quiz-generator")

name=input("What is your name? ")

status=input("Hi "+name+". Are you in? Enter \n1 for elementary school\n2 for high school or\n3 or other character(s) for none of the above?\n")


if status=='1': # for elementary school
    # your code goes here
    ascii_name_plaque(f"{name}, welcome to my quiz-generator for elementary school students")

    ele_choice = int(input(f"{name} what would you like to practice? Enter \n 0 for inverse of exponentiation \n 1 for exponentaiation \n"))
    if (ele_choice == 0) or (ele_choice == 1):
        n = float(input("How many practice questions would you like to do? Enter 0, 1, or 2: "))
        if n == 0:
            print("Zero questions. OK. Good bye")
        elif n == 1:
            if elementary_school_quiz(ele_choice, n) == 1:
                print(f"Congratulations {name}! You’ll probably get an A tomorrow. Good bye Mia!")
        elif n == 2:
            if elementary_school_quiz(ele_choice, n) == 2:
                print(f"Congratulations {name}! You’ll probably get an A tomorrow. Good bye Mia!")
            elif elementary_school_quiz(ele_choice, n) == 1:
                print(f"You did ok {name}, but I know you can do better. Goodbye Mia!")
            else:
                print(f"I think you need some more practice {name}. Good bye Mia!")
        else:
            print("Only 0,1, or 2 are valid choices for the number of questions.")
    else:
        print("Invalid chose. Only 0 or 1 is accepted.")
    pass

elif status=='2': # for high school
    # your code for welcome message
    ascii_name_plaque(f"quadratic equation, a·x^2 + b·x + c= 0, solver for {name}")

    flag=True
    while flag:
        question=input(name+", would you like a quadratic equation solved? ")
        
        # your code to handle varous form of "yes" goes here
        question = question.replace(" ","").lower()
        
        if question != "yes":
            flag=False
        else:
            print("Good choice!")
            a = float(input("Enter a number the coefficient a:"))
            b = float(input("Enter a number the coefficient b:"))
            c = float(input("Enter a number the coefficient c:"))
            high_school_quiz(a,b,c)
            # your code goes here (i.e ask for coefficients a,b and c and call)
            # then make a function call and pass to the fucntion
            # the three coefficients the pupil entered
 
else:
    print(f"{name} you are not a target audience for this software.Good bye {name}!")
    # your code goes here
    pass

print("Good bye "+name+"!")

```

# Part2_1
`min_enclosing_rectangle(radius, x, y)` - 5 points Computing a smallest (axis-aligned) rectangle that encloses a set of objects in the plane is a very common computational problem arising in graphics and thus game development too. Write a function, called `min_enclosing_rectangle`, that has 3 input parameters. The first is a number representing a radius of a circle and the next two are two numbers representing the x- and y-coordinates of its center. Consider the smallest axis-aligned rectangle that contains that circle. The function should return the x- and y-coordinates of the bottom-left corner of that rectangle. If radius is a negative number, `min_enclosing_rectangle` should return None.
>`min_enclosing_rectangle(radius, x, y)` 5 分计算一个最小（轴对齐）矩形，该矩形包围平面中的一组对象，是图形学和游戏开发中非常常见的计算问题。编写一个名为 `min_enclosing_rectangle` 的函数，该函数有 3 个输入参数。第一个是表示圆半径的数字，接下来的两个是两个表示其中心的 x 和 y 坐标的数字。考虑包含该圆的最小轴对齐矩形。该函数应返回该矩形左下角的 x 和 y 坐标。如果 radius 是负数，则 `min_enclosing_rectangle` 应返回 None。

```python
def min_enclosing_rectangle(radius,x,y):
    '''
    radius,x,y -> float number
    radius should be >= 0, otherwise it will return None
    '''
    if radius >= 0:
        return (x - radius, y - radius)
    else:
        return None
```

# Part2_2
Write a function called vote_percentage that takes a string as input. The function has one input parameter, called results. Your function should count the number of substrings ’yes’ in the string results and the number of substrings ’no’ in the string results, and it should return the percentage of ’yes’ (among all ’yes’ and ’no’). (You may assume that string results has at least one yes or no and that the only words present are yes, no and/or abstained).
Hint: you may use count method from Python’s str module/library.
>编写一个名为 `vote_percentage` 的函数，该函数接受一个字符串作为输入。这个函数有一个输入参数，名为 `results`。你的函数应该统计字符串 `results` 中子字符串 `yes` 的数量，以及子字符串 `no` 的数量，然后返回 `yes` 在所有 `yes` 和 `no` 中所占的百分比。（你可以假设字符串 `results` 至少包含一个 `yes` 或 `no`，并且该字符串只包含单词 `yes`, `no` 和/或 `abstained`）。
提示：你可以使用 Python 字符串模块/库中的 `count` 方法。
```python
def vote_percentage(results):
    '''
    results -> string
    only has 'yes', 'no', and 'abstained'. And only count the numbers of yes and no
    '''
    y = results.count('yes')
    n = results.count('no')
    return y/(y+n)
```

# Part2_3
If there is a vote at a meeting, there are several possible outcomes based on the number of yes and no votes (abstains are not counted). If all the votes are yes, then the proposal passes "unanimously", if at least 2/3 of the votes are yes, then the proposal passes with "super majority", if at least 1/2 of the votes are yes, then the proposal passes by "simple majority", and otherwise it fails. Write a function called vote that asks a user to enter all yes-s and no-s and abstained-s and then press enter. The function then prints the outcome of the vote. You solution must involve making a call to function vote_percentage (You may assume that the user will enter at least one yes or no and that the only words present are yes, no and/or abstained)
>如果在会议上进行投票，根据 `yes` 和 `no` 票的数量可能有几种不同的结果（弃权票不计算内）。如果所有的票都是 `yes`，那么提案通过并且结果为“全体一致通过”（unanimously）；如果至少有 2/3 的票数为 `yes`，则提案以“超级多数”（super majority）通过；如果至少有 1/2 的票数为 `yes`，则提案以“简单多数”（simple majority）通过，否则提案失败。编写一个名为 `vote` 的函数，该函数要求用户输入所有的 `yes`、`no` 和 `abstained`，然后按回车键。该函数随后输出投票结果。你的解决方案必须调用 `vote_percentage` 函数（你可以假设用户至少输入一个 `yes` 或 `no`，并且输入的内容只包含 `yes`、`no` 和/或 `abstained`）。

```python
def vote():
    '''
    r are the strings
    '''
    r = str(input("Enter the yes, no, abstained votes one by one and then press enter:"))
    if vote_percentage(r) == 1:
        print ("proposal passes unanimously")
    elif 2/3 < vote_percentage(r) < 1:
        print ("proposal passes with super majority")
    elif 1/2 < vote_percentage(r) < 2/3:
        print ("proposal passes with simple majority")
    else:
        print ("proposal fails")
```
# Part2_4
Write a function called `l2lo(w)` that takes a non-negative number w as input and returns a pair of numbers `(l,o)` such that `w = l + o/16` and l is an integer and o is a non-negative number smaller than 16. Note that the solution l and o are unique.
>编写一个名为 `l2lo(w)` 的函数，该函数接受一个非负数 `w` 作为输入，并返回一对数字 `(l, o)`，使得 `w = l + o/16`，其中 `l` 是一个整数，`o` 是一个小于 16 的非负数。注意，`l` 和 `o` 的解是唯一的。
```python
def l2lo(w):
    '''
    w -> float
    return l -> int, o -> float
    '''
    l = int(w // 1)
    o = (w - l) * 16
    return (l,o)
```
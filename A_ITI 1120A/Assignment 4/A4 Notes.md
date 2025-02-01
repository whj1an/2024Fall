In this assignment you may not use any of the following:
– dictionaries, sets
– keywords break and continue
– global variables in bodies of functions

# Part 1

## 1.1 `number_divisible()`

Implement a Python function named `number_divisible` that takes a list of integers and a integer n as input parameters and returns the number of elements in the list that are divisible by n. Then, in the main, your program should ask the user to input integers for the list and an integer for n, then it should call the function `number_divisible`, and print the result. In this question you may assume that the user will follow your instructions and enter a sequence of integers separated by spaces for the list and an integer for n. You can use str method . strip and . split to handle the user input. Here is a way to ask a user for a list: `raw_input ("Please input a list of numbers separated by space: " ).strip( ).split()`. But now `raw_input` is a list of strings that look like integers so you need to create a new list that is a list of equivalent integers.

> 实现一个名为number_divisible的Python函数，该函数以整数列表和整数n作为输入参数，并返回列表中可被n整除的元素数。然后，在主进程中，您的进程应要求用户输入列表的整数和n的整数，然后它应调用函数number_divisible并打印结果。在这个问题中，您可以假设用户将按照您的指示输入列表的整数串行和n的整数，并用空格分隔。您可以使用str方法.strip和.split来处理用户输入。以下是要求用户提供列表的一种方法：`raw_input ("Please input a list of numbers separated by space: " ).strip( ).split()`但是现在raw_input是一个看起来像整数的字符串列表，因此您需要创建一个新的列表，它是一个等效整数列表。

Function call example:

```python
>>>number_divisible([6, 10, 2, 3, 4, 5, 6, 0], 3)
4
```

An example run of the program:

```
Please input a list of integers separated by spaces: 1 2 3 0 5 -6 995
Please input an integer: 2
The number of elements divisible by 2 is 3
```

### ANSWER

```python
def number_divisible(l,n):
    '''(list,int)->int
    if you just call this function please enter a list and then a intager,
    divided them by ","
    if just run it you will get some Text issues
    '''
    count = 0
                
    new_l = []
    for element in l:
        element = int(element)
        new_l.append(element)
    
    for i in new_l:
        if i % n == 0:
            count += 1
    return count

#main
l = input("Please input a list of numbers separated by space: " ).strip( ).split()
n = int(input("Please input an integer: ").strip())
result = number_divisible(l,n)
print(f"The number of elements divisible by {n} is {result}")
```



## 1.2 `two_length_run`

A run is a sequence of consecutive repeated values. Implement a Python function called `two_length_run` that takes a list of numbers as input parameter and returns True if the given list has at least one run (of length at least two), and False otherwise. Make sure the function is efficient (i.e. it stops as soon as the answer is known). Then, in the ma i n, your program should ask the user to input the list, then it should call `two_length_run` function, and print the result. You can obtain a list of numbers from the user as explained in Question 1.

> 运行是连续重复值的串行。实现一个名为 two length_run 的 Python 函数，该函数以数字列表作为输入参数，如果给定列表至少有一个运行（长度至少为 2），则返回 True，否则返回 False。确保该函数是有效的（即，一旦知道答案，它就会停止）。然后，在主进程中，您的进程应该要求用户输入列表，然后它应该调用 two length_run 函数，并打印结果。您可以按照问题 1 中的说明从用户那里获取数字列表。

Four examples of program runs:

```python
Please input a list of numbers separated by space: 1    4 3 3 4
True
Please input a list of numbers separated by space: 1 2 3 3   3 4.5 6 5
True
Please input a list of numbers separated by space: 1.0 2 3.7 4 3 2
False
Please input a list of numbers separated by space: 7.7
False
```

Function call examples:
```pyhton
>>> two_length_run( [2.7, 1.0, 1.0, 0.5, 3.0, 1.0] )
True
>>>
>>> two_length_run([1.0,1])
True
```

### ANSWER

```python
def two_length_run(l):
    '''(list)->boolean
    you should enter a list of numbers and judge does it appear two same numbers continuely
    length at least 2
    '''
    new_l = []
    for element in l:
        element = float(element)
        new_l.append(element)

    length = len(new_l)
    for i in range(length - 1):
        if new_l[i] == new_l[i+1]:
            return True
    return False

l = input("Please input a list of numbers separated by space: ").strip().split()
print(two_length_run(l))
```



## 1.3

As mentioned, a run is a sequence of consecutive repeated values. Implement a Python function called `longest_run` that takes a list of numbers and returns the length of the longest run. For example in the sequence: 2, 7, 4, 4, 2, 5, 2, 5, 10, 12, 5, 5, 5, 5, 6, 20, 1 the longest run has length 4. Then, in the main, your program should ask the user to input the list, then it should call longest_run function, and print the result. You can obtain a list of numbers from the user as explained in Question l.

> 如上所述，运行是连续重复值的串行。实现一个名为“longest_run”的 Python 函数，该函数接受一个数字列表并返回最长运行的长度。例如，在串行中：2、7、4、4、2、5、2、5、10、12、5、5、5、5、6、20、1 最长运行的长度为 4。然后，在主进程中，您的进程应要求用户输入列表，然后它应调用 longest_run 函数并打印结果。您可以按照问题 l 中的说明从用户那里获取一个数字列表。

Five examples of program runs:

```python
Please input a list of numbers separated by space: 1 1 2 3.0 3 3 3 3 6 5
5
Please input a list of numbers separated by space: 6 6 7 1 1 1 1 4.5 1
4
Please input a list of numbers separated by space: 6 2.4 4 8 6
1
Please input a list of numbers separated by space: 3
1
Please input a list of numbers separated by space:
0
```

Function call example:

```python
longest_run([6, 6, 7, 1.0, 1.0, 1.0, 1, 4.5, 1])
4
```

### ANSWER

```python
def longest_run(l):
    '''(list)->int
    counter the longest numbers of the run, if no runs returns 1
    if empty return 0.
    '''
    # if empty returns 0
    if l == []:
        return 0
    
    # initialize length
    initial_len = 1 
    max_len = 1

    # set all elements to float
    new_l = [] 
    for element in l:
        element = float(element)
        new_l.append(element)

    # counters
    length = len(new_l)
    for i in range(1, length):
        if new_l[i] == new_l[i-1]:
            initial_len += 1
        else:
            if initial_len > max_len:
                max_len = initial_len
            initial_len = 1 # initialize
            
    # check the last comparing
    if initial_len > max_len:
        max_len = initial_len
        
    return max_len

# main
l = input("Please input a list of numbers separated by space:").strip().split()
print(longest_run(l))
```

## 1.4 

In the questions you are provided with starter code `a4_Q4_xxxxxx.py` and 5 files: `file1.txt` ... `file5.txt`. As usual you cannot modify the given parts of the code. For this question you need to code the two missing functions `clean_up` and `is_rigorous` What these functions should do is described in the docstrings. Some test cases for these two functions can also be found in the docstrings. The provided program asks for the name of a file. The files your program will be tested with will have one character per line (like bo1.txt). Then the function `read_raw` returns a list of characters from the file.

> 在问题中，你会得到起始代码“a4_Q4_xxxxxx.py”和 5 个文档：“file1.txt”...“file5.txt”。像往常一样，你不能修改代码的给定部分。对于这个问题，你需要编写两个缺失的函数 `clean_up` 和 `is_rigorous`。这些函数应该做什幺在文档字符串中描述。这两个函数的一些测试用例也可以在文档字符串中找到。提供的进程要求输入一个文档的名称。将用来测试你的进程的文档每行有一个字符（如 bo1.txt）。然后函数 `read_raw` 返回文档中的字符列表。

RUN 1:

```python
Enter the name of the file: file1.txt
Before clean-up:
['D','F','B','G','$','$','$','A','A','C','G','D','A','$','C','*','P','E','D','*','D','D','E','B','$','#','D','D']
After clean-up:
['$', '$', '$', '$', 'A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'D', 'D', 'D', 'D', 'E', 'E', 'G', 'G']
This list has no * but is not rigorous and it has 20 characters.
RUN 2:
Enter the name of the file: file2.txt
Before clean-up:
['A', '*', '$', 'C', '*', '*', 'P', 'E', 'D', 'D', '#', 'D', 'E', 'B', '$', '#']
After clean-up:
['#', '#', '$', '$', 'D', 'D', 'E', 'E']
This list is now rigorous; it has no * and it has 8 characters.
RUN 3:
Enter the name of the file: file3.txt
Before clean-up:
['A', 'B', '*', 'C', '*', 'D', '*', '*', '*', 'E']
After clean-up:
[]
This list is now rigorous; it has no * and it has 0 characters.
RUN 4:
Enter the name of the file: file4.txt
Before clean-up:
['A', 'A', 'A', 'A', 'A', 'A', 'A']
After clean-up:
['A', 'A', 'A', 'A', 'A', 'A']
This list has no * but is not rigorous and it has 6 characters.
RUN 5:
Enter the name of the file: file5.txt
Before clean-up:
[]
After clean-up:
[]
This list is now rigorous; it has no * and it has 0 characters.
```

### ANSWER

```python

def read_raw(file):
    '''str->list of str
    Returns a list of strings that was stored in a file.'''
    raw = open(file).read().splitlines()
    for i in range(len(raw)):
        raw[i]=raw[i].strip()
    return raw


def clean_up(l):
    '''list of str->list of str

    The functions takes as input a list of characters.
    It returns a new list containing the same characters as l except that
    one of each characters that appears odd number of times in l is removed
    and all the * characters are removed

    >>> clean_up(['A', '*', '$', 'C', '*', '*', 'P', 'E', 'D', 'D', '#', 'D', 'E', 'B', '$', '#'])
    ['#', '#', '$', '$', 'D', 'D', 'E', 'E']

    >>> clean_up(['A', 'B', '*', 'C', '*', 'D', '*', '*', '*', 'E'])
    []
    '''
    clean_board=[]
    # remove all the *
    for char in l:
        if char != '*':
            clean_board.append(char)

    # remove the character which appears odd times
    for char in l:
        if char != '*' and l.count(char) % 2 == 1:
            if clean_board.count(char) % 2 == 1:
                clean_board.remove(char)
    # Sorting
    clean_board.sort()
    
    return clean_board
    


def is_rigorous(l):
    '''list of str->bool
    Returns True if every character in the list appears exactlly 2 times or the list is empty.
    Otherwise, it returns False.

    Precondition: You may assume that every element in the list appears even number of times
    (i.e. that the list is clean-up by clean_up function)

    >>> is_rigorous(['E', '#', 'D', '$', 'D', '$', 'E', '#'])
    True
    >>> is_rigorous(['A', 'B', 'A', 'A', 'A', 'B'])
    False
    '''
    if l == []:
        return True
    for char in l:
        if l.count(char) != 2:
            return False
    return True

    
#main
file=input("Enter the name of the file: ")
file=file.strip()
b=read_raw(file)
print("\nBefore clean-up:\n", b)
b=clean_up(b)
print("\nAfter clean-up:\n", b)
if is_rigorous(b):
    print("\nThis list is now rigorous; it has no * and it has "+str(len(b))+" characters.")
else:
    print("\nThis list has no * but is not rigorous and it has "+str(len(b))+" characters.")
     
```

# Part 2

You will implement the two player version. One player will be the computer (i.e. your program) and the other a user of your program. In what follows, let's refer to the computer player as Robot and user player as Human. You may assume that Robot will always deal the cards.As part of this assignment I provided the file called `a4_GAME_xxxxxx.py`. Replace xxxxxx in the file name with your student number. You should open that file and run it to see what it does already. All of your code must go inside of that file. The file already has some functions that are fully coded for you and other functions for which only docstrings and partial or no code are provided. Designing your program by decomposing it into smaller subproblems (to be implemented as functions) makes programming easer, less prone to errors and makes your code more readable. No part of the given code can be changed. Your code must go into clearly indicated places. No code can be added to the main. You can design some extra functions of your own if you like. Functions `make_deck`, `wai` and `shuff_Ie_deck` are already fully coded for you. You need to develop the remaining functions: `deal_cards`, `remove_pairs`, `print_deck`, `get_valid_input`, and `play_game`. The functions must meet the requirements as specified in their docstrings (and as implied by the exam- ple program runs below and as implied by the video instructions).The main bulk of your code (the game playing part) will go into the function called `play_game`. That function should use/ call the other functions that you are required to develop (i.e. `deal_cards`, `remove_pairs`, `print_deck`, and `get_valid_input`).When developing function `get_valid_input` you may assume that Human will enter integer when asked for an integer, but you may not assume that it will be in the correct range. The function gets the input from Human about which face-down card of Robot it wants. When it is Robot's turn to play you must implement it such that Robot takes a random card from Human. Also recall that what Human calls 3rd card, for example, is in position/ index 2 in Robot's deck (as it is represented by a list).Study the example of the program run below carefully to understand how your program should behave. The be- haviour of the program that you see in the run is required —s all aspects of it. Also watch the video I made to get even better idea of how your program must behave. The video demo can be found here: https://youtu.be/mMBApSkvHyM

​	Some Suggestions:

- Study the provided code and understand what it does and how it should be used.

- Spend some time thinking about various parts of the game that need to be implemented. For example, it needs to be able to display Human’s deck to Human, it needs to be able to ask Human for what card she wants, it needs to be able to remove pairs from either Human or Robot’s deck ... etc. The provided functions do quite of bit of that job for you.

- When you are coding individual functions recall that you can test each function in the shell without finishing the remaining functions. For example, when implementing function remove_pairs you can test it in the shell by typing something like:
  ```
  >>> remove_pairs(['10♣', '2♣', '5q', '6♣', '9♣, 'Aq', '10q'])
  The shell should display (with cards not necessarily in this order):
  ['2♣', '5q', '6♣', '9♣', 'Aq']
  ```

  Thus you can code and test your functions one by one (without completing the other parts)

- The game alternates between Robot and Human. Think about how you can represent whose turn it is to play, in your program. One way is to have a variable that you set to zero when it is Robot’s turn and to one when it is Human’s turn. You also need to figure out what to test to see if the game is over

> 您将实现双人版本。一个玩家将是计算机（即您的进程），另一个玩家将是进程的用户。在下文中，我们将计算机玩家称为机器人，将用户玩家称为人类。您可以假设机器人将始终发牌。作为此作业的一部分，我提供了名为“a4_GAME_xxxxxx.py”的文档。将文档名中的 xxxxxx 替换为您的学生编号。您应该打开该文档并运行它以查看它已经执行的操作。您的所有代码都必须放在该文档中。该文档已经有一些为您完全编码的函数，而其他函数只提供文档字符串和部分代码或没有提供代码。通过将进程分解为较小的子问题（作为函数实现）来设计进程，可以使编程更容易，更不容易出错，并使您的代码更具可读性。给定代码的任何部分都不能更改。您的代码必须放在明确指示的位置。主进程中不能添加任何代码。如果您愿意，您可以设计一些自己的额外功能。函数“make_deck”、“wai”和“shuff_Ie_deck”已为您完全编码。您需要开发其余函数：“deal_cards”、“remove_pairs”、“print_deck”、“get_valid_input”和“play_game”。这些函数必须满足其文档字符串中指定的要求（以及下面运行的示例进程和视频说明中暗示的要求）。代码的主要部分（游戏部分）将进入名为`play_game`的函数。该函数应使用/调用您需要开发的其他函数（即“deal_cards”、“remove_pairs”、“print_deck”和“get_valid_input”）。在开发函数“get_valid_input”时，您可以假设当要求输入整数时，人类会输入整数，但您可能不会假设它会在正确的范围内。该函数从人类那里获取关于它想要机器人哪张面朝下的牌的输入。当轮到机器人出牌时，你必须实现它，让机器人从人类那里拿走一张随机牌。另外回想一下，例如，人类所说的第三张牌在机器人牌组的位置/索引为 2（因为它由列表表示）。仔细研究下面进程运行的示例，以了解你的进程应该如何表现。你在运行中看到的进程的行为是必需的——它的所有方面。还可以观看我制作的视频，以更好地了解你的进程必须如何表现。视频演示可以在这里找到：https://youtu.be/mMBApSkvHyM 
>
> 一些建议：
>
> - 研究提供的代码，了解它的作用以及如何使用它。
> - 花点时间思考需要实现的游戏的各个部分。例如，它需要能够向人类展示人类的牌组，它需要能够询问人类她想要什幺牌，它需要能够从人类或机器人的牌组中移除成对的牌……等等。提供的函数为您完成了相当多的工作。
> - 当您编写单个函数时，请记住，您可以在 shell 中测试每个函数，而无需完成其余函数。例如，在实现函数 remove_pairs 时，您可以通过键入以下内容在 shell 中对其进行测试：
>   ``` >>> remove_pairs(['10♣', '2♣', '5q', '6♣', '9♣, 'Aq', '10q']) 壳应该显示（卡片不一定按此顺序）： ['2♣', '5q', '6♣', '9♣', 'Aq'] ``` 因此，您可以逐个编码和测试您的功能（无需完成其他部分）
> - 游戏在机器人和人类之间交替进行。考虑一下如何在进程中表示轮到谁玩。一种方法是设置一个变量，当轮到机器人时将其设置为零，当轮到人类时将其设置为一。您还需要弄清楚要测试什幺来查看游戏是否结束

```python
# In this implementation a card (that is not a 10) is represented
# by a 2 character string, where the 1st character represents a rank and the 2nd a suit.
# Each card of rank 10 is represented as a 3 character string, first two are the rank and the 3rd is a suit.

import random


def wait_for_player():
    '''()->None
    Pauses the program until the user presses enter
    '''
    try:
        input("\nPress enter to continue. ")
        print()
    except SyntaxError:
        pass


def make_deck():
    '''()->list of str
        Returns a list of strings representing the playing deck,
        with one queen missing.
    '''
    deck = []
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    for suit in suits:
        for rank in ranks:
            deck.append(rank + suit)
    deck.remove('Q\u2663')  # remove a queen as the game requires
    return deck


def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck
    '''
    random.shuffle(deck)


#####################################

def deal_cards(deck):
    '''(list of str)-> tuple of (list of str,list of str)

    Returns two lists representing two decks that are obtained
    after the dealer deals the cards from the given deck.
    The first list represents dealer's i.e. computer's deck
    and the second represents the other player's i.e user's list.
    '''
    dealer = []
    other = []

    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
    # YOUR CODE GOES HERE

    length = len(deck)
    for i in range(length):
        if i % 2 == 0:
            dealer.append(deck[i]) #bot's
        else:
            other.append(deck[i]) #Mine
    
    return (dealer, other)


def remove_pairs(l):
    '''
     (list of str)->list of str

     Returns a copy of list l where all the pairs from l are removed AND
     the elements of the new list shuffled

     Precondition: elements of l are cards represented as strings described above

     Testing:
     Note that for the individual calls below, the function should
     return the displayed list but not necessarily in the order given in the examples.

     >>> remove_pairs(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> remove_pairs(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''

    no_pairs = []

    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
    # YOUR CODE GOES HERE

    l.sort() #sorting
    l_length = len(l)
    i = 0 # counter
    while i < l_length - 1: # while loop
        if l[i][:-1] == l[i+1][:-1]:
            i += 2 # press two
        else:
            no_pairs.append(l[i])
            i += 1 # put it into and next one

    #last one if exist
    if i == l_length -1:
        no_pairs.append(l[i])

    # MY CODE ENDS HERE
    
    random.shuffle(no_pairs)
    return no_pairs


def print_deck(deck):
    '''
    (list)-None
    Prints elements of a given list deck separated by a space
    '''

    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
    # YOUR CODE GOES HERE
    print(" ".join(deck))
    # MY CODE ENDS HERE


def get_valid_input(n):
    '''
    (int)->int
    Returns an integer given by the user that is at least 1 and at most n.
    Keeps on asking for valid input as long as the user gives integer outside of the range [1,n]

    Precondition: n>=1
    '''

    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
    # YOUR CODE GOES HERE
    valid_input = False
    while not valid_input:
        choice = input(f"Give me an integer between 1 and {n}: ")
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= n:
                valid_input = True
            else:
                print(f"Invalid number. Please enter an integer between 1 and {n}.")
    # MY CODE ENDS HERE
    return choice

def play_game():
    '''()->None
    This function plays the game'''

    deck = make_deck()
    shuffle_deck(deck)
    tmp = deal_cards(deck)

    dealer = tmp[0]
    human = tmp[1]

    print("Hello. My name is Robot and I am the dealer.")
    print("Welcome to my card game!")
    print("Your current deck of cards is:")
    print_deck(human)
    print("Do not worry. I cannot see the order of your cards")

    print("Now discard all the pairs from your deck. I will do the same.")
    wait_for_player()

    dealer = remove_pairs(dealer)
    human = remove_pairs(human)

    # COMPLETE THE play_game function HERE
    # YOUR CODE GOES HERE
    turn = 0 # 0 -> player, 1 -> bot
    while len(dealer) > 0 and len(human) > 0:
        if turn == 0: # my turn
            print("Your Ture.")
            print("Your current deck of cards is:")
            print_deck(human)
            print(f"I have {len(dealer)} cards. If 1 stands for my first card and {len(dealer)} for my last card, which of my cards would you like?")
            choice = get_valid_input(len(dealer)) - 1
            chosen_card = dealer.pop(choice) # remove the chosen card from dealer
            human.append(chosen_card) # plug it into my card
            print(f"You asked for my {choice + 1}{'st' if (choice + 1) == 1 else 'nd' if (choice + 1) == 2 else 'rd' if (choice + 1) == 3 else 'th'} card. Here it is. It is {chosen_card}")
            human = remove_pairs(human)

        else: # bot turn
            print("My Turn.")
            chosen_card_index = random.randint(0, len(human) - 1)  # pick a card randomly
            chosen_card = human.pop(chosen_card_index) # remove that card from human
            dealer.append(chosen_card)  # plug it into dealer's
            print(f"I took your {chosen_card_index + 1}{'st' if (chosen_card_index + 1) == 1 else 'nd' if (chosen_card_index + 1) == 2 else 'rd' if (chosen_card_index + 1) == 3 else 'th'} card.")
            dealer = remove_pairs(dealer)

        wait_for_player() # WAITTING
        turn = 1 - turn # switch

    if len(human) == 0:
        print("Ups. You do not have any more cards \n Congratulations! You, Human, win")
    else:
        print("Ups. I do not have any more cards \n You lost! I, Robot, win")
    # MY CODE ENDS HERE
# main
play_game()
```


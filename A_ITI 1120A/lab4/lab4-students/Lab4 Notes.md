# Programming exercise: Solved Problem

## File Name: prog_solved_v1.py

```python
def prog_solved_v1():
     name = input("What is your name? ")
     age = int(input("How old are you? "))
     if age<18:
          print(name, ", you are", age, "years old, and thus underage and ineligible to vote")
     else:
          print(name, ", you are", age, "years old, and thus eligible to vote")
     return
```



## File Name: prog_solved_v2.py

```python
def is_eligible(age):
     if age >=18:
          return True
     else:
          return False

def vote():
     name=input("What is your name? ")
     age = int(input("How old are you? "))
     if is_eligible(age):
          print(name, ", you are eligible to vote")
     else:
          print(name, ", you are ineligible to vote") 
```

# Programming exercise 1

Repeat the exercise in the previous question (version 2), where in addition you need to ask the user for their citizenship and if they are currently in prison convicted for a criminal offence. Your program should print a nice message telling the user if they are eligible to vote (i.e. if they are 18+, Canadian and do not live in prison convicted for a criminal offence, then they can vote. Otherwise not). You should modify function is_eligible so it takes to additional paramters as input. In particular the head of the function should be: ` is_eligible(age, citizenship, prison)`

> 重复上一个问题（版本 2）中的练习，此外，您还需要询问用户的国籍以及他们是否因刑事犯罪而被定罪。您的程序应该打印一条友好的消息，告诉用户他们是否有资格投票（即，如果他们年满 18 岁、是加拿大人并且没有因刑事犯罪而被定罪，那么他们就可以投票。否则就不能）。您应该修改函数 is_eligible，以便它接受其他参数作为输入。特别是，函数的头部应该是：is_eligible(age, citizenship, prison)

```python
def is_eligible():
    '''
    name -> String
    age -> intage
    citizenship -> String
    prison -> string, only has no will come out True
    '''
    name= input("Please enter your name: ")
    age = int(input("Please enter you age: "))
    citizenship = input("Please enter you citizneship: ").replace(" ","").lower()
    prison = input("Have you ever lived in prison? ").replace(" ","").lower()
    if (age>=18) and (citizenship=="canada" or citizenship=="canadian") and (prison=="no"):
          print(name, ", you are eligible to vote")
    else:
          print(name, ", you are ineligible to vote")
    return

```

# Programming exercise 2

Write a function called mess that takes a phrase (i.e., a string) as input and then 
returns the copy of that phrase where each character that is one of the last  8 
consonants of English alphabet is capitalized (so,  r, s, t, v, w, x,y , z) and where 
each blank space is replaced by dash.

> 编写一个名为 mess 的函数，以短语（即字符串）作为输入，然后
> 返回该短语的副本，其中英文字母表最后 8 个辅音中的每个字符都大写（因此，r、s、t、v、w、x、y、z），并且
> 每个空格都用破折号替换。

```python
def mess(text):
    result = ""
    last_alpha = ("r,s,t,v,w,x,y,z")
    for char in text:
        if char.lower() in last_alpha:
            result += char.upper()
        elif char == " ":
            result += "-"
        else:
            result += char
    return result
```

# Programming exercise 3

Open the file ex23n8.py. Inside of that file:
1. write a function called print_all_23n8(num), that takes as input a non-negative 
    integer num and prints all the the non-negative numbers smaller than num that  are divisible by 2 or 3 but not 8. You should use the function that is already 
    present in the file (and that you developed for the last lab)

2. Outside of that function ask the user for a non-negative integer. Your program 
    should then print all non-negative numbers that are divisible by 2 or 3 but not 8, by making a call to function print_all_23n8

3. Run your program and test it by entering, for example, 1000 when prompted for a number

> 打开文件 ex23n8.py。该文件内部：
>
> 1. 编写一个名为 print_all_23n8(num) 的函数，该函数以非负整数 num 作为输入，并打印所有小于 num 且能被 2 或 3 整除但不能被 8 整除的非负数。您应该使用文件中已有的函数（以及您为上一个实验开发的函数）
>
> 2. 在该函数之外，要求用户输入一个非负整数。然后，您的程序应通过调用函数 print_all_23n8 打印所有能被 2 或 3 整除但不能被 8 整除的非负数
>
> 3. 运行您的程序并通过在提示输入数字时输入（例如 1000）来测试它

```python
def is_divisible(n,m):
     '''
     (int, int)->bool
     returns True if n is divisible by n, and False otherwise.
     '''
     return n%m==0

def is_divisible23n8(n):
     '''(int)->bool
     returns string "yes" if n is divisible by 2 or 3 but not 8, and "no" otherwise.'''
     if ( (is_divisible(n,2) or is_divisible(n,3)) and not(is_divisible(n,8))):
          return True
     else:
          return False

def ex23n8():
     num = int(input("Please enter a non-negative number: "))
     for i in range(0,num):
          if is_divisible23n8(i):
               print(i, end=" ")
          else:
               pass
```

# Programming exercise 4

```python
for i in range(11):
    print(" "*(11-i),end="")
    print("#"*(2*i-1))
```

# Programming exercise 5

素数

```python
def prime_num():
    num = int(input("Please enter a number: "))
    for i in range(1,num+1):
        if (num/i)%1 == 0:
            print(i,end=" ")
        else:
            i+=1
    return
```
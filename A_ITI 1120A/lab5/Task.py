import math
# Task 4 and Programming Exercise 1
def ah(l,x,y):
    filt_num = [i for i in l if x <= i <= y] # 创建遍历集合l中的每个元素，并将它放到这个数组中
    count = len(filt_num) # 计算数组的长度
    min_num = min(filt_num) # 在数组中找最小数
    return(count, min_num)

# Task 5
def test1():
    count = 0
    for i in range(-2, 14):
        print("*")
        print("**")
        count += 1
    print(count) #16,then times 3 = 48
    return

# Task 6
def task2():
    fruits = ["apple","orange","banana","cherry"]
    for afruit in fruits:
        print(afruit, end = " ")

    for position in range(len(fruits)):
        print(fruits[position], end=" ")


    for name in ["Joe", "Amy", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]:
        print("Hi ", name, "Please come to my party on Saturday !")

# task 7
def task3():
    for i in range(5,0,-1):
        num = 1
        for j in range(1,i+1):
            print(num, end="| ")
            num = num*2
        print()

# Programming Exercise 2
def is_perfect(n):
    '''
    n->int
    '''
    sum_of_div = 1  # 1 是任何数的真因子
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            sum_of_div += i
            if i != n // i:  # 处理平方数的情况
                sum_of_div += n // i
    return sum_of_div == n

#  Programming Exercise 3a: Arithmetic progression
def arithmetic(l):
    '''l is a list of number'''
    if len(l) <= 2:
        return True

    diff = l[1] - l[0]

    for i in range(1,len(l) -1):
        if l[i + 1] - l[i] != diff:
            return False
    return True

# Programming Exercise 3b: and now … is it sorted?
def is_sorted(n):
    if len(n) <= 1:
        return True

    for i in range(len(n) - 1):
            if n[i] > n[i + 1]:
                return False

    return True

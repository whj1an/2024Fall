# PE2
def sum_of_nums():
    '''
    non->non
    '''
    flag = "yes"
    while flag == "yes":
        num1 = int(input("Please enter the first number: "))
        num2 = int(input("Please enter the second number: "))
        result = num1 + num2
        print(f"The final answer is {result}")
        flag = input("Do you want to continue?(yes/no): ").lower().replace(" ","")
    return

#PE3
def first_neg(l):
    '''
    list->int
    '''
    position = 0
    while position < len(l):
        if l[position] < 0:
            return position
        position += 1
    return None

#PE4
def sum_5_consecutive(l):
    '''list->bool
    '''
    if len(l) < 5:
        return False
    for i in range(len(l) - 4):
        if sum(l[i:i+5]) == 0:
            return True
    return False

#PE6
def fib(n):
    '''int -> list
    n>1
    '''
    l = [1,1]
    for i in range(2,n):
        l.append(l[i-1]+l[i-2])
    print(l)

#PE7
def inner_product(x,y):
    '''(list,list)->int
    two lists should be in the same length
    '''
    result = 0
    l = len(x)
    for i in range(0,l):
        result += x[i] * y[i]
    return result

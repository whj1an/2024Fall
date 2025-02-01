# Programming exercises: Q3b
def is_divisible(n,m):
    '''
    n -> floating number
    m -> floating number
    '''
    if (n % m == 0):
        return 1
    else:
        return 0


def is_divisible23n8():
    '''
    x -> int number
    '''
    x = float(input("Enter an interger: "))
    if ((is_divisible(x,2) == 1) or (is_divisible(x,3) == 1)) and is_divisible(x,8) == 0:
        print(f"{x} is divisible by 2 or 3 but not 8")
    else:
        print(f"It is not true that {x} is divisible by 2 or 3 but not 8")

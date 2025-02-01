# Task 2
def al():
    current_time = int(input("What is the current time (in hours 0-23)?"))
    wait_time = int(input("How many hours do you want to wait"))

    final_time = current_time + wait_time

    final_time_a = final_time % 24

    print ("The time afeter waiting is: ", final_time_a)

    return


# Programming exercises: Q1
def pay(s,t):
    '''
    s -> float number
    t -> float number
    '''
    if t < 40:
        salary = s * t
    elif 40 < t < 60:
        salary = (s * 40) + ((t-40) * 1.5 * s)
    elif t > 60:
        salary = (s * 40) + (1.5 * 20 * s) + ((t-60) * 2 * s)

    return salary

# Programming exercises: Q2
def rps(p1,p2):
    '''
    player1 -> str: 'R', 'P', or 'S'
    player2 -> str: 'R', 'P', or 'S'
    return: -1 if player 1 wins, 1 if player 2 wins, 0 if it's a tie
    '''
    if (p1 == "R" and p2 == "S") or (p1 == "S" and p2 == "P") or (p1 == "P" and p2 == "R"):
        return -1
    elif (p1 == p2):
        return 0
    else:
        return 1


# Programming exercises: Q3
def is_divisible():
    '''
    n -> floating number
    m -> floating number
    '''
    n = int(input("Enter 1st integer: "))
    m = int(input("Enter 2nd integer: "))
    if (n % m == 0):
        print(f"{n} is divisible by {m}")
    else:
        print(f"{n} is not divisible by {m}")



    

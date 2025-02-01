import math
import random


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
    for _ in range(int(n)):
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


def high_school_quiz(a,b,c):
    # Your code for high_school_quiz function goes here (instead of keyword pass)
    # Your code should include  dosctrings and the body of the function
    print(f"The quadratic equation {a}·x^2 + {b}·x + {c} = 0")
    delta = b ** 2 - 4*a*c
    if a == 0:
        if b == 0:
            if c == 0:
                print(f"The quadratic equation 0*x^2+0*x+0=0 is satisfied for all numbers x")
            else:
                print(f"The quadratic equation 0*x + {c} = 0 is satisfied for no numbers x")
        else:
            root = -c / b
            print(f"The quadratic equation {b}*x+c=0 has the following root/solution: {root}")
    return

    if delta > 0:
        root1 = (-b + math.sqrt(delta)) / (2 * a)
        root2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"The quadratic equation {a}x^2+{b}*x+{c}=0 has the following real roots: {root1}, \n {root2}")
    elif delta == 0:
        root = -b / (2 * a)
        print(f"The quadratic equation {a}x^2+{b}x+{c}=0 has only one solution, a real root: {root}")
    else:
        real_part = -b / (2 * a)
        ima_part = math.sqrt(-delta) / (2 * a)
        print(f"The quadratic equation {a}x^2+{b}x+{c}=0 has follwing two complex roots: \n {real_part} + i {ima_part} \n and \n {real_part} + i {ima_part}")
    pass



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

status=input("Hi "+name+". Are you in? Enter \n1 for elementary school\n2 for high school \n3 other character(s) for none of the above?\n")


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
                print(f"Congratulations {name}! You’ll probably get an A tomorrow. Good bye {name}!")
        elif n == 2:
            if elementary_school_quiz(ele_choice, n) == 2:
                print(f"Congratulations {name}! You’ll probably get an A tomorrow. Good bye {name}!")
            elif elementary_school_quiz(ele_choice, n) == 1:
                print(f"You did ok {name}, but I know you can do better. Goodbye {name}!")
            else:
                print(f"I think you need some more practice {name}. Good bye {name}!")
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

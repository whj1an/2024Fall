# File Nme: q0.py
```python
  
############# PART 1 ##############  
  
def info_day(today, weather, temperature):  
     print(today, "is a", weather, "day. The temperature is", temperature, "degrees Celsius.")  
  
     #Create a string s below such that print(s) command below  
     #prints the exact same message as the above print statement.     # Once you are done, uncomment the two lines of code below     #     s= f"{today} is a {weather} day. The temperature is {temperature} degress Celsius"     print(s)  
  
info_day("Saturday", "nice", 29)  
info_day("Monday", "so so", 15)  
  
############# PART 2 #############  
  
# Uncomment the 3-4 lines of code starting with def below.  
# Run the program. Why does it crash?  
# Can you fix it without chaning function call: letter_grade("B")  
  
def letter_grade(letter_grade):  
     print("Your grade is", letter_grade)  
     return  
letter_grade("B")  
  
############# PART 3 #############  
  
# Rewrite the following program so that it computes the average  
# in a function called average_of_two. # Obtaining the input from the user and printing of the result  
# must still be outside of the the function.  
#  
# Make sure to write DOCSTRINGS for your function, including TYPE CONTRACT.  
# Test it by running help(average_of_two) in python shell.  
def average_of_two():  
     '''  
     x -> float     y -> float     '''     x=float(input("Give me 1st number: "))  
     y=float(input("give me 2nd number: "))  
  
     average=(x+y)/2  
     print("The average of", x, "and", y,"is", average)  
     return
```

# File Nmae: a0_lab3.py
```python
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
    s -> float number    t -> float number    '''    if t < 40:  
        salary = s * t  
    elif 40 < t < 60:  
        salary = (s * 40) + ((t-40) * 1.5 * s)  
    elif t > 60:  
        salary = (s * 40) + (1.5 * 20 * s) + ((t-60) * 2 * s)  
  
    return salary  
  
# Programming exercises: Q2  
def rps(p1,p2):  
    '''  
    player1 -> str: 'R', 'P', or 'S'    player2 -> str: 'R', 'P', or 'S'    return: -1 if player 1 wins, 1 if player 2 wins, 0 if it's a tie    '''    if (p1 == "R" and p2 == "S") or (p1 == "S" and p2 == "P") or (p1 == "P" and p2 == "R"):  
        return -1  
    elif (p1 == p2):  
        return 0  
    else:  
        return 1  
  
  
# Programming exercises: Q3  
def is_divisible():  
    '''  
    n -> floating number    m -> floating number    '''    n = int(input("Enter 1st integer: "))  
    m = int(input("Enter 2nd integer: "))  
    if (n % m == 0):  
        print(f"{n} is divisible by {m}")  
    else:  
        print(f"{n} is not divisible by {m}")
```
# File Nmae: Lab3_a0_Question3_b
```python
# Programming exercises: Q3b  
def is_divisible(n,m):  
    '''  
    n -> floating number    m -> floating number    '''    if (n % m == 0):  
        return 1  
    else:  
        return 0  
  
  
def is_divisible23n8():  
    '''  
    x -> int number    '''    x = float(input("Enter an interger: "))  
    if ((is_divisible(x,2) == 1) or (is_divisible(x,3) == 1)) and is_divisible(x,8) == 0:  
        print(f"{x} is divisible by 2 or 3 but not 8")  
    else:  
        print(f"It is not true that {x} is divisible by 2 or 3 but not 8")
```
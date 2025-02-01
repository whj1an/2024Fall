def number_divisible(l,n):
    '''(list,int)->int
    if you just call this function please enter a list and then a intager,
    divided them by ","
    if just run it you will get some Text issues
    '''
    count = 0
                
    new_l = [] # set a empty list
    for element in l:
        element = int(element)
        new_l.append(element) #trans
    
    for i in new_l:
        if i % n == 0:
            count += 1 #counter self+
    return count

#main
user_l = input("Please input a list of numbers separated by space: " ).strip( ).split()
user_n = int(input("Please input an integer: ").strip())

result = number_divisible(user_l,user_n)

print(f"The number of elements divisible by {user_n} is {result}")

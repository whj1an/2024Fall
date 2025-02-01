def two_length_run(l):
    '''(list)->boolean
    you should enter a list of numbers and judge does it appear two same numbers continuely
    length at least 2
    '''
    new_l = [] # initialize
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

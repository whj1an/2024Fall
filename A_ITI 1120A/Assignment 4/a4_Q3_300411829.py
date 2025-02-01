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

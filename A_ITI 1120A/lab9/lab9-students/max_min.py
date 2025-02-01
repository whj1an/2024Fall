def min_or_max_index(l,b):
    '''(lst,bool)->tuple
    '''
    if b:
        target_value = l[0]
        target_index = 0
        # Find minimum
        for i in range(1, len(l)):
            if l[i] < target_value:
                target_value = l[i]
                target_index = i
    else:
        target_value = l[0]
        target_index = 0
        # Find maximum
        for i in range(1, len(l)):
            if l[i] > target_value:
                target_value = l[i]
                target_index = i

    return target_value, target_index

def mssl(l):
    '''(list)->int
    '''
    max_sum = 0
    for i in range(len(l)-1):
        current_sum = 0
        for j in range(i+1,len(l)):
            current_sum += l[j]
            max_sum = max(max_sum, current_sum)
    return max_sum

l = [1,-2,8,32,-17,-3,3,4,1]
mssl(l)
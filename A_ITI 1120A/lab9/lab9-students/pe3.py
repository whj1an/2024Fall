def first_one(L):
    '''(list) -> int'''
    if 1 not in L: return -1

    for i in range(len(L)):
        if L[i] == 1:
            return i

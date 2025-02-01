def move_zeros_v1(l):
    tmp = [x for x in l if x != 0]
    tmp.extend([0] * l.count(0))
    return tmp

def move_zeros_v2(l):
    c = 0
    for i in range(len(l)):
        if l[i] != 0:
            l[c] = l[i]
            c += 1
    for i in range(c,len(l)):
        l[i] = 0

def move_zeros_v3(l):
    counter = 0

    for i in range(len(l)):
        if l[i] != 0:
            l[i], l[counter] = l[counter], l[i]
            counter += 1

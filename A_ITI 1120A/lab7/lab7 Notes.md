```python
#5.16
def indexes(s1,s2):
    '''(string, string)->list
    '''
    l = []
    counter = -1
    for char in s1:
        counter += 1
        if char == s2:
            l.append(counter)
    return l

#5.17
def doubles(l):
    '''(list) -> None
    '''
    for i in range(len(l)-1):
        if l[i-1]*2 == l[i]:
            print(l[i])
    return

#5.18
def four_letter(l):
    '''(list) -> list
    '''
    new_l = []
    for i in range(len(l)):
        if len(l[i]) == 4:
            new_l.append(l[i])
    return new_l

#5.19
def inBoth(list1,list2):
    '''(list,list)->boolean
    '''
    for char1 in list1:
        for char2 in list2:
            if char1 == char2:
                return True
    return False

#5.20
def intersect(list1,list2):
    '''(list,list)->list
    '''
    for i in range(len(list1)):
        if list1.count(list1[i]) > 1:
            return False
    for j in range(len(list2)):
        if list2.count(list2[j]) > 1:
            return False

    new_l = []
    for char1 in list1:
        for char2 in list2:
            if char1 == char2:
                new_l.append(char2)
    return new_l

#5.21
def pair(list1,list2,n):
    '''(list1,list2,int)->None
    return two numbers which is element in both list are added is n
    '''
    for char1 in list1:
        for char2 in list2:
            if char1 + char2 == n:
                print(char1,char2)
    return

#5.22
def pairSum(l,n):
    '''(list,int)->None
    '''
    for i in range(len(l)):
        for j in range(i,len(l)):
            if l[i] + l[j] == n:
                print(i,j)
    return

#5.29
def lastfirst(l):
    '''(list)->list
    '''
    last_name = []
    first_name = []
    t = [last_name,first_name]
    for i in range(len(l)):
        new_l = l[i].split(',')
        last_name.append(new_l[1])
        first_name.append(new_l[0])
    return t

#5.31
def subsetSum(l,n):
    '''(list,iint)->boolean
    '''
    for i in range(len(l)-2):
        for j in range(i+1,len(l)-1):
            for k in range(j+1,len(l)):
                if l[i] + l[j] + l[k] == n:
                    return True
    return False

#5.33
def mystery(n):
    '''(int)->int
    '''
    counter = 0
    while not n == 1:
        n = n // 2
        counter += 1
    return counter

#5.46
def inversions(s):
    '''(str)->int
    '''
    counter = 0
    for i in range(0,len(s)-1):
        for j in range(i+1,len(s)):
            if s[i] > s[j]:
                counter += 1
    return counter

#5.48
def sublist(list1,list2):
    '''(list,list)->Boolean
    '''
    new_l = []
    for i in range(len(list1)):
        for j in range(i+1,len(list2)):
            if list1[i] == list2[j]:
                new_l.append(list1[i])
    if new_l == list1:
        return True
    else:
        return False

#5.37
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

```


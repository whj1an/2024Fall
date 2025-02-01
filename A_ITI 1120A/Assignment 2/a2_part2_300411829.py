# Haojian Wang
# ITI 1120 Vida
# A2
# Sept. 29 2024

# Part 2_1
def min_enclosing_rectangle(radius,x,y):
    '''
    radius,x,y -> float number
    radius should be >= 0, otherwise it will return None
    '''
    if radius >= 0:
        return (x - radius, y - radius)
    else:
        return None

def vote_percentage(results):
    '''
    results -> string
    only has 'yes', 'no', and 'abstained'. And only count the numbers of yes and no
    '''
    y = results.count('yes')
    n = results.count('no')
    return y/(y+n)

def vote():
    '''
    r are the strings
    If all the votes are yes, then the proposal passes "unanimously",
    if at least 2/3 of the votes are yes, then the proposal passes with "super majority",
    if at least 1/2 of the votes are yes, then the proposal passes by "simple majority",
    and otherwise it fails.
    '''
    r = str(input("Enter the yes, no, abstained votes one by one and then press enter:"))
    if vote_percentage(r) == 1:
        print ("proposal passes unanimously")
    elif 2/3 <= vote_percentage(r) < 1:
        print ("proposal passes with super majority")
    elif 1/2 <= vote_percentage(r) < 2/3:
        print ("proposal passes with simple majority")
    else:
        print ("proposal fails")

def l2lo(w):
    '''
    w -> float
    return l -> int, o -> float
    '''
    l = int(w // 1)
    o = (w - l) * 16
    return (l,o)

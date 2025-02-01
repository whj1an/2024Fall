# Haojian Wang
# 300411829
# ITI 1120
# 13 Oct. 2024

import math
# 2.1
def sum_odd_divisors(n):
    '''
    (numebr)->number
    if n is 0, returns None. Else return int
    '''
    if n == 0:
        return None #判断特例
    n = abs(n) #n变为正数
    sum = 0 #初始化
    for i in range(1,n+1,2):
        if n % i == 0:
            sum += i
    return sum

# 2.2
def series_sum():
    '''
    None->float
    please enter a positive number, otherwise it will return None
    '''
    n = int(input("Please enter a non-negative integer: "))
    if n < 0:
        return None # 用户非法输入，返回空值 Illegal input, return None
    ser_sum = 1000
    #进入循环 enter loop
    for i in range(1,n+1):
        ser_sum += 1 / (i**2)
    return ser_sum

# 2.3
def pell(n):
    '''
    int -> float
    '''
    n = int(n)
    if n < 0:
        return None
    elif n == 0:
        return 0
    elif n == 1:
        return 1

    p0 = 0
    p1 = 1
    for i in range(2,n+1):
        p_result = 2 * p1 + p0
        p0 = p1
        p1 = p_result
    return p1

# 2.4
def countMembers(s):
    '''
    (string)->number
    '''
    count = 0 #初始化
    for char in s:
        each_char = ord(char) #将每个字符串转换成ASCII码
        
        if 101 <= each_char <= 106: #检查小写e到j
            count += 1
        
        elif 70 <= each_char <= 88: #jiancha daxie F dao X /w
            count += 1
            
        elif 50 <= each_char <= 54: #jiancha 2 dao 6 /h
            count += 1
            
        elif char == "!" or char == "," or char == "\\": #jiancha qita /j
            count += 1
            
    return count

#2.5
def casual_number(s):
    '''
    (str) -> int
    '''
    if s[0] == '-': #处理负的 Negaive
        cleaned_s = s[1:].replace(",", "")  #处理逗号
        if cleaned_s.isdigit():  # 检查是否全是数字
            return -int(cleaned_s)
        else:
            return None  #如果非合法数字返回None
    else: #处理正的 Positive
        cleaned_s = s.replace(",", "")
        if cleaned_s.isdigit():
            return float(cleaned_s)
        else:
            return None


# 2.6
def alienNumbers(s):
    '''
    (str) -> number
    '''
    return sum({'T': 1024, 'y': 598, '!': 121, 'a': 42, 'N': 6, 'U': 1}[char] for char in s)

# 2.7
def alienNumbersAgain(s):
    '''
    (str) -> number
    '''
    total_value = 0  #初始化
    
    for char in s:
        if char == 'T':
            total_value += 1024
        elif char == 'y':
            total_value += 598
        elif char == '!':
            total_value += 121
        elif char == 'a':
            total_value += 42
        elif char == 'N':
            total_value += 6
        elif char == 'U':
            total_value += 1
    
    return total_value

# 2.8
def encrypt(s):
    '''
    (str)->str
    '''
    reversed_s = s[::-1]
    encrypted = ""  #初始化
    length = len(reversed_s)
    
    for i in range((length + 1) // 2):
        encrypted += reversed_s[i]  #从左边
        if i != length - i - 1:  #防止在字符串长度为奇数时重复添加中间字符
            encrypted += reversed_s[length - i - 1] #从右边
    
    return encrypted

# 2.9
def oPify(s):
    '''
    (str) -> str
    '''
    #如果字符串长度为1,则直接返回
    if len(s) < 2:
        return s
    
    result = "" #初始化空字符串
    
    for i in range(len(s)-1): #根据题意,最后一个不需要判断
        front = s[i]
        second = s[i + 1]
        
        result += front #先把第一个放进去
        
        if front.isalpha() and second.isalpha(): # panduan panduan
            if front.isupper(): # 插o/O
                result += 'O'
            else:
                result += 'o'
                
            if second.isupper():
                result += 'P'
            else:
                result += 'p'
                
    result += s[-1] #将最后一个字符串加进去
    return result

# 2.10
def nonrepetitive(s):
    l = len(s)

    for sub_l in range(1, l // 2 + 1):
        #比较相邻的子串
        for i in range(l - 2 * sub_l + 1): # 上面取整,这里x2+1可以找到中间那个
            #两个相邻的子串进行比较
            if s[i:i+sub_l] == s[i+sub_l:i+2*sub_l]:
                return False  # 如果相邻子串相同，返回 False
    
    return True  # 如果没有相邻子串相同，则返回 True



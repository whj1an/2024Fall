# Lectures

## 23 Sept.

Question 11
m how many times you can devid.  m by 2 before u get a number <= 1

```python
5.4//2
#2.7
5.5/2/2
#1.35
5.4/2/2/2
#0.675
```
Lets write more nicely:
$$
\begin{split}
	\frac{m}{2{\times}2{\times}2{\times}...} \\
	\\
	=> \frac{m}{2^k}
\end{split}
$$
```python
import(math)
#log_2 n
math.log(1000000000,2)
#29,897352853986263
```

### One-way if statement
```python
if <condition>
	<indented code block>
<non-indented statement>
```
Example
```python
if temp > 30:
	print("It is hot!")
	pring()
```

### Two-wat if statement
```python
if <condition>:
	<indented code block>
else:
	<indented code block>
<non-indented statement>
```

example:
```python
if a > 30:
	print("AAA")
else:
	print("BBB")
print("goodbey")
```

### Multi-way if statement
```python
def temperature(t):
	if t > 30:
		print('It is hot')
	else t > 0:
		print('I is cool')
	else:
		print('It is freezing')
	print('Goodbye')
```
#### Example 1
```python
# What does this print?
x = -10
if x < 10:
	print('I am negative number')
if x > 0:
	print('I am a postive number')
else:
	print('I am zero')

# continues
print('good bye')
```
output:
```python
I am negative number
I am zero
good bye
```

#### Example 2
```python
# What does this print?
x = 25
if x < 10:
	print('paris')
elif x < 30:
	print('ottawa')
elif x < 100:
	print('toronto')
else:
	print('uf')

print('good bye')
```
output
```python
ottawa
good bye
```
it meets the first part of  `elif`, and after comparing it's `Ture`, so it prints `ottawa` only, even if the second `elif` comes out is Ture as well, but it won't print anymore.
Attention: if you change the second `elif` to `else`, it will print `toronto` as well.


```python
def format_age(age):
'''
	(int) -> None
	(you have to tell the user what kind of velua they need to type.) -> (What kind of the velua you want to return.)
'''
	if age < 20:
		return str(age)
	elif age < 30:
		return "twenty somethin"
	elif age < 40:
		return "thirty something"
	else:
		return "ancient"
```

### `math.abs()`
In python, `math.abs()` function which we can rewrite it by `if else` statements:
```python
def abs(x):
	'''
	(number) -> (number)
	'''
	print("bl")

	if x < 0:
		return -x
	else:
		return x
----------------------------------
def abs(x):
	'''
	(number) -> (number)
	'''
	print("bl")

	if x < 0:
		return -x
	return x
-----------------------------------
def abs(x):
	'''
	(number) -> (number)
	'''
	print("bl")

	if x < 0:
		x = -x  # you can put this line to the line above to save the space.
	return x
```

## String Operators
![[Pasted image 20240923141527.png]]

Example
```python
s = "It is September"

"S" in s
#Ture
"s" in s
#Ture
```

###  `str.count`

```python
help(str.count)
'''
Help on method_descriptor:

count(...)
    S.count(sub[, start[, end]]) -> int
    
    Return the number of non-overlapping occurrences of substring sub in
    string S[start:end].  Optional arguments start and end are
    interpreted as in slice notation.
'''

help(abs)
'''
Help on built-in function abs in module builtins:

abs(x, /)
    Return the absolute value of the argument.
'''
```

 method is a special function.

### `str.(strip)`
自己打一下就可以了

There are so many useful function you can check by `dir(str)`

![[Recording 20240923142221.webm]]



# 2nd Oct.

```python
def messify(s):
	newS = ""
	for ch in s :
		if ch in "0123456789":
			if ch in "2357":
				newS = newS + "pr"
			else:
			newS = newS + ch * int(ch) *
	return newS
```
>given a string s, create a new string that is an encrypted version
imagine you pair consecutive disjoint characters,
reverse every pair,
for example `s = "abcdef"("ab","cd","ef") -> ("ba","dc","fe") `
after every pair, you need to insert * or @
`*` if the pair contains a vowel, and @ otherwise.
if the string has an odd number of characters the last character is added on as-is

```python
def flip_consecutive_disjoint_pairs():
	news = ""
	if len(s) < 2:
	    return s
	
	for i in range(0,len(s),2):
		pair1 = s[0]
		pair2 = s[1]
		reverse - pair2 + pair1
		# if pair1 or pair2 in vowels => if (pair1) or (pair2) 
		if pair1 in vowels or pair2 in vowels:
			news = news + "*"
		else:
			news = news + "@"
	
	if len(s) % 2 == 1:
		news = news + s[-1]

print(flip_consecutive_disjoint_pairs("abc"))
```


> Module random

[[教材-Introduction to Computing Using Python An Application Development Focus (Ljubomir Perkovic).pdf#page=216&selection=137,4,139,6|教材-Introduction to Computing Using Python An Application Development Focus (Ljubomir Perkovic), 页面 216]]

# 7 Oct.

List

```python
q1 = [2,10,0]
q2 = [2,10,0]
q1 == q2
#True
```

# 9 Oct.

```python
l=[2,10,4]
for item in i:
    print(item)
```

```python
answer = input("Enter yes or no").lower()

while answer != "yes" and answer !="no":
answer = input("Enter yes or no:")
```

```python
import random

def guessing.game():
    print("I'm thinking of a number in the set 1,2,3,...,1000")
    x=random.randint(1, 1000)
    
    guess = int(input("Try and guess a number between 1 and 1000"))
    
    tries = 3
    
    while tries > 0 and guess != x:
        if guess < x:
            print("too low")
        elif guess > x:
            print("too high")
        elif guess == x:
            print("you win!")
            
guessing_game()
```





# 21st Oct

Trying to find the maxmum number in the list. 
[[A_ITI 1120A/教材-Introduction to Computing Using Python An Application Development Focus (Ljubomir Perkovic).pdf#page=58&selection=22,0,23,0|教材, 页面 58]]

```python
def maxmum(l):
    '''
    (list)->number
    Precondition: l is non empty list of numbers
    
    Given the list of numbers l, the function returns the maximum fron the list
    '''
    current_max = l[0]
    for item in l:
        if item > current_max:
            current_max = item
            
    return current_max

# of operations <= 1 + n + n + n + 1 = 3n + 2 = n

# solution 2:
# of operations < 4n - 1000 = 0(n)
```

method of `list`

|            **Usage** | **Explanation**                      |
| -------------------: | ------------------------------------ |
|           `x in lst` | `x` is an item of `lst`              |
|       `x not in lst` | `x` is not an item of `lst`          |
|         `lst + lstB` | Concatenation of `lst` and `lstB`    |
| `lst * n`, `n * lst` | Concatenation of `n` copies of `lst` |
|             `lst[i]` | Item at index `i` of `lst`           |
|           `len(lst)` | Number of items in `lst`             |
|           `min(lst)` | Minimum item in `lst`                |
|           `max(lst)` | Maximum item in `lst`                |
|           `sum(lst)` | Sum of items in `lst`                |

```python
def amxmum(l):
	result = max(l)
	return restult
```

V1
```python
def duplicate():
	n = len(l) #1 *n
	#'card* l[i]
	for i in range(n):
		for j in range(n):
			if l[i]==l[j] and i != j:
				return True
	return False
```
V2
```python
def duplicate(l):
	n = len(l)
	for i in range(n):
		for j in range(n):
			if l[i]==l[j] and i != j:
				return True
	return False
```

V1-1

```python
def duplicate(l):
    n = len(l)
    
    for i in range(n):# 1 *n
        #l[0]: n
        #l[1]: n
        #...
        #l[n-1]:n
        ofr j in range(n): # 1*n^2
            if l[i]==l[j] and i != j:
                return True
    return False
# 1+ n + n^2 + 2*n^2 +` = 2 + n + 3n^2 = 0(n^2)
```

V2-1

```python
def duplicate(l):
    n = len(l)#1
    
    for i in range(n):
        #l[0]:n-1 -> first time to loop the No.0
        #l[1]:n-2
        #l[2]:n-3
        #...
        #       1
        #       0
        for j in range(i+1,n):# 1 *
            if l[i]==l[j]:
                return True
    return False

# n-1 + n-2 + n-3 + ... +3 +2 +1 <== (n+1)*n/2 = n^2+n = 0(n^2)
```

Can we do it faster???

```python
def duplicate(l):
    n = len(l) #1
    
    l.sort()
    for i in range(n): # 1*n
        if l.count(l[i])>=2: # n * n
            return True
    return False #<1
```

cwyg82g6z

# 23 Oct.

```python
import random

def duplicates_fixed(lst):
    '''list -> bool
    Returns True if the list contains at least elements
    '''
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i] == lst[j] and i != j:
                return True
    return False

# im trying to find if there are some same elements in the list
def duplicates_fixed(l):
    '''list -> bool
    Returns True if the list contains at least elements
    '''
    n = len(l) #1
    for i in range(n):# 1*n
        for j in range(n): #1 * n * n = n ** 2
            	for k in range(n) # 1 * n*n**2 = n ** 3
            		if l[i] == l[j] and l[i] == l[k] and i != j and i!= k and j != k: #5*n**3
                		return True # <=1
    return False

# 1+n + n^2 + 6*n^3 + 1 = 2 + n + n^2 + 6n^3 <=2n^3 + n^3 + n^3 + 6n^3 = 0(n^3)

def triplicates_v2(l):
    n = len(l)
    for item in l:
        if mycount(l,item) >= 3:
            return True
    return False

def mycount(l,x):
    counter = 0
    for item in l:
        if item == x:
            counter += 1
    return counter


```

# 4th Nov.

```python
import random
l = random.sample(range(1,100001),1000)

def linear_search(l, y):
    '''(list, object)->int'''
```

# 6th Nov.

operations unsorted list vs. sorted list vs. sets

| operations | unsorted list | sorted list | sets |
| :--------: | :-----------: | :---------: | :--: |
|   `add`    |     O(1)      |    O(n)     | O(1) |
|  `remove`  |     O(n)      |    O(n)     | O(1) |
|  `search`  |     O(n)      |  O(log n)   | O(1) |

```python
wordlist = open(\fileName)

def palindram(words):
    pal = []
    for word in words:
        if word == word[::-1]:
            pal.append(word)
    return pal

results = palindrom(wordlist)

```

# 11th Nov.

Class

```python
class class_name:
    def __init__(slef, xcoord, ycoord):
        #bod
```

```python
class Point:
    def __init__(self, xcoord, ycoord):
        self.x = xcoord
        self.y = ycoord
    
    def move(slef, dx, dy):
        self.x += dx
        slef.y += dy
```

test

```python
p = Point(2,3)
```


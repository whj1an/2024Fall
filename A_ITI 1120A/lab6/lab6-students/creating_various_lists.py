import random
n=int(input("Enter a positive even integer for the size of the list?" ))
a = [0] * n
print("List a:",a)

b = []
for i in range(n):
    random_num = random.randint(1,100)
    b.append(random_num)
print("List b:",b)

c = b
print("c is the alias of b")

half_n = n // 2
for i in range(half_n):
    b[i] = 0

print(b,"\b",c)

d=[]
for element in b:
    d.append(element)
print("d is a copy of b",b)

e = []
i = 1
while i < n:
    e.append(b[i])
    i+=1
print("e includes all the elements of b",e)

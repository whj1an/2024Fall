# test 1
def orange(n):
    if n > 0:
        print(n, end=" ")
        orange(n - 2)


orange(10)


# test 2
def mulberry(n):
    if n == 1:
        return 1
    else:
        return n + mulberry(n - 1)


print(mulberry(4))


# task 3
def cantaloupe(n):
    if n > 0:
        print(n % 10)
        cantaloupe(n // 10)


cantaloupe(7254)


# tesk 4
def almond(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        tmp = almond(lst[0:len(lst) - 1])
        if tmp > lst[len(lst) - 1]:
            return tmp
        else:
            return lst[len(lst) - 1]


a = [2, 7, -11]
print("test4: ", almond(a))


# tesk 5
def fig(lst, high):
    if high == 0:
        return lst[0]
    else:
        tmp = fig(lst, high - 1)
        if tmp > lst[high]:
            return tmp
        else:
            return lst[high]


a = [2, 7, -11]
print("test5: ", fig(a, len(a) - 1))


# tesk 6
def nox(s, ch):
    if len(s) == 0:
        return s
    elif s[0] == ch:
        return nox(s[1:], ch)
    else:
        return s[0] + nox(s[1:], ch)


print("test6: ", nox('Cacic', 'c'))


# PE 1
def m(i):
    if i == 1:
        return 1 / 3
    else:
        return i / (2 * i + 1) + m(i - 1)


for i in range(1, 11):
    print(m(i))


# PE 2
def count_digits(n):
    if n == 0:
        return 1
    elif n < 10:
        return 1
    else:
        return 1 + count_digits(n // 10)


print(count_digits(10))
print(count_digits(100))


# PE 3
def is_palindrome(n):
    """(str)->bool"""
    if len(n) <= 1:
        return True

    if n[0] == n[-1]:
        return is_palindrome(n[1:-1])
    else:
        return False


print(is_palindrome('blurb'))
print(is_palindrome('anna'))


# PE 4
def is_palindrome_v2(n):
    new_n = ''
    for i in range(len(n)):
        if n[i].isalpha():
            new_n += n[i]

    new_n = new_n.lower()
    return is_palindrome(new_n)


print(is_palindrome_v2("A man, a plan, a canal -- Panama!"))
print(is_palindrome_v2("Madam, I'm"))


# PE 5
def gcd(a, b):
    """a>b->int"""
    if b == 0:
        return a
    return gcd(b, a % b)


print(gcd(36, 20))  # Output: 4
print(gcd(12, 8))   # Output: 4
print(gcd(100, 25))  # Output: 25
print(gcd(7, 5))

# # 57616e6748616f6a69616e
# # ITI 1100
# # Lab 2
# # 18 Sept. 2024
#
# import math
#
# # Programming Exercises 1
# def repeater(s1, s2, n):
#     return((s1+s2)*n)
#
# # Programming Exercises 2
# def root(a, b, c):
#     print(f"The quadratic equation with coefficients a = {a}, b = {b}, c = {c}")
#     t = b**2-(4*a*c)
#     if (t>=0):
#         root1 = math.sqrt(t)/(2*a) - b
#         root2 = -math.sqrt(t)/(2*a) - b
#         print(f"has the following solutions (i.e. roots): \n {root1} and {root2}")
#     else:
#         print("This function doesn't have roots.")
#     return
#
# # Programming Exercises 3
# def real_roots(a,b,c):
#     t = b**2-(4*a*c) >= 0
#     return t
#
# # Programming Exercises 4
# def reverse(x):
#     a = x%10
#     b = x//10
#     return (10*a+b)
def ascii_name_plaque(name):
    edge=(len(("__" + name + "__")))
    print("*" * (edge+2))
    print("*" + "  "*(edge) + "*")
    print("*" + "__" + name + "__" + "*")
    print("*" + "  "*(edge) + "*")
    print("*" * (edge+2))
    return

ascii_name_plaque("Wanghaojian")
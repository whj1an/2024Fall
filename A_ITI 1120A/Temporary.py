# # # Yuting Yuan
# # # 300374547
# # # ITI 1120
# # # AssignmentNumber 3
# # # 2024
# #
# # def split_tester(N, d):
# #     '''
# #     (str, int) -> numbers, boolen
# #     '''
# #     # Your code for split_tester function goes here (instead of keyword pass)
# #     # Your code should include  dosctrings and the body of the function
# #     a = str(N)
# #     b = int(d)
# #
# #     if len(a) % b != 0:
# #         return False
# #
# #     for i in range(0, len(a), b):
# #         current_N = [i:i+b]
# #
# #         print(','.join(current_N))
# #
# #         for i in range(1, len(current_N)):
# #             if current_N[i] < current_N[i - 1]:  # 判断前一个和后一个的大小关系
# #                 return False
# #
# #         return True
# #
# #     # you can add more function definitions here if you like
# #
# #     # main
# #     # Your code for the welcome message goes here, instead of name="Vida"
# #     def ascii_name_plaque(name):
# #         nameOfLen = len(name)
# #         print("*" * (nameOfLen + 10))
# #         print("*" + " " * (nameOfLen + 8) + "*")
# #         print(f"*  __{name}__  *")
# #         print("*" + " " * (nameOfLen + 8) + "*")
# #         print("*" * (nameOfLen + 10))
# #
# #     ascii_name_plaque("Welcome to my increasing-splits tester")
# #     name = input("What is your name?").strip()
# #     ascii_name_plaque(f"{name},welcome to my increasing-splits tester.")
# #
# #     flag = True
# #     while flag:
# #         question = input(name + ", would you like to test if a number admits an increasing-split of give size? ")
# #         question = (question.strip()).lower()
# #         if question == 'no':
# #             flag = False
# #         # YOUR CODE GOES HERE. The next line should be elif or else.
# #         else:
# #             if question != "yes":
# #                 print("Please enter yes or no. Try again.")
# #             else:
# #                 print("Good choice!")
# #                 N = input("Enter a positive integer:").strip()
# #                 if N[0] == '-':
# #                     if N[1:].isdigit():  # 负数时判断是否为整数
# #                         print("The input has to be a positive integer.Try again.")
# #                     else:
# #                         print("The input can only contain digits. Try again.")
# #                 elif not N.isdigit():  # 判断是否为整数
# #                     print("The input can only contain digits. Try again.")
# #                 elif N == '0':
# #                     print("The input has to be a positive integer.Try again.")
# #
# #                 else:
# #                     d = input(f"Input the split. The split has to divide the length of {N} i.e. " + str(
# #                         len(N)) + '\n').strip()
# #                     if d[0] == '-':
# #                         if d[1:].isdigit():
# #                             print("The split has to be a positive integer.Try again.")
# #                         else:
# #                             print("The split can only contain digits. Try again.")
# #                     elif not d.isdigit():
# #                         print("The split can only contain digits. Try again.")
# #                     elif d == '0':
# #                         print("The split has to be a positive integer.Try again.")
# #                     else:
# #                         if len(N) % int(d) == 0:  # 可以被整除
# #                             if split_tester(N, d):
# #                                 print("The sequence is increasing")
# #                             else:
# #                                 print("The sequence is not increasing")
# #                         else:
# #                             print(f"{d} does not divide {len(N)}. Try again.")  # 不能被整除
# #
# #     # finally your code goes here too.
# #
#
# def duplicate(l):
#     n = len(l)  #1
#
#     l.sort() # 0(n^2)
#
#     for i in range(n):  # 1 * n
#         if l[i] == l[i + 1]: # 1 * n
#             return True # <= 1
#     return False # < 1

# int-list & int n
# def number_divisors(list, n):
#     result = 0
#     for element in list:
#         if element % n == 0:
#             result = result + 1
#     return result
#

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        initial_set = set()
        max_len = 0
        left_point = 0

        for i in range(len(s)):
            while s[i] in initial_set:
                initial_set.remove(s[left_point])
                left_point += 1
            initial_set.add(s[i])
            max_len = max(max_len, i - left_point + 1)
        return max_len
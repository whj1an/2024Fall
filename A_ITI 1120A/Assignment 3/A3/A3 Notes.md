# Part 1: Increasing-splits tester

----

`Copyright Haojian Wang all receives` 

免责声明：此笔记仅针对2024 Fall, ITI 1120 - A00, Assignment 3 参考与讨论，如果其他利用导致其他后果概不负责。如果对笔记有任何疑问或纠错，请随时联系

----

(40 points) (中文翻译随后)
To clarify Part 1 speciﬁcations, I have provided sample tests in Section 3. The behaviour implied by the sample tests
should be considered as required speciﬁcations in addition to what is explained below.

Description: Some positive integers N can be split into smaller pieces, such that the pieces are comprised of consecutive
digits of N and such that each piece contains the same number of digits. Given an integer N and given a number of digits
d, one can then ask if N can be split into pieces such that each pieces has d digits and such that the resulting sequence
of numbers is strictly increasing.
Examples:

- For N = 154152 and d = 2, the answer is yes, since d = 2 implies the following sequence 15, 41, 52 which is increasing.
- For N = 154152 and d = 3, the answer is no, since d = 2 implies the following sequence 154, 152 which is not increasing.
- For N = 154152 and d = 5, the answer is no, since 154152 cannot be split into ﬁve-digit pieces.
- For N = 137 and d = 1, the answer is yes, since since d = 1 implies the following sequence 1, 3, 7 which is increasing.
- For N = 137 and d = 2, the answer is no, since 137 cannot be split into two-digit pieces.
- For N = 113 and d = 1, the answer is no, since since d = 1 implies the following sequence 1, 1, 3 which is not increasing.
- For N = 113 and d = 3, the answer is yes, since d = 3 implies the following sequence 113 which is increasing.

Design, implement and test a Python program which checks to see if a user-supplied positive integer N and a user-
speciﬁed split d, are such that N can be split into pieces with d digits such that the resulting sequence is strictly increasing.
Here are the steps that your program should have: (Note that since no collection other than strings is allowed you will be
working with N and d as strings)

0. The program greets the user.
1. The program asks the user if they want to test if a number admits an increasing-split of give size.
2. The program prompts the user to enter a positive integer. If the user enters an invalid input (anything other than a positive integer), the program will repeat the questions starting with step 1.

2


3. The program prompts the user to enter the number of digits in each piece. The program will verify that the input is valid (a positive integer which is a proper divisor of the number of digits in the ﬁrst input); If the input is invalid, the program will repeat the questions starting with step 1.
4. Once the valid input is obtained, the program splits the number into pieces of speciﬁed length and displays/prints hose pieces in one line (separated by commas).
5. Finally, the program reports whether or not the obtained sequence of numbers is in strictly increasing order. If there is only one piece, it is deﬁned to be in strictly increasing order.
For this part, I provided you with starter code in ﬁle called part1_xxxxxx.py. Begin by replacing xxxxxx in the ﬁle name with your student number. Then open the ﬁle. Your solution (code) for this part must go into that ﬁle in the clearly indicated spaces only. You are not allowed to delete or comment-out or change any parts of the provided code except for the keyword pass.
For this part you need to submit two ﬁles: a3_part1_xxxxxx.py and a3_part1_xxxxxx.txt
a3_part1_xxxxxx.py needs to contain your program for Part 1 as explained above and a3_part1_xxxxxx.txt needs
to contain the proof that you tested your two core function from this part, namely split_tester.

> 为了阐明第 1 部分的规范，我在第 3 节中提供了示例测试。除了下文所述内容之外，示例测试所暗示的行为应被视为必需规范。
>
> 描述：一些正整数 N 可以拆分成更小的部分，使得这些部分由 N 的连续数字组成，并且每个部分包含相同数量的数字。给定一个整数 N 和给定的数字 d，然后可以询问是否可以将 N 拆分成几部分，使得每部分都有 d 位数字，并且得到的数字序列严格递增。
> 示例：
>
> 对于 N = 154152 和 d = 2，答案是肯定的，因为 d = 2 意味着以下序列 15、41、52 是递增的。
> 对于 N = 154152 和 d = 3，答案是否定的，因为 d = 2 意味着以下序列 154、152 不是递增的。
> 对于 N = 154152 和 d = 5，答案是否定的，因为 154152 不能拆分成五位数。
> 对于 N = 137 和 d = 1，答案是肯定的，因为 d = 1 意味着以下序列 1、3、7 是递增的。
> 对于 N = 137 和 d = 2，答案是否定的，因为 137 不能拆分成两位数。
> 对于 N = 113 和 d = 1，答案是否定的，因为 d = 1 意味着以下序列 1、1、3 不是递增的。
> 对于 N = 113 和 d = 3，答案是肯定的，因为 d = 3 意味着以下序列 113 是递增的。
>
> 设计、实现和测试一个 Python 程序，检查用户提供的正整数 N 和用户指定的分割 d 是否可以将 N 分割成具有 d 位数字的部分，使得生成的序列严格递增。
>
> 以下是您的程序应具有的步骤：（请注意，由于不允许使用除字符串之外的其他集合，因此您将使用 N 和 d 作为字符串）
>
> 0. 程序向用户打招呼。
>
> 1. 程序询问用户是否要测试数字是否允许给定大小的递增分割。
>
> 2. 程序提示用户输入正整数。如果用户输入无效输入（除正整数之外的任何内容），程序将从步骤 1 开始重复问题。
>
> 3. 程序提示用户输入每个部分的数字。程序将验证输入 
>    是否有效（一个正整数，是第一个输入的数字的真除数）；如果输入无效，程序将从步骤 1 开始重复问题。
> 4. 一旦获得有效输入，程序将数字拆分为指定长度的片段，并在一行中显示/打印这些片段（以逗号分隔）。
> 5. 最后，程序报告获得的数字序列是否严格递增。如果 
>     只有一段，则定义为严格递增。
>     对于这一部分，我在名为 part1_xxxxxx.py 的文件中为您提供了起始代码。首先将文件 
>     名称中的 xxxxxx 替换为您的学生编号。然后打开文件。您对此部分的解决方案（代码）必须仅放在该文件中明确指示的空间中。除了关键字 pass 之外，您不得删除、注释或更改所提供代码的任何部分。
>     对于此部分，您需要提交两个文件：a3_part1_xxxxxx.py 和a3_part1_xxxxxx.txt
>     a3_part1_xxxxxx.py 需要包含您第 1 部分的程序（如上所述），而 a3_part1_xxxxxx.txt 需要包含您测试此部分的两个核心函数（即 split_tester）的证据。

```python
def split_tester(N,d):
    def split_tester(N, d):
    '''
    (str, int) -> boolen
    '''
    # Your code for split_tester function goes here (instead of keyword pass)
    # Your code should include  dosctrings and the body of the function
    str_n = str(N)

    if len(str_n) % d != 0:
        return False

    current_N = [int(str_n[i:i+d]) for i in range (0, len(str_n), d), end=',']

    for i in range (1, len(current_N)):
        if current_N[i] <= current_N[i-1]:
            return False

    return True
```



## Part 1.1 The Core Function

Your solution in a3_part1_xxxxxx.py must have a function called: `split_tester`. You should design and test function `split_tester` before moving onto designing and coding the main part of the program. Here are speciﬁcations for that
function:

- `split_tester` This function has two parameters, a string N and a string d. These two strings can be assume to be such that each looks like a positive integer and such that the number of digits in N is divisible by the integer represented by d. Since N and d are assumed to be valid i.e. meet the preconditions, they deﬁne a sequence of numbers (as speciﬁed in the examples above). The function should print that sequence of numbers in such a way that the consecutive numbers are separated by commas as shown in the test cases. Note that there cannot be a comma after the last number in the sequence. The function should then return True if the sequences is strictly increasing and False otherwise. (Reporting, i.e. printing, whether or not the obtained sequence of numbers is strictly increasing has to be done in the main and not in the body of the split_tester function). Here are two approaches that may help you design this function:
  
  - You may ﬁnd it easier to process the number N, which is given as a string, when you split it into pieces.
    One approach:
  
    ```markdown
    start with an empty string to hold the substring, i.e. the split
    as you loop through the whole number one digit at a time
    append digits to the substring
    if the substring reaches the desired length
    do something with the substring
    reset the substring to empty to collect the next substring
    reset the substring length count to zero
    ```

  - Another approach:
  
     ```markdown
     figure out how many substrings you want
     loop that number of times
     use slices to create the substrings
     ```
  
  - Other suggestions:

    - You can use the `isdigit()` string method to determine if a string contains only digits. Type help(str.isdigit) in the Python shell for more information.
    - You can use the `len()` function to determine the length of a string i.e. the number of digits in N.
    - If you ﬁnd getting the commas right in the output tricky (because only commas between numbers are allowed), leave that until everything else is working correctly.
  
> a3_part1_xxxxxx.py 中的解决方案必须有一个名为`split_tester`的函数。在继续设计和编写程序的主要部分之前，您应该设计和测试 `split_tester` 函数。以下是该函数的规范：`split_tester` 此函数有两个参数，一个字符串 N 和一个字符串 d。这两个字符串可以假设为 每一个都看起来像一个正整数，并且 N 中的位数可以被 d 表示的整数整除。由于 N 和 d 被认为是有效的，即满足先决条件，因此它们定义了一个数字序列（如上例中所述）。该函数应以这样的方式打印该数字序列，即连续的数字用逗号分隔，如测试用例中所示。请注意，序列中最后一个数字后面不能有逗号。如果序列严格递增，则函数应返回 True，否则返回 False。 （报告，即 打印，无论获得的数字序列是否严格增加，都必须在主函数中完成，而不是在 `split_tester` 函数体中完成）。以下两种方法可能有助于您设计此函数：
>
> - 当您将数字 N 拆分成几部分时，您可能会发现处理以字符串形式给出的数字 N 更容易。
>   一种方法：
>
> ```markdown
> 以一个空字符串开始，用于保存子字符串，即分割 
> 当您循环遍历整个数字时，每次一位数字 
> 将数字附加到子字符串 
> 如果子字符串达到所需长度 
> 对子字符串执行某些操作 
> 将子字符串重置为空以收集下一个子字符串 
> 将子字符串长度计数重置为零
> ```
>
> - 另一种方法：
>
> ```markdown
> 计算出您想要多少个子字符串 
> 循环该次数 
> 使用切片创建子字符串 
> ```
>
> - 其他建议：
>
> 您可以使用 `isdigit()` 字符串方法来确定字符串是否仅包含数字。在 Python shell 中键入 help(str.isdigit) 
> 以获取更多信息。
> 您可以使用 `len()` 函数来确定字符串的长度，即 N 中的数字位数。
> 如果您发现在输出中正确使用逗号很棘手（因为数字之间只允许使用逗号），
> 请保留此操作，直到其他一切都正常工作。

### 测试需求 Testing Requirements：

```
Here is how you should test your two functions from Part 1 in Python shell.
>>> split_tester("12311234","2")
12, 31, 12, 34
False
>>> split_tester("12311234","4")
1231, 1234
True
>>> split_tester("0012311234","2")
00, 12, 31, 12, 34
False
>>> split_tester("0012311234","5")
00123, 11234
True
>>> split_tester("1","1")
1
True
>>> split_tester("1","1")
1
8
True
>>> split_tester("734","1")
7, 3, 4
False
>>> split_tester("734","3")
734
True

Here is what pressing Run on your program (Part 1) and should give:
************************************************
* 											   *
*  __Welcome to my increasing-splits tester__  *
* 											   *
************************************************

What is your name? Doctor Avrana Kern

*********************************************************************
* 																	*
* __Doctor Avrana Kern, welcome to my increasing-splits tester.__ 	*
* 																	*
*********************************************************************

Doctor Avrana Kern, would you like to test if a number admits an increasing-split of give size? sure
Please enter yes or no. Try again.
Doctor Avrana Kern, would you like to test if a number admits an increasing-split of give size? sure
Please enter yes or no. Try again.
Doctor Avrana Kern, would you like to test if a number admits an increasing-split of give size? yEs
Good choice!
Enter a positive integer: 123156
Input the split. The split has to divide the length of 123156 i.e. 6
4
4 does not divide 6. Try again.
Doctor Avrana Kern, would you like to test if a number admits an increasing-split of give size? YES
Good choice!
Enter a positive integer: 123156
Input the split. The split has to divide the length of 123156 i.e. 6
3
123, 156
The sequence is increasing
Doctor Avrana Kern, would you like to test if a number admits an increasing-split of give size? yes
Good choice!
Enter a positive integer: 3.4
The input can only contain digits. Try again.
Doctor Avrana Kern, would you like to test if a number admits an increasing-split of give size? yes
Good choice!
Enter a positive integer: -44
The input has to be a positive integer.Try again.
Doctor Avrana Kern, would you like to test if a number admits an increasing-split of give size? yes
Good choice!
Enter a positive integer: 3331
Input the split. The split has to divide the length of 3331 i.e. 4
2
33, 31
The sequence is not increasing
Doctor Avrana Kern, would you like to test if a number admits an increasing-split of give size? yes
Good choice!
Enter a positive integer: twenty
The input can only contain digits. Try again.
Doctor Avrana Kern, would you like to test if a number admits an increasing-split of give size? yeS
Good choice!
Enter a positive integer: 4321
Input the split. The split has to divide the length of 4321 i.e. 4
```

### 思路1 Method 1

1. 首先复制使用A1 中的`ascii_name_plaque()`函数
   ```python
   def ascii_name_plaque(n):
       '''
       name -> string
       it should be covered by "
       '''
       length=(len(n) + 6)
       print("*" * length)
       print("*" + " "*(length - 2) + "*")
       print(f"* _{n}_ *")
       print("*" + " "*(length - 2) + "*")
       print("*" * length)
       return
   ```

2. 现在，我们将这个函数拆解成3个部分：

   1. `custom_num()`部分
   2. `split()`部分
   3. `split_tester()`部分（主函数体）

#### `custom_num()`部分

这一部分主要用于判断用户输入的需要拆解数字，判断是否为digit并且式正整数，否则返回非法输入并返回主函数

```python
def custom_num(n):
    n = int(n)
    if not n.isdigit() or n <= 0:
            print("The input has to be a positive integer.Try again.")
            split_tester()
            return n
```



#### `split()`部分



#### `split_tester()`部分（主函数体）





























### 思路2 Method 2

1. 由测试中的Line1-14可以直到我们需要用到A1中的`ascii_name_plaque()`函数

```python
def ascii_name_plaque(n):
    '''
    name -> string
    it should be covered by "
    '''
    length=(len(n) + 6)
    print("*" * length)
    print("*" + " "*(length - 2) + "*")
    print(f"* _{n}_ *")
    print("*" + " "*(length - 2) + "*")
    print("*" * length)
    return
```

2. 用name接受用户输入的姓名，询问用户是否接受，注意用户只能输入yes或者no，如果输入了其他就`print("Please enter yes or no. Try again")`并重新接收，这里无论用户输入什么类型的yes或者no，都需要将输入的变量转换成yes或者no来识别，比如:`Y   es`,`Ye  s`,`        no`这些都需要被识别出来，可以用到`.replace(" ","")`和`.lower()`两个函数来去除空格并将字符串全部小写来识别。

```python
judge_yorn = input(f"{name}, would you like to test if a number admits an increasing-split of give size").replace(" ","").lower() #判断yes或者no
```

3. 将上述两个模块整合，随后判断用户输入的yes、no或者其他内容进行if判断。将大模块(Line 17 ~ 23)设置好。

```python
def ascii_name_plaque(n):
    '''
    name -> string
    it should be covered by "
    '''
    length=(len(n) + 6)
    print("*" * length)
    print("*" + " "*(length - 2) + "*")
    print(f"* _{n}_ *")
    print("*" + " "*(length - 2) + "*")
    print("*" * length)
    return
def split_tester():
    name = input("What is your name? ")
    ascii_name_plaque(name)
    judge_yorn = input(f"{name}, would you like to test if a number admits an increasing-split of give size").replace(" ","").lower() #判断yes或者no
    
    # main / if type yes
    if judge_yorn == "yes":
        # function
        elif judge_yorn == "no":
            ascii_name_plaque(f"Good bye Doctor {name}")  # 结束
        else:
            print("Please enter yes or no. Try again.") #用户非法输入，重新调用函数->返回函数入口
            split_tester()
```

4. 在（3）中的代码Line 18 `#function`处设计符合题意的代码。
   根据测试需求中的22行处代码，我们需要要求用户先输入一个`int`数字`custom_num`，随后在要求输入1，2，3，4，5，6中的任意一个并赋值给`split`，要求按照split来将`custon_num`切割。注意：按照测试需求中的需要将用户输入的数字全部转变成没有空格的类型识别并进行判断。
   根据测试需求23行发现：`Input the split. The split has to divide the length of 123156 i.e. 6`，i.e.后面跟的是一个随机数字。random

   ```python
   # replace function in the code block above
   #方式1：整合嵌入式代码
   rand_num = random.randrange(1,7)
   custom_num = int(input("Enter a positive integer: ").replace(" ",""))
   split = int(input(f"Input the split. The split has to divide the length of 123156 i.e. {rand_num}").replace(" ",""))
   ```
   
5. 接下来就是判断用户输入的`custom_num` 和 `split`是否合法，如果不合法则从新调用此函数并返回函数入口
   ```python
   # main / if type yes
       if judge_yorn == "yes":
   
           # custom_num part 用于判断用户输入的是否为整数或者非负
           custom_num = int(input("Good choice! \nEnter a positive integer: ").replace(" ",""))
   
           if not custom_num.isdigit() or int(custom_num) <= 0:
               print("The input has to be a positive integer.Try again.")
               split_tester() #用户非法输入，调用函数返回函数入口
               return
   
           # split part 用于判断用户输入的split是否为0~9
           split = int(input(f"Input the split. The split has to divide the length of {custom_num} i.e. {rand_num}: ").replace(" ",""))
           if split.isdigit() and (int(split) in range(0, 10)): #这里用`.isdigit()`函数和`in`函数判断
               print(f"Valid split: {split}")
           else:
               print("Invalid split value. Try again.")
               split_tester() #用户非法输入，调用函数返回函数入口
   ```

   *注：`.isdigit()`用于判断是否为数字*

   

### 思路3 Method 3

```python
import random

def ascii_name_plaque(n):
    '''
    Displays the name in a decorative ASCII art plaque.
    '''
    length = (len(n) + 6)
    print("*" * length)
    print("*" + " " * (length - 2) + "*")
    print(f"* _{n}_ *")
    print("*" + " " * (length - 2) + "*")
    print("*" * length)

def is_increasing_sequence(lst):
    '''
    Check if the list of numbers is strictly increasing.
    '''
    for i in range(1, len(lst)):
        if lst[i] <= lst[i-1]:
            return False
    return True

def split_number_into_pieces(num_str, split_size):
    '''
    Splits the number string into equal pieces of length split_size.
    '''
    return [int(num_str[i:i + split_size]) for i in range(0, len(num_str), split_size)]

def split_tester():
    name = input("What is your name? ")
    ascii_name_plaque(name)
    
    while True:
        # Asking user if they want to test the number split
        judge_yorn = input(f"{name}, would you like to test if a number admits an increasing-split of given size? (yes/no): ").replace(" ","").lower()
        
        if judge_yorn == "yes":
            # Asking for a positive integer
            custom_num = input("Good choice! \nEnter a positive integer: ").replace(" ", "")
            
            # Check if input is a valid positive integer
            if not custom_num.isdigit() or int(custom_num) <= 0:
                print("The input has to be a positive integer. Try again.")
                continue  # Ask the question again from step 1
            
            # Asking for the split size
            num_len = len(custom_num)  # length of the input number
            split = input(f"Input the split. The split has to divide the length of {custom_num}, i.e., {num_len}: ").replace(" ", "")
            
            # Validate if split is a digit and a valid divisor of the length of the number
            if not split.isdigit() or int(split) <= 0 or num_len % int(split) != 0:
                print(f"{split} does not divide {num_len}. Try again.")
                continue  # Ask the question again from step 1
            
            # Perform the split
            split_size = int(split)
            pieces = split_number_into_pieces(custom_num, split_size)
            
            # Display the split pieces
            print(f"The sequence: {', '.join(map(str, pieces))}")
            
            # Check if the sequence is strictly increasing
            if is_increasing_sequence(pieces):
                print("The sequence is increasing.")
            else:
                print("The sequence is not increasing.")
            
        elif judge_yorn == "no":
            ascii_name_plaque(f"Goodbye Doctor {name}")
            break  # Exit the loop

        else:
            print("Please enter yes or no. Try again.")

# Run the split tester
split_tester()

```





### File Name: a3_part1_xxxxxx.py



```python
# first: say hello to user
import 
def ascii_name_plaque(n):
    '''
    name -> string
    it should be covered by "
    '''
    length=(len(n) + 6)
    print("*" * length)
    print("*" + " "*(length - 2) + "*")
    print(f"* _{n}_ *")
    print("*" + " "*(length - 2) + "*")
    print("*" * length)
    return

def main_function():
    ascii_name_plaque("Welcome to my increasing-splits tester")
    name = input("What is your name? ")
    ascii_name_plaque(name)
    judge_yorn = input(f"{name}, would you like to test if a number admits an increasing-split of give size")
```

---

# Part 2: A Library of Functions

---

注意：本部分包含`a3_part2_xxxxxxxxx.py`文件和`a3_part2_xxxxxxxxx.txt`文件：前者为代码文件，后者为测试文件

---

## 2.1 `sum_odd_divisors(n)`

Write a function called `sum_odd_divisors` that takes a integer n as input. If n is zero, `sum_odd_divisors` returns None. Else, sum_odd_divisors returns the sum of all the postive odd divisors of n.

> 编写一个名为“sum_odd_divisors”的函数，以整数 n 作为输入。如果 n 为零，则“sum_odd_divisors”返回 None。否则，sum_odd_divisors 返回 n 的所有正奇数除数之和。

测试结果：

<img src="A3 Notes.attachments/image-20241010154304116.png" alt="image-20241010154304116" style="zoom:75%;" />

*注意：需要`import math`*

### **方法一/Method 1**

```python
def sum_odd_divisors(n):
    '''
    (numebr)->number
    if n is 0, returns None. Else return int
    '''
    if n == 0:
        return None #首先判断特例：0的时候直接返回None（题目中表述了）
    n = math.abs(n) #根据测试需求，将n变为正数
    sum = 0 #先设置一个sum来存放奇数和
    for i in range(1,n+1,2):
        if n % i == 0:
            sum += i
    return sum
```

### **方法二/Method 2**

```python
def sum_odd_divisors(n):
    '''
    (numebr)->number
    if n is 0, returns None. Else return int
    '''
    if n == 0:
        return None
    n = math.abs(n)
    div_sum = sum(i for i in range(1,n+1,2) if n % i == 0) #求和（i对于所有i在范围（1~n+1，间隔为2）之中，如果n对i取余等于0）
    return div_sum
```

---

## 2.2 `series_sum()`

Write a function called series_sum() that prompts the user for an non-negative integer n. If the user enters a negative integer the function should return None otherwise the function should return the sum of the following series:
$$
1000 + \frac{1}{1^{2}} + \frac{1}{2^{2}} +\frac{1}{3^{2}} + \frac{1}{4^{2}} + ...+\frac{1}{n^{2}}
$$
for the given integer n. For example, for n = 0, the function should return 1000, for n = 1, the function should return 1001, for n 2, the function should return 1001.25, for n = 3, the function should return 1001.3611111111111, etc.

> 编写一个名为 series_sum() 的函数，提示用户输入一个非负整数 n。如果用户输入的是负整数，则函数应返回 None，否则函数应返回以下系列的总和：$1000 + \frac{1}{1^{2}} + \frac{1}{2^{2}} +\frac{1}{3^{2}} + \frac{1}{4^{2}} + ...+\frac{1}{n^{2}}$ 对于给定的整数 n。例如，对于 n = 0，函数应返回 1000，对于 n = 1，函数应返回 1001，对于 n 2，函数应返回 1001.25，对于 n = 3，函数应返回 1001.3611111111111，等等。

测试结果/Test：

```
>>> series_sum()
Please enter a non-negative integer: -10
>>> series_sum()
Please enter a non-negative integer: 0
1000
>>> series_sum()
Please enter a non-negative integer: 5
1001.463611111111
```

解决方法：

根据测试结果Line2发现，如果用户输入一个负数，则返回None，所以我们可以先判断负值这个特殊情况

### **方法一/method 1**

```python
def series_num():
    '''
    None->float
    please enter a positive number, otherwise it will return None
    '''
    n = int(input("Please enter a non-negative integer: "))
    if n < 0: # 用户非法输入，返回空值
        return None
    
    ser_sum = 1000 # 初始化ser_num的值
    #进入循环
    for i in range(1,n+1):
        ser_sum += 1 / (i**2)
    return ser_sum
```

### **方法二/Method：**==未测试==

```python
def series_num():
    '''
    None->float
    Please enter a non-negative integer, otherwise it will return None
    '''
    n = int(input("Please enter a non-negative integer: "))
    if n < 0:
        return None
    
    return 1000 + sum(1 / (i ** 2) for i in range(1, n + 1)) # 列表推导循环
```



---

## 2.3 `pell(n)`

Pell numbers are a mathematical sequence of numbers that help approximate the value of $\sqrt{2}$ (check out the Wikipedia page on Pell Numbers: https://en.wikipedia.org/wiki/Pell_number). The sequence is defined recursively as shown in eq. 1.
$$
P_n =  \begin{cases}  0, & \text{if } n = 0 \\ 1, & \text{if } n = 1 \\ 2P_{n-1} + P_{n-2}, & \text{if } n > 1  \end{cases}
$$
Write a function called `pell()` that takes one integer parameter n, of type int. If n is negative, pell returns None. Else, pell returns the nth Pell number (i.e. $P_n$).

> 佩尔数是数学数字序列，有助于近似 $\sqrt{2}$ 的值；编写一个名为 `pell()`的函数，该函数接受一个整型参数 n，类型为 int。如果 n 为负数，pell 返回 None。否则，pell 返回第 n 个 Pell 数（即 $P_n$）

测试结果/Test Result：

```
>>> pell(0)
0
>>> pell(1)
1
>>> pell(2)
2
>>> pell(3)
5
>>> pell(-45)
>>> pell(6)
70
>>> pell(1743)
532690007842574349527112009340648584206039420554652235605917968301878560204391358977288970768088948931512979242757675577993
290392759079609635614256071618406298994532643385226638853102443318071341757012888307627361739142916789755393486051687770688
826270892256294622920292002671354119783127549690735964749390914433090966928985482211622995711178437113046183531202406642424
338067044223749234565988260287660191555741946139008489540633861672714251246514572808657156171836659007522426709678946690131
627254854511941937501064402371005017444986539854908064857327597139176688814079527858978412577793058938555244277033473983250
7514635151419472104046900160626484896467099596437905
```

```python
def pell(n):
    '''
    int -> float
    '''
    n = int(n) #整型化n
    
    if n < 0: # 判断三种特殊情况
        return None
    elif n == 0:
        return 0
    elif n == 1:
        return 1

    p0 = 0 # 初始化p0
    p1 = 1 # 初始化p1
    for i in range(2,n+1):
        p_result = 2 * p1 + p0
        p0 = p1
        p1 = p_result # 逐个回溯赋值
    return p1
```

## 2.4 `countMembers(s)`

In this question you are not allowed to use any of the Python's string methods (i.e. those string functions that you call with dot operator).

​	Say a character is `extraordinary` if it is one of the following: the lower case letter between e and j (inclusive), the upper case letters between F and X (inclusive), numerals between 2 and 6 (inclusive), and the exclamation point (!) , comma and backslash (\\)

​	You are required to count how many times these characters appear in a string.

​	Write a function called `countMembers` that takes a single input parameter s, of type str. `countMembers` then returns the number of characters in s, that are extraordinary. Therefore, if there are two Xs in s, `countMembers` must count two extraordinary characters (one for each occurrence of X in s).

> 在这个问题中，你不允许使用任何 Python 的字符串方法（即你用点运算符调用的那些字符串函数）。
>
> 如果某个字符是以下字符之一，则说它是“非凡的”：e 和 j（含）之间的小写字母，F 和 X（含）之间的大写字母，2 和 6（含）之间的数字，以及感叹号 （！） 、逗号和反斜杠 （\\）
>
> 您需要计算这些字符在字符串中出现的次数。
>
> 编写一个名为 'countMembers' 的函数，该函数采用单个输入参数 s，类型为 str。`countMembers` 然后返回 s 中的`extraordinary`字符数。因此，如果 s 中有两个 X，则 'countMembers' 必须计算两个特殊字符（每个 x 在 s 中出现）。

测试要求/Testing Requirements:

```
>>> countMembers("\\")
1
>>> countMembers("2\'")
1
>>> countMembers("1\'")
0
>>> countMembers("2aAb3?eE'_13")
4
>>> countMembers("one, Two")
3
```

### 方法一/Method 1

首先，需要识别有哪些所谓的Extraordinarily

- 小写字母e到j(包括e和j)
- 大写字母F到X(包括F和J)
- 数字2到6(包括2和6)
- 符号：感叹号、逗号、反斜杠

**这里引入一个重点ASCII码** Dec表示二进制代码，Char表示表示的内容：

| Dec  | Char | Dec  | Char  | Dec  | Char | Dec  | Char |
| ---- | :--- | ---- | ----- | ---- | ---- | ---- | ---- |
| 0    | NUL  | 32   | Space | 64   | @    | 96   | `    |
| 1    | SOH  | 33   | !     | 65   | A    | 97   | a    |
| 2    | STX  | 34   | "     | 66   | B    | 98   | b    |
| 3    | ETX  | 35   | #     | 67   | C    | 99   | c    |
| 4    | EOT  | 36   | $     | 68   | D    | 100  | d    |
| 5    | ENQ  | 37   | %     | 69   | E    | 101  | e    |
| 6    | ACK  | 38   | &     | 70   | F    | 102  | f    |
| 7    | BEL  | 39   | '     | 71   | G    | 103  | g    |
| 8    | BS   | 40   | (     | 72   | H    | 104  | h    |
| 9    | TAB  | 41   | )     | 73   | I    | 105  | i    |
| 10   | LF   | 42   | *     | 74   | J    | 106  | j    |
| 11   | VT   | 43   | +     | 75   | K    | 107  | k    |
| 12   | FF   | 44   | ,     | 76   | L    | 108  | l    |
| 13   | CR   | 45   | -     | 77   | M    | 109  | m    |
| 14   | SO   | 46   | .     | 78   | N    | 110  | n    |
| 15   | SI   | 47   | /     | 79   | O    | 111  | o    |
| 16   | DLE  | 48   | 0     | 80   | P    | 112  | p    |
| 17   | DC1  | 49   | 1     | 81   | Q    | 113  | q    |
| 18   | DC2  | 50   | 2     | 82   | R    | 114  | r    |
| 19   | DC3  | 51   | 3     | 83   | S    | 115  | s    |
| 20   | DC4  | 52   | 4     | 84   | T    | 116  | t    |
| 21   | NAK  | 53   | 5     | 85   | U    | 117  | u    |
| 22   | SYN  | 54   | 6     | 86   | V    | 118  | v    |
| 23   | ETB  | 55   | 7     | 87   | W    | 119  | w    |
| 24   | CAN  | 56   | 8     | 88   | X    | 120  | x    |
| 25   | EM   | 57   | 9     | 89   | Y    | 121  | y    |
| 26   | SUB  | 58   | :     | 90   | Z    | 122  | z    |
| 27   | ESC  | 59   | ;     | 91   | [    | 123  | {    |
| 28   | FS   | 60   | <     | 92   | \    | 124  | \|   |
| 29   | GS   | 61   | =     | 93   | ]    | 125  | }    |
| 30   | RS   | 62   | >     | 94   | ^    | 126  | ~    |
| 31   | US   | 63   | ?     | 95   | _    | 127  | DEL  |

根据题意，我们可以利用将字母或者数字转换成ASCII码值来判断他们是否在指定符号之内：

- 小写字母 e 到 j 的 ASCII 值范围为 101 到 106。
- 大写字母 F 到 X 的 ASCII 值范围为 70 到 88。
- 数字 2 到 6 的 ASCII 值范围为 50 到 54。
- 杜宇感叹号、逗号和反斜杠我们可以直接进行比较

参考代码/Keys:

```python
def countMembers(s):
    '''
    (string)->number
    '''
    count = 0 #初始化计数器
    for char in s:
        each_char = ord(char) #将每个字符串转换成ASCII码
        
        if 101 <= each_char <= 106: #检查小写e到j
            count += 1
        
        elif 70 <= each_char <= 88: #检查大写F到X
            count += 1
            
        elif 50 <= each_char <= 54: #检查2到6
            count += 1
            
        elif char == "!" or char == "," or char == "\\":
            count += 1
            
    return count
```

*注意：`ord()`不属于字符串方法，详情请查阅`help(str)`*

### 方法二/Method 2

第二种方法就是不使用ASCII码，直接进行源字符比对：

```python
def countMembers(s):
    '''
    (str) -> int
    '''
    count = 0  # 初始化计数器

    for char in s:
        # 检查小写字母 e 到 j
        if 'e' <= char <= 'j':
            count += 1
        # 检查大写字母 F 到 X
        elif 'F' <= char <= 'X':
            count += 1
        # 检查数字 2 到 6
        elif '2' <= char <= '6':
            count += 1
        
        # 检查符号 !, , 和 \
        elif char == '!' or char == ',' or char == '\\':
            count += 1
    
    return count
```

## 2.5 `casual_number(s)`

Imagine a customer in a bank is asked to enter a whole number representing their approximate monetary worth. In that case, some people use commas to separate thousands, millions etc, and some don’t. In order to perform a some calculations the bank needs that number as na integer. Write a function, called `casual_number(s)` that has one parameter, s, as input where s is a string. Function `casual_number(s)` should return an integer representing a number in s. If s does not look like a number the function should return None. Note that if a string in s looks like a number but with commas, you may assume that commas are in meaningful places i.e. you may assume that s will not be a string like ’1,1,345’.

> 假设银行的一位客户被要求输入一个整数，代表他们的大致货币价值。在这种情况下，有些人使用逗号来分隔数千、数百万等，而有些人则不使用。为了执行一些计算，银行需要该数字为 na 整数。编写一个名为 'casual_number（s）' 的函数，该函数有一个参数 s 作为输入，其中 s 是一个字符串。函数 'casual_number（s）' 应返回一个整数，表示以 s 为单位的数字。如果 s 看起来不像一个数字，则函数应返回 None。请注意，如果 s 中的字符串看起来像一个数字但带有逗号，则可以假设逗号位于有意义的位置，即可以假设 s 不会是像这样的字符串 '1,1,345’.

测试要求/Testing Requirements：

```
>>> casual_number("251")
251
>>> casual_number("1,aba,251")
>>> casual_number("1,251")
1251
>>>casual_number("1251")
1251
>>> casual_number("-97,251")
5
-97251
>>> casual_number("-97251")
-97251
>>> casual_number("-,,,,")
>>> casual_number("--97,251")
>>> casual_number("-")
>>> casual_number("-1,000,001")
-1000001
>>> casual_number("999,999,999,876")
999999999876
>>> casual_number("-2")
-2
```

### 方法一/Method 1

首先创建一个空的字符串，判断是正数还是负数，然后用for循环逐个字符判断是否为`,`如果不是则将他存进空字符串，最后检查它是否为是一个数字。

```python
def casual_number(s):
    '''
    (str) -> int
    '''
    empty_str = "" #创建一个空的字符串
    if s[0] == '-': #判断是否为负
        for char in s[1:]: #对s中第二个开始逐个检查
            if char != ",": #如果char不是逗号，那就将他存入空字符串
                empty_str += char
                
        if empty_str.isdigit():
            return -int(empty_str) #返回负数值
        else:
            return None
        
    else:
        for char in s: #对s中开始逐个检查
            if char != ",": #如果char不是逗号，那就将他存入空字符串
                empty_str += char
                
        if empty_str.isdigit():
            return int(empty_str)
        else:
            return None
```

### 方法二/Method 2

这里和上面方法相似，但是直接用replace方法，并且整合了部分代码：

```python
def casual_number(s):
    '''
    (str) -> int
    '''
    if s[0] == '-': #如果第一个字符是负号，则我们处理负数
        cleaned_s = s[1:].replace(",", "")  #处理逗号
        if cleaned_s.isdigit():  # 检查是否全是数字
            return -int(cleaned_s)
        else:
            return None  #如果非合法数字返回None
    else: # 如果没有负号，按之前的方式处理
        cleaned_s = s.replace(",", "")
        if cleaned_s.isdigit():
            return int(cleaned_s)
        else:
            return None
```

## 2.6 `alienNumbers(s)`

Strange communication has been intercepted between two alien species at war. NASAs top linguists have determined that these aliens use a weird numbering system. They have symbols for various numeric values, and they just add all the
values for the symbols in a given numeral to calculate the number. NASA’s linguists have given you the following table of
symbols and their numeric values. Since they have a lot of these numbers to compute, they want you to write a function that they can use to automate this task.

> 两个外星物种之间的奇怪通信被截获。NASA 的顶级语言学家已经确定这些外星人使用了一种奇怪的编号系统。它们有各种数值的符号，它们只是将给定数字中符号的所有值相加来计算数字。NASA 的语言学家为您提供了以下符号表及其数值。由于他们有很多这样的数字要计算，因此他们希望您编写一个他们可以用来自动执行此任务的函数。

| Symbol | Value |
| :----: | :---: |
|   T    | 1024  |
|   y    |  598  |
|   !    |  121  |
|   a    |  42   |
|   N    |   6   |
|   U    |   1   |

Thus `a!ya!U!NaU` represents a value of 1095 (see table below for an explanation).

| Numeral | Value | Occurrences |  Total Value  | Running Total |
| :-----: | :---: | :---------: | :-----------: | :-----------: |
|    T    | 1024  |      0      | 0 × 1024 = 0  |       0       |
|    y    |  598  |      1      | 1 × 598 = 598 |      598      |
|    !    |  121  |      3      | 3 × 121 = 363 |      961      |
|    a    |  42   |      3      | 3 × 42 = 126  |     1087      |
|    N    |   6   |      1      |   1 × 6 = 6   |     1093      |
|    U    |   1   |      2      |   2 × 1 = 2   |     1095      |

Write a function called `alienNumbers` that takes ==one string parameter s==, and returns the integer value represented by
s. Since aliens only know these characters you may assume that no character in s outside of this set: {T,y, !,a, N, U}.
Callenge: try to make the whole body of this function only one line long.

> 编写一个名为 `alienNumbers` 的函数，该函数采用一个字符串参数 s，并返回由 s 表示的整数值。由于外星人只知道这些字符，你可以假设 s 中没有字符超出这个集合：{T，y， ！，a， N， U}。注意：尽量使这个函数的整个主体只有一行长。

测试需求/Testing Requirements

```
>>> alienNumbers("a!ya!U!NaU")
1095
>>> alienNumbers("aaaUUU")
129
>>> alienNumbers("")
0
```



### 方法一/Method 1

一行那就一行吧（Chat GPT）

```python
def alienNumbers(s):
    '''
    (str) -> number
    '''
    return sum({'T': 1024, 'y': 598, '!': 121, 'a': 42, 'N': 6, 'U': 1}[char] for char in s)
```

### 方法二/Method 2

死办法：

```python
def alienNumbers(s):
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
```

## 2.7 `alienNumbersAgain(s)`

NASA is very pleased with your proof-of-concept solution in the previous question. Now, they’ve designed a small chip that runs a very restricted version of python - it doesn’t have any of the string methods that you are used to. They want you to now rewrite your `alienNumbers` function to run without using any of those string methods you may have otherwise used. Basically, you can use a loop of some sort and any branching you’d like, but none of the string methods. Use accumulator variable as we have seen in class.’ 

Write a function called `alienNumbersAgain`, that takes a single string parameter s, and returns the numeric value of the number that s represents in the alien numbering system.

> NASA 对您在上一个问题中的概念验证解决方案非常满意。现在，他们设计了一个小芯片，它运行一个非常受限的 python 版本，它没有任何你习惯的字符串方法。他们希望您现在重写` alienNumbers` 函数，以便在不使用任何您可能使用过的字符串方法的情况下运行。基本上，你可以使用某种类型的循环和任何你想要的分支，但不能使用任何字符串方法。使用我们在类中看到的累加器变量。编写一个名为 `alienNumbersAgain` 的函数，该函数采用单个字符串参数 s，并返回 s 在外星人编号系统中表示的数字的数值。

测试要求：

```
>>> alienNumbersAgain("a!ya!U!NaU")
1095
>>> alienNumbersAgain("aaaUUU")
129
>>> alienNumbersAgain("")
0
```

上一题的方法二.................

```python
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
```

## 2.8 `encrypt()`

​	Hint: Think of how slicing and reversing of strings can help with this problem. (We saw how to do slicing and reversing in several lectures including Lecture 8)
​	You want to send a note to your friend in class, and because you want to be respectful in class, you don’t want to whip out your phone and send a text or an email (or any other digital communication). Instead, you choose to go old school and write it out on a piece of paper and pass it along to your friend. The problem is, you don’t want anyone else to read the note as they pass it along. Luckily, your friend and you have come up with an encryption system so that nobody else can understand your message. Here’s how it works: you write out your message backwards (so, Hello, world becomes dlrow ,olleH). But you don’t stop there, because that’s too easy to crack - anyone can figure that out! Now that you’ve written in backwards, Then you start on either side of the string and bring the characters together. So the first and the last characters become the first and the second character in the encrypted string, and the second and the second last characters become the third and the fourth characters in the string, and so on. Thus, Hello, world ultimately becomes dHlerlolwo , (notice how all punctuation, special characters, spaces, etc are all treated the same) and 0123456789 becomes 9081726354. 

​	Write a function called encrypt, that has one parameter s where s is a string and `encrypt` returns a string which is the encrypted version of s.
**Fun fact** in cryptography, s is called “clear text” and the encrypted version you return is called “cipher text”

> 提示：想想如何通过对字符串进行切片和反转来解决此问题。（我们在包括第 8 讲在内的多个讲座中了解了如何进行切片和反转）您想在课堂上给您的朋友发一条消息，因为您想在课堂上保持礼貌，所以您不想掏出手机发送短信或电子邮件（或任何其他数字通信）。相反，您选择采用老式方法，将其写在一张纸上并传给您的朋友。问题是，您不希望其他人在传递消息时阅读它。幸运的是，您和您的朋友想出了一个加密系统，这样其他人就无法理解您的消息。它的工作原理如下：您将消息反向写出（因此，Hello, world 变成 dlrow,olleH）。但您不能就此止步，因为这太容易破解了，任何人都可以弄清楚！现在您已经反向书写，然后从字符串的两侧开始，将字符放在一起。因此，第一个和最后一个字符成为加密字符串中的第一个和第二个字符，第二个和倒数第二个字符成为字符串中的第三个和第四个字符，依此类推。因此，Hello, world 最终变成 dHlerlolwo，（请注意所有标点符号、特殊字符、空格等都被视为相同），0123456789 变成 9081726354。编写一个名为`encrypt` 的函数，它有一个参数 s，==其中 s 是一个字符串==，`encrypt` 返回一个字符串，它是 s 的加密版本。**有趣的事实** 在密码学中，s 被称为“明文”，而您返回的加密版本称为“密文”

测试要求：

```
>>> encrypt("Hello, world")
'dHlerlolwo ,'
>>>> encrypt("1234")
'4132'
>>> encrypt("12345")
'51423'
>>> encrypt("1")
'1'
>>> encrypt("123")
'312'
>>> encrypt("12")
'21'
>>> encrypt("Secret Message")
'eSgeacsrseetM '
>>> encrypt(",'4'r")
"r,''4"
```

### 方法一/Method 1

空字符串方法:

```python
def encrypt(s):
    reversed_s = s[::-1]
    encrypted = ""  #初始化
    length = len(reversed_s)
    
    for i in range((length + 1) // 2):
        encrypted += reversed_s[i]  #从左边
        if i != length - i - 1:  #防止在字符串长度为奇数时重复添加中间字符
            encrypted += reversed_s[length - i - 1] #从右边
    
    return encrypted
```

### 方法二/Method 2

递归方法：

```python
def encrypt(s):
    if len(s) <= 1: #only一个字符的字符串
        return s
    # 递归拼接两端的字符
    return s[-1] + s[0] + encrypt(s[1:-1])
```



其他方法：双指针、队列方法、zip()方法等

## 2.9 `oPify(s)`

Hint: Depending on how you plan to solve this problem, accumulator variable initialized as an empty string may help in this question.
	Write a function called oPify, that takes a single string parameter (s) and returns a string. This function considers every pair of consecutive characters in s. It returns a string with the letters o and p inserted between every pair of consecutive characters of s, as follows. If the first character in the pair is uppercase, it inserts an uppercase O. If however, it is lowercase, it inserts the lowercase o. If the second character is uppercase, it inserts an uppercase P. If however, it is lowercase, it inserts the lowercase p. If at least one of the character is not a letter in the alphabet, it does not insert anything between that pair. Finally, if s has one or less characters, the function returns the same string as s.
	Do dir(str) and check out methods isalpha (by typing `help(str.isalpha)` in Python shell), and isupper

> 提示： 根据你打算如何解决这个问题，初始化为空字符串的 accumulator 变量可能会对这个问题有所帮助。 编写一个名为 oPify 的函数，该函数采用单个字符串参数并返回一个字符串。此函数考虑 s 中的每对连续字符。它返回一个字符串，其中字母 o 和 p 插入到 s 的每对连续字符之间，如下所示。如果对中的第一个字符是大写的，则插入大写的 O。但是，如果它是小写的，则插入小写的 o。如果第二个字符是大写的，则插入一个大写的 P。但是，如果它是小写的，则插入小写的 p。如果至少有一个字符不是字母表中的字母，则不会在该对之间插入任何内容。最后，如果 s 具有一个或多个字符，则函数返回与 s 相同的字符串。 执行 dir（str） 并检查方法 isalpha（通过在 Python shell 中键入 `help(str.isalpha)`和 isupper

测试要求：

```
>>> oPify("aa")
'aopa'
>>> oPify("aB")
'aoPB'
>>> oPify("ooo")
'oopoopo'
>>> oPify("ax1")
'aopx1'
>>> oPify("abcdef22")
'aopbopcopdopeopf22'
>>> oPify("abcdef22x")
'aopbopcopdopeopf22x'
>>> oPify("aBCdef22x")
'aoPBOPCOpdopeopf22x'
>>> oPify("x")
'x'
>>> oPify("123456")
'123456'
```

题目要求:

如果两个字符都是字母：

- 如果第一个字符是大写字母，则在它和第二个字符之间插入 `O`，否则插入 `o`。
- 如果第二个字符是大写字母，则在它和第一个字符之间插入 `P`，否则插入 `p`。

如果至少有一个字符不是字母，则不会插入任何内容。

如果输入字符串只有一个字符或者是空字符串，返回原字符串。

### 方法一/Method 1

空字符串方法: 初始化空字符串, 便利字符串, 用`isalipha()`来判断, 再用`isupper()`来判断是否是大写, 最后累加同时将op或者OP插入

```python
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
        
        if front.isalpha() and second.isalhpa():
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
```

## 2.10 `nonrepetitive(s)`

This may be quite a challenging question to solve. Slicing and remembering that you can ask if two strings (`s1==s2`) are the same are key to a short solution to this problem.
	A nonrepetitive word is a word that does not contain any subword twice in a row. Examples: 

==ana== is nonrepetitive. 
==borborygmus== is not nonrepetitive, since it has subword, bor twice in a row.
==abracadabra== is nonrepetitive. 
==repetitive== is not nonrepetitive since subword ti is repeated twice in a row.
==grammar== is not nonrepetitive since subword m is repeated twice in a row.
==gaga== is not s nonrepetitive since subword ga is repeated twice in a row.
==rambunctious== is nonrepetitive.
==abcab== is nonrepetitive.
==abacaba== is nonrepetitive.
==zrtzghtghtghtq== is not nonrepetitive since subword ght is repeated twice (in fact three times, but it is enough to find two repetitions to conclude that the word is not nonrepetitive).
==aa== is not nonrepetitive since subword a is repeated twice.
==zatabracabrac== is not nonrepetitive since subword abrac is repeated twice in a row.
	Write a function, called `nonrepetitive`, that has one parameter, s, where s is a string. The function returns True if s is nonrepetitive and False otherwise.

> 这可能是一个相当具有挑战性的问题。切片并记住你可以问两个字符串 （`s1==s2`） 是否相同是解决这个问题的关键。 非重复词是连续两次不包含任何子词的词。示例： ==ana== 是非重复的。 ==borborygmus== 不是非重复的，因为它连续两次有子词 bor。==abracadabra== 是非重复的。 ==repetitive== 不是非重复的，因为子词 ti 连续重复两次。==grammar== 不是不重复的，因为子词 m 连续重复两次。==gaga== 不是非重复的，因为子词 ga 连续重复两次。==rambunctious== 是非重复的。==abcab== 是非重复的。==abacaba== 是非重复的。==zrtzghtghtghtq== 不是非重复的，因为子词 ght 重复了两次（实际上是重复了三次，但找到两次重复就足以得出这个单词不是非重复的结论）。==aa== 不是不重复的，因为子词 a 重复了两次。==zatabracabrac== 不是不重复的，因为子词 abrac 连续重复两次。 编写一个名为 nonrerepeated 的函数，该函数具有一个参数 s，其中 s 是一个字符串。如果 s 是非重复的，则函数返回 True，否则返回 False。

切片!!!!!!!!!!!!!!!!!!!!!i天然居考核官员才能不放心的我VS合同如果发生i户籍地你看面色成功vr

### 方法一/Method 1

```python
def nonrepetitive(s):
    length = len(s)
    
    # 遍历每个子串长度，从 1 到 l//2
    for sub_str in range(1, l // 2 + 1):
        #比较相邻的子串
        for i in range(l - 2 * sub_str + 1): # 上面取整,这里x2+1可以找到中间那个
            #两个相邻的子串进行比较
            if s[i:i+sub_str] == s[i+sub_str:i+2*sub_str]:
                return False  # 如果相邻子串相同，返回 False
    
    return True  # 如果没有相邻子串相同，则返回 True
```

### 方法二/Method 2

**扩展: 正则表达式** `<Chat GPT>`

```python
import re

def nonrepetitive(s):
    pattern = re.compile(r"(..+?)\1")
    return not bool(pattern.search(s))
```

**解释**：

1. 正则表达式解释：

   - `(..+?)`：匹配一个最短的、至少有两个字符的子串。

   - `\1`：表示该子串连续出现两次。

2. **`re.compile()`**：用来编译正则表达式模式，使其可以多次使用。

3. **`pattern.search(s)`**：搜索字符串 `s` 中是否存在匹配的连续重复子串。如果找到，则返回 `False`，否则返回 `True`。



---

<center>
    最后更改: 13 Oct. 2024 13:41 <br>
    ***** 完结撒花 *****








```python
i += 1

i = i + 1
```


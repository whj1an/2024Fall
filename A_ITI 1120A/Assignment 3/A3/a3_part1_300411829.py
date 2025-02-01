def split_tester(N, d):
    '''
    (str, int) -> numbers, boolen
    '''
    # Your code for split_tester function goes here (instead of keyword pass)
    # Your code should include  dosctrings and the body of the function
    str_n = str(N)
    int_d = int(d)

    if len(str_n) % int_d != 0:
        return False

    current_N = [str_n[i:i+int_d] for i in range (0, len(str_n), int_d)] #判断0~len间隔d个数放入c_N

    print(','.join(current_N))
    
    for i in range (1, len(current_N)):
        if current_N[i] < current_N[i-1]: #判断前一个和后一个的大小关系
            return False

    return True

# you can add more function definitions here if you like
            
# main
# Your code for the welcome message goes here, instead of name="Vida"
def ascii_name_plaque(n):
    '''
    (n) -> string
    it should be covered by "
    '''
    length=(len(n) + 6)
    print("*" * length)
    print("*" + " "*(length - 2) + "*")
    print(f"* _{n}_ *")
    print("*" + " "*(length - 2) + "*")
    print("*" * length)
    return

ascii_name_plaque("Welcome to my increasing-splits tester")
name = input("What is your name?").strip()
ascii_name_plaque(f"{name},welcome to my increasing-splits tester.")

flag=True
while flag:
    question=input(name+", would you like to test if a number admits an increasing-split of give size? ")
    question=(question.strip()).lower()
    if question=='no':
        ascii_name_plaque(f"Good bye{name}!")
        flag=False
    #YOUR CODE GOES HERE. The next line should be elif or else.
    else:
        if question != "yes":
            print("Please enter yes or no. Try again.")
        else:
            print("Good choice!")
            N = input("Enter a positive integer:").strip()
            if N[0] == '-':
                if N[1:].isdigit(): #负数时判断是否为整数
                    print("The input has to be a positive integer.Try again.")
                else:
                    print("The input can only contain digits. Try again.")
            elif not N.isdigit(): #判断是否为整数
                print("The input can only contain digits. Try again.")
            elif N == '0':
                print("The input has to be a positive integer.Try again.")
                
            else:
                d = input(f"Input the split. The split has to divide the length of {N} i.e. " + str(len(N)) + '\n').strip()
                if d[0] == '-':
                    if d[1:].isdigit():
                        print("The split has to be a positive integer.Try again.")
                    else:
                        print("The split can only contain digits. Try again.")
                elif not d.isdigit():
                    print("The split can only contain digits. Try again.")
                elif d == '0':
                    print("The split has to be a positive integer.Try again.")
                else:
                    if len(N) % int(d) != 0:
                        print(f"{d} does not divide {len(N)}. Try again.") #不能被整除
                    else: #可以被整除
                        if split_tester(N,d):
                            print("The sequence is increasing")
                        else:
                            print("The sequence is not increasing")
                    
                
#finally your code goes here too.

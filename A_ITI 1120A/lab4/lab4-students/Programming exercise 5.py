def prime_num():
    num = int(input("Please enter a number: "))
    for i in range(1,num+1):
        if (num/i)%1 == 0:
            print(i,end=" ")
        else:
            i+=1
    return

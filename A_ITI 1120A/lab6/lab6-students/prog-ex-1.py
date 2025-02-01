def sum_odd_while_v2(n):
     '''(int)->int
        Returns the sum of all odd integers between 5 and n
        '''
     odd_num = 5
     sum1 = 0
     while odd_num < n:
          sum1 += odd_num
          odd_num += 2
     return sum1

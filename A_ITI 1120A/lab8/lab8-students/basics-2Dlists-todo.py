import random
def get_matrix_dimensions():
     got_it_flag=False
     while not(got_it_flag):
          try:
               a=int(input("Enter a positive number for the number of rows: "))
               b=int(input("Enter a positive number for the number of columns: "))
               if(a>0 and b>0):
                    got_it_flag=True
               else:
                    print("Both numbers must be positive integers")
          except ValueError:
               print("Both numbers must be an integer")
               
     return (a,b) # note that this returns a tuple, i.e. immutable list of lenght 2

def make_matrix(a,b, value):
     '''(int,int,Object)->2D list

     Returns a 2D list representing a matarix with a rows and b columns
     where each element of the matrix is equal to the given value
     Note that the value can be anything, number, string, None ...
     In that case type contract should just say "Object"
     
     Precondition: a and b are both positive integers
     '''

     m=[] # make an empty list
     for i in range(a):
          row=[] # make an empty row
          for j in range (b):
               row.append(value)
          m.append(row)
     return m
     
def print_matrix(m):
     '''(2D list)->None
     prints values in 2D list m row by row'''
     for row in m:
          for item in row:         #print item followed by 
               print(item, end=' ')    #a blank space
          print()                  # move to next line

def increment_all_matrix(m):
     '''(2D list)->None
        increments each number in 2D list m by 1
        Precondition: m represents a matrix, i.e. each element of m is a list of same length; and
                      all elements of the matrix a numbers'''
     nrows=len(m)
     ncols=len(m[0]) # we can do this since all elements of m  
     for i in range(nrows):
          for j in range(ncols):
               m[i][j]=m[i][j]+1


def min_matrix(m):
     '''(2D list)->number
     Returns the minimum number from the given 2D list m
     Precondition: m represents a matrix all of whose elements are numbers and
                   and m has at least 1 raw and 1 columb'''
     
     minimum=m[0][0]
     for i in range(len(m)):
          for j in range(len(m[i])):
               if m[i][j] < minimum: # if yes, we found smaller number
                    minimum=m[i][j]  # update minimum
     return minimum

def sum_each_col(m):
     '''(2D list)->list
     Returns a list where in position p of the list is the sum of the elements of p-th column of m
     Precondition: m represents a matrix all of whose elements are numbers and
                   and m has at least 1 raw and 1 columb'''
     nrows=len(m)
     ncols=len(m[0])
     sums=[]
     for j in range(ncols):
          col_sum=0
          for i in range(nrows):
               col_sum=col_sum+m[i][j]
          sums.append(col_sum)
     return sums       

# programming exercise  1

def make_matrix_random(a,b, x, y):
     '''(int,int,int)->2D list
     Returns a 2D list representing a matrix with a rows and b columns
     filled with random integers >=x and <=y
     Precondition: a,b positive and x <=y
     '''
     # your code goes here
     matrix = []
     for i in range(a):
          matrix_row = []
          for j in range(b):
               matrix_row.append(random.randint(x,y))
          matrix.append(matrix_row)
     return matrix
     #O(a*b)


# programming exercise  2
def sum_above_diagonal(m):
     '''(2D list)->number
     Returns the sum of the elements of the matarix m that are on or about the diagonal of m
     (for clarification see the slide entitled: Details about Prog Ex 2)
     Precondition: m is a square matrix filled with numbers

     >>> sum_above_diagonal([[1,2],[10,20]] )
     23
     '''
     # your code goes here
     final_sum = 0
     for i in range(len(m)):
          final_sum += m[i][i]
     return final_sum
     
     

# programming exercise  3
def max_over_all_even_cols(m):
     '''(2D list)->number
     Returns the maximum element among all the numbers that are in even columns of m
     i.e the maximum element amoung all elements in 0th, 2th, 4th etc. column
     Precondition: m is a matrix filled with numbers with at least 1 row and 1 column
     
     >>> max_over_all_even_cols([1,1,1,1,1,1,1],[1,10,3,20,12,6,0] )
     12
     '''
     # your code goes here
     max_num = m[0][0]
     for i in range(len(m)):
          for j in range(0,len(m[i]),2):
               if m[i][j] > max_num : max_num = m[i][j]
     return max_num
     

#programming exercise  4
def max_each_row(m):
     '''(2D list)->list
     Returns a list where in position p of the list is the max number among all the numebrs of p-th row of m
     Precondition: m is a matrix filled with numbers

     >>> max_each_row([[1,2],[200,0],[3,3],[-10,-20]])
     [2, 200, 3, -10]
     '''
     # your code goes here
     out_list = []
     for i in range(len(m)):
          a = max(m[i])
          out_list.append(a)
     return out_list
     

# programming exercise  5
def index_of_max_sum_row(m):
     '''(2D list)->int
     Returns the index of a row that has the largest sum of all the rows
     Precondition: m is a matrix filled with numbers
     >>> index_of_max_sum_row([[100,100], [-100,0], [200,30], [1,2]])
     2
     >>> index_of_max_sum_row([[100,100], [-100,0], [200,30], [10000,2]])
     3
     '''
     # your code goes here
     largest_sum = sum(m[0])
     largest_index = 0
     for i in range(1, len(m)):
          # row_sum = sum(m[i])
          if sum(m[i]) > largest_sum:
               largest_sum = sum(m[i])
               largest_index = i
     return largest_index


# main

# testing obtaining the right dimensions
dimensions=get_matrix_dimensions()
a=dimensions[0]
b=dimensions[1]

# testing make_matrix
# create an a x b matrix, called m, filled with 1s
m=make_matrix(a,b,1)
print_matrix(m)

# testing increment_all_matrix
increment_all_matrix(m)
print_matrix(m)

# testing min_matrix function
print(min_matrix([[1,2,0],[-1,1,100],[100,-2,5]]))

# testing sum_each_col funciton
print( sum_each_col([[1,2,10],[1,2,10],[0,0,0]]) )

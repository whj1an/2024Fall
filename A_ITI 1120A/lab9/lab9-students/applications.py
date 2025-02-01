# QUESTION 1

def element_uniqueness(L):
     '''(list)->bool
     Returns True if all the elements in the list are distinct,
     in other words, if there is no element in the list that appears more than once.
     Precondition: L is not empty

     >>> element_uniqueness([2, 2,2, 2, 8])
     False
     >>> element_uniqueness([1,-20,-1])
     True
     >>> element_uniqueness([3,2,4,0,3])
     False
     >>> element_uniqueness([10])
     True
     >>> element_uniqueness([10,10])
     False
     >>> element_uniqueness([10,-1])
     True
     '''
     for i in range(len(L)):
          if L[i].count() > 1:
               return False
     return True
 
# QUESTION 2

def one_unique_at_least(L):
     '''(list)->bool
     Returns True if there exist at least one element in L that is unique,
     in other words, that appears exactlly once in the list
     Precondition: L is not empty
     >>> one_unique_at_least([2,2,2,2,8])
     True
     >>> one_unique_at_least([2,1,2])
     True
     >>> one_unique_at_least([1,-20,-1])
     True
     >>> one_unique_at_least([3,2,2,3,3])
     False
     >>> one_unique_at_least([10])
     True
     >>> one_unique_at_least([10,10])
     False
     >>> one_unique_at_least([10,-1])
     True
     '''
     L.sort()
     for i in range(len(L)-1):
          if L[i] == L[i+1]:
               return False
     return True

# QUESTION 3
     
def all_unique(L):
     ''' (list,int)->list
     Return a list of elements of L that appear exactlly once in L. 
     Precondition: L is not empty
    
     >>> all_unique([2, 2,2, 2, 8])
     [8]
     >>> all_unique([1,-20,-1])
     [-20,-1,,1]
     >>> all_unique([3,2,2,3,3])
     []
     >>> all_unique([10])
     [10]
     >>> all_unique([10,10])
     []
     >>> all_unique([10,-1])
     [-1,10]
     '''
     new_lst = []
     for i in range(len(L)):
          if L[i].count == 1:
               new_lst.append(L[i])
     return new_lst
 

# QUESTION 1 again

def element_uniqueness_v2(L):
     # make now a 2nd solution to element_uniqueness
     # by making a call to all_unique
     new_lst = all_unique(L)
     if new_lst = L:
          return True
     return False
 

# QUESTION 2 again

def one_unique_at_least_v2(L):
     # make now a 2nd solution to one_unique_at_least_v2
     # by making a call to all_unique
     new_lst = all_unique(L)
     if len(L) == len(new_lst):
          return True
     return False

# QUESTION 4

def count_unique(L):
     '''(list,int)->int
     Return the number of unique elements of L,
     i.e. the number of elements that appear exactlly once in L
     Precondition: L is not empty
    
     >>> count_unique([2, 2,2, 2, 8])
     1
     >>> count_unique([1,-20,-1])
     3
     >>> count_unique([3,2,2,3,3])
     0
     >>> count_unique([10])
     1
     >>> count_unique([10,10])
     0
     >>> count_unique([10,-1])
     2
     '''
     counter = 0
     for i in range(len(L)):
          if L[i].count() == 1:
               counter += 1
     return counter


# QUESTION 5                               

def duplicates(L):
     ''' (list)->int
     Returns True if the given list L has duplicates, in other,
     if it has at least one element that appears two or more times.
     Precondition: L is not empty

     >>> duplicates([2, 2,2, 2, 8])
     True
     >>> duplicates([1,-20,-1])
     False
     >>> duplicates([3,2,2,3,3])
     True
     >>> duplicates([10])
     False
     >>> duplicates([10,10])
     True
     >>> duplicates([10,-1])
     False
     '''
     for i in range(len(L)):
          L[i].count > 1:
               return True
     return False

# QUESTION 6

def majority(L):
     '''(list)->
     An element of a list is called "majority" if MORE THAN half of the elements of the list are equal to it.
     This function returns the majority element of L if such an element exsits, otherwise it returns None
     >>> majority([2,1,2])
     2
     >>> majority([10,5,1,5,5])
     5
     >>> majority([5,5,1,1])
     
     >>> majority([3])
     3
     >>> majority([8,8,2,8])
     8
     '''




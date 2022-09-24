# 

'''
part of list_comprehension 
Output expression,
Input sequence,
A variable representing a member of the input sequence and
An optional predicate part.

even_l=[x for x in l if x%2==0]  initial x is output expression
in l -- Input sequence

second x is variable 
if part is optional predicate part-- 


[start : stop : steps] 



'''''

l=[2,3,4,8,9,13,16,18]

even_l=[x for x in l if x%2==0]  # will create new list of even

l1=[x*x+1 for x in l ] # all the calulation or excepted output should done in initial of the list
print(l1)

odd_l=[x for x in l if x%2 !=0] # will create new list of odd
print(even_l)
print(odd_l)

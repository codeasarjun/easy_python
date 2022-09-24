# in this example will try to understand nesting list comprehension

l=[2,3,4,8,9,13,16,18]


l1=[[x+50 for x in l]  for y in l] # second for loop will help to loop the inputs 

print(l1)



# flatten a given 2-D list  
# will make 2 D list in 1D by nesting list comprehension

l=[[1, 2, 3], [4, 5], [6, 7, 8, 9]]


flatten_l = [val for sublist in l for val in sublist]
  
print(flatten_l)



even_flatten_l=[val for sublist in l for val in sublist if val%2==0]  # using if in nesting the list 

print(even_flatten_l)


'''
flatten_l  = [val  # suggests what we want to append to the list
                 for sublist in matrix  # for sublist in matrix’ returns the sublists inside the matrix one by one which would be:[1, 2, 3], [4, 5], [6, 7, 8, 9]
                  for val in sublist]  # for val in sublist’ returns all the values inside the sublist. Hence if sublist = [1, 2, 3], ‘for val in sublist’ –> gives 1, 2, 3 as output one by one.
                  
                    
'''

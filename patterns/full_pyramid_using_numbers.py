# full_pyramid_using_numbers

'''
     0
    012
   01234
  0123456
 012345678
 
 '''
n=int(input('please enter number of rows '))
space=0
for i in range(n):
    for j in range(1,(n-i)+1):
        print(end=" ")
 
    while space!=(2*i)+1:
        print(space,end="")
        space+=1
    
    space=0
    print()

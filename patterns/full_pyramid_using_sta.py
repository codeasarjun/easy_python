# full pyramid using *

'''
     *
    ***
   *****
  *******
 *********
 
 '''
n=int(input('please enter number of rows '))
space=0
for i in range(n):
    for j in range(1,(n-i)+1):
        print(end=" ")
 
    while space!=(2*i)+1:
        print('*',end="")
        space+=1
    space=0
    print()

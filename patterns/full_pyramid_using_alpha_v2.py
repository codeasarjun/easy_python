# full_pyramid_using_alpha
'''
     A
    BBB
   CCCCC
  DDDDDDD
 EEEEEEEEE
 
 '''

n=int(input('please enter number of rows '))
space=0
alpha=0
for i in range(n):
    for j in range(1,(n-i)+1):
        print(end=" ")
 
    while space!=(2*i)+1:
        print(chr(65+alpha),end="")
        
        space+=1
    alpha+=1
    space=0
    print()

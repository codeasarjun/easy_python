# full pyramid using alpha 
'''
     A
    BCD
   EFGHI
  JKLMNOP
 QRSTUVWXY
 
 '''

n=int(input('please enter number of rows '))
space=0
alpha=0
for i in range(n):
    for j in range(1,(n-i)+1):
        print(end=" ")
 
    while space!=(2*i)+1:
        print(chr(65+alpha),end="")
        alpha+=1
        space+=1
    space=0
    print()

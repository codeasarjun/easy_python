# Inverted_Right_Triangle

'''
*******
******
*****
****
***
**
*

'''

n=int(input('please enter numbers of row needed '))
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print("*",end="")
        
    print("")

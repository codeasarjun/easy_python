# Right_Triangle_'*'
'''
*
**
***
****
*****
******

'''




n=int(input('please enter number of rows'))
for i in range(n):
    for j in range(0,i):
        print("*",end="")
    print("")

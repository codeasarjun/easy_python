# half diamond

'''
*
**
***
****
*****
****
***
**
*
'''








n=int(input("Please enter an integer value "))
for i in range(1,n):
    for j in range(0,i):
        print("*",end="")
    print("")
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print("*",end="")
        
    print("")

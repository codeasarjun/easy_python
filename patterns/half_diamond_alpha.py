# half_diamond using using alpha 
'''
A
AB
ABC
ABCD
EFG
HI
J

'''

n=int(input("Please enter an integer value "))
for i in range(0,n):
    for j in range(0,i):
        print(chr(65+j),end="")
    print("")
al=0
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(chr(65+al),end="")
        al+=1
        
    print("")

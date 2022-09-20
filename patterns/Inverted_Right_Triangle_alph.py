# Inverted_Right_Triangle alpha
'''
AAAAA
BBBB
CCC
DD
E
'''

n=int(input('enter number of rows'))
k=0
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(chr(65+k),end="")
    k+=1
    print()

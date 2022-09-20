#Right_Triangle_ using alpha 2
'''
A
BB
CCC
DDDD
'''



n=int(input("Please enter an interger "))
al=0
for i in range(1,n):
    for j in range(1,i+1):
        print(chr(65+al),end="")
    al+=1
    print('')

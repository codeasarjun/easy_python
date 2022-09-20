# Right_Triangle_ using numbers 
'''
1
12
123
1234
12345

'''
n=int(input("Please enter an interger "))
for i in range(1,n):
    for j in range(1,i+1):
        print(j,end="")
    print('')

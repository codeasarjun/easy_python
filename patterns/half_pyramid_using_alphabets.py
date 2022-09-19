# Program to print half pyramid using alphabets

'''
A
B B
C C C
D D D D
E E E E E
'''

n_rows=int(input('Please enter number of rows needed')) # rows

ascii_value=65
for i in range(n_rows):
    for j in range(i+1):
        print(chr(ascii_value),end="")
    ascii_value+=1
    print()
 

# half pyramid using alphabets
'''
A
AB
ABC
ABCD
ABCDE

'''

n_rows=int(input('Please enter number of rows needed')) # rows

for i in range(n_rows):
    for j in range(i+1):
        print(chr(j+65),end="")
    print()

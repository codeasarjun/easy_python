# half pyramid a using numbers
'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''

n_rows=int(input('Please enter number of rows needed')) # rows


for i in range(n_rows):
    for j in range(i+1):
        print(j+1,end="")
    print()

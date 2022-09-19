# Program to print half pyramid using 
'''

*
* *
* * *
* * * *
* * * * *

'''

n_rows=int(input('Please enter number of rows needed')) # rows


for i in range(n_rows):
    for j in range(i+1):
        print('*',end="")
    print()

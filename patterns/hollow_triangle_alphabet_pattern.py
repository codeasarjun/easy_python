# hollow triangle alphabet pattern

'''

A
AB
A B
A  B
A   B
ABCDEF

'''
n=int(input('please enter number of rows'))
for i in range(1, n+1):
    count = 0
    for j in range(i):
        # print alphabets only at start and end of the row
        if j == 0 or j == i-1:
            print(chr(65 + count), end='')
            count += 1
        # print only alphabets if it's last row
        else:
            if i != n:
                print(' ', end='')
            else:
                print(chr(65 + count), end='')
                count += 1
    print()

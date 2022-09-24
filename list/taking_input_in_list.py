# will take user inputs and will store the same in the list 
# simple input using map and split 

arr=list(map(int,input('please enter list elements').split()))
print(arr)

# in above int will typecast the input value to int 

# taking list input for given size

n=int(input('please enter size for list'))

arr2=list(map(int, input(f'please enter {n} elements').split()))[:n]  # this n fix the size for the list
print(arr2)

# here if we try to give inputs more than size n -- there will not be any error but arr2 will only store values for size n

#  
# right_shifted_right_angle_using number  

'''
     1
    12
   123
  1234
 12345
 
 '''

n=int(input('please enter number of rows '))
for i in range(n):
    for j in range(n-i):
        print(end=" ")
    for k in range(1,i+1):
        print(k,end="")
    print()

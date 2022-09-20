# right_shifted_right_angle_*
'''
          *
         **
        ***
       ****
      *****
     ******
    *******
   ********
  *********
 **********
'''

n=int(input('please enter number of rows '))
for i in range(n):
    for j in range(n-i):
        print(end=" ")
    for k in range(i+1):
        print('*',end="")
    print()
    

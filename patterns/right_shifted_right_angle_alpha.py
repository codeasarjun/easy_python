# right_shifted_right_angle_using_alpha
'''
      A
     BC
    DEF
   GHIJ
  KLMNO
 PQRSTU
 '''

n=int(input('please enter number of rows '))
alpha=0
for i in range(n):
    for j in range(n-i):
        print(end=" ")
    for k in range(1,i+1):
        print(chr(65+alpha),end="")
        alpha+=1
    print()

#right_shifted_right_angle_using_alphabets_2

'''
                          A
                         BB
                        CCC
                       DDDD
                      EEEEE
                     FFFFFF
                    GGGGGGG
                   HHHHHHHH
                  IIIIIIIII
                 JJJJJJJJJJ
                KKKKKKKKKKK
               LLLLLLLLLLLL
              MMMMMMMMMMMMM
             NNNNNNNNNNNNNN
            OOOOOOOOOOOOOOO
           PPPPPPPPPPPPPPPP
          QQQQQQQQQQQQQQQQQ
         RRRRRRRRRRRRRRRRRR
        SSSSSSSSSSSSSSSSSSS
       TTTTTTTTTTTTTTTTTTTT
      UUUUUUUUUUUUUUUUUUUUU
     VVVVVVVVVVVVVVVVVVVVVV
    WWWWWWWWWWWWWWWWWWWWWWW
   XXXXXXXXXXXXXXXXXXXXXXXX
  YYYYYYYYYYYYYYYYYYYYYYYYY
 ZZZZZZZZZZZZZZZZZZZZZZZZZZ
'''

n=int(input('please enter number of rows '))
alpha=0
for i in range(n):
    for j in range(n-i):
        print(end=" ")
    for k in range(i+1):
        print(chr(65+alpha),end="")
    alpha+=1
    print()

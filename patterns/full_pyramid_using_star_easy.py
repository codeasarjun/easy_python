# full_pyramid_using_star_easy.py

'''
       * 
      * * 
     * * * 
    * * * * 
   * * * * * 
  * * * * * * 
 * * * * * * * 
* * * * * * * * 
'''


n=int(input('please enter number rows'))
for i in range(n):
    for j in range(1,n):
        print(end=" ")
    for k in range(0,i+1):
        print('* ',end="")
    n-=1
    print()

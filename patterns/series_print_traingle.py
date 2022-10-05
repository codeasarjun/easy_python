'''
Write a program that receives a number n as input and prints it in the following format as shown below.
Like for n = 2 the pattern will be:
1*2*5*6
--3*4

Example 1:

Input: n = 3
Output: 
1*2*3*10*11*12
--4*5*8*9
----6*7

'''

def pattern(self, n):
        # code here
        l=(n*(n+1))//2        #initializing the last pointer
        r=l+1 
        sol=[]                         #creating list for storing each row
        for i in range(n):                      #loop for each new line
            for j in range(i+1):                   #loop for digits 
                if j==0:
                    temp=str(l) + "*"  + str(r)     
                    l-=1                            #decrementing left pointer
                    r+=1                            #incrementing right pointer
                else:    
                    temp=str(l) + "*" + temp + "*" + str(r)    #adding * and value at left and right
                    l-=1 
                    r+=1 
            sol.insert(0,temp)               #inserting each line to sol from front end
        for i in range(n):
            sol[i]="--"*(i)+sol[i]           #inserting "--" i times in ith line
        return sol

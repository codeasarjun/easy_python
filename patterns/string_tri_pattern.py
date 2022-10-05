'''
Given a string of a constant length, print a triangle out of it. The triangle should start with the given string and keeps shrinking downwards by removing one character from the begining of the string. The spaces on the left side of the triangle should be replaced with dot character.

 

Example 1:

Input:
S = Geeks
Output:
Geeks
.eeks
..eks
...ks
....s

'''



def triDownwards(self, S):
        # code here
        
        res=''
        for i in range(len(S)):
            for j in range(len(S)):
                if i>j:
                    res+='.'
                else:
                    res+=S[j]
        return res

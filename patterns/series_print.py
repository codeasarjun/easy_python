
'''
Print a sequence of numbers starting with N where A[0] = N, without using loop, in which  A[i+1] = A[i] - 5,  until A[i] > 0. After that A[i+1] = A[i] + 5  repeat it until A[i] = N.

Example 1:

Input: N = 16
Output: 16 11 6 1 -4 1 6 11 16
Explaination: The value decreases until it 
is greater than 0. After that it increases 
and stops when it becomes 16 again.

'''

#User function Template for python3
import sys
sys.setrecursionlimit(10**6)
class Solution:
    def solve(self,N,arr):
        arr.append(N)
        if N<=0:
            return arr
        
        self.solve(N-5,arr)
        arr.append(N)
        return arr
    def pattern(self, N):
        arr=[]
        
        return self.solve(N,arr)

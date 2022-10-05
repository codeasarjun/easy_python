'''
Given an integer n. Return the nth row of the following look-and-say pattern.
1
11
21
1211
111221
Look-and-Say Pattern:

To generate a member of the sequence from the previous member, read off the digits of the previous member, counting the number of digits in groups of the same digit. For example:

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
1211 is read off as "one 1, one 2, then two 1s" or 111221.
111221 is read off as "three 1s, two 2s, then one 1" or 312211.
Example 1:

Input:
n = 5
Output: 111221
Explanation: The 5th row of the given pattern
will be 111221.


'''




def lookandsay(self, n):

        if n==1:

            return '1'

        res=self.lookandsay(n-1)

        res=str(res)

        count=0

        ans=''

        for i in range(0,len(res)):

            count+=1

            if i==len(res)-1 or res[i]!=res[i+1] :

                ans+=str(count)+res[i]

                count=0

        return ans

/*
You a given a number N. You need to print the pattern for the given value of N.

For N = 2 the pattern will be 
2 2 1 1
2 1

For N = 3 the pattern will be 
3 3 3 2 2 2 1 1 1
3 3 2 2 1 1
3 2 1

Note: Instead of printing a new line print a "$" without quotes.

Example 1:

Input: 2
Output:
2 2 1 1 $2 1 $


*/



void printPat(int n)
    {
         // Your code here
    for( int i=1 ; i<=n ; i++)

    {

      for(int j=n ; j>=1 ; j--)

      {

        for(int k=n ; k>=i ; k--)

        {

          System.out.print(j+" ");

        }

      }

      System.out.print('$');

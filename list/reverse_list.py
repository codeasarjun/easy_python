# reverse() -- it doesn’t use any extra space but it just modifies the original list.


l=[1,2,3]
l.reverse() # reverse 
print(l)


# reversed() method returns an iterator that accesses the given sequence in the reverse order.

rev_l=list(reversed(l)) # reversin the list but it will have iterator 
for i in reversed(l): # no need to use len or range funtion 
    print(i)
print(rev_l)
print(l)

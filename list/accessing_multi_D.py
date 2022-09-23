
# in multi D list, each new list element will start from 0 indexing 

# in l if we need to print 30 then first we need to go to [4] then [0] so l[4][0]

l=[1,8,'A','Sun',[30,1000],[1,[2,3]]]
print(l[0]) # print the elemnt @ 0 indx
print(l[4][0]) # will print 30

print(l[-1][1][0]) # will print 2 
for i in l:  # will print each elements 
    print(i)

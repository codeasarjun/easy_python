'''
Time Complexity : O(n) 

Auxiliary Space : O(n)

'''



from collections import defaultdict
arr = [10, 20, 20, 10, 10, 20, 5, 20 ]
d=dict()
for i in range(len(arr)):
    if arr[i] in d.keys():
        d[arr[i]]+=1
    else:
        d[arr[i]]=1
print(d)



# using of defaultdict will not give key error 
m=defaultdict(int)

for i in arr:
   m[i]+=1
print(m)

for key,value in m.items():
    print(key,'-------',value)

# list comprehension 

x=[1,2,3,4,5,6]

y=[a*2 for a in x]
print("List 1",x)
print('Comprehesion list',y)

# make another list wiht even number only 

even=[a for a in x if a%2==0]
print(even)

z=x+y
f=[1,2,[2,3,[4,5,6]]]
print(f)

print(len(f))
print(f[0])
print(f[1])
print(f[2][0])
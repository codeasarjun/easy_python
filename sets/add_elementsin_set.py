# add() method add set elements but cannto add list or tuples to id


l={'raj',20,30,'some'}
l.add('FB')
print(l)

# update() method can add list/tuples/set to a set 


l={'raj',20,30,'some'}
d=[1,2]
t=('a','b','a')

l.update(d,t)
print(l)

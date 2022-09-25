# If the item to remove does not exist, remove() will raise an error.

l={'raj',20,30,'some'}
l.remove(20)
print(l)

# If the item to remove does not exist, discard() will NOT raise an error.
l={'raj',20,30,'some'}
l.discard(20)
l.discard(20) # second time removing the same element but it will not give the error 
print(l)

# pop() method to remove an item, but this method will remove the last item.


l={'raj',20,30,'some'}
l.pop()

print(l)


# clear() method empties the set:


l={'raj',20,30,'some'}
l.clear()

print(l)

# del keyword will delete the set completely:

l={'raj',20,30,'some'}
del l

print(l)

# after runing it will give the error 
'''
  File "<string>", line 4, in <module>
NameError: name 'l' is not defined
'''

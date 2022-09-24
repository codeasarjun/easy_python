# remove() method in List will only remove the first occurrence of the searched element.

'''
Time Complexity: O(n)

Space Complexity: O(1)

'''

l=[1,2,3,2,3]
l.remove(3) # it will remove first 3 
print(l)


'''
pop() function can also be used to remove and element  and return that  element from the list, 
 by default it removes only the last element of the list, 
 to remove an element from a specific position of the List, the index of the element is passed as an argument to the pop() method.

Time Complexity: O(1)/O(n) (O(1) for removing the last element, O(n) for removing the first and middle elements)

Space Complexity: O(1)


'''

l=[1,2,3,2,3]

l.pop() # will remove last element 
l.pop(2) # will remove element @ index 2

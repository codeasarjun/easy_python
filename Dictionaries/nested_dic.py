
d={
    'Class A':{'option 1':'BCA','option 2':'BCA DS'}, # dict 1
    'Class B':{'option 1':'MCA','option 2':'MTech'}  # dict 2
    
}

print(d['Class A']) # can be print inside dict by defining the name

print(d['Class A']['option 1'])# can access keys inside nested dic


# adding value to nested dict 

d['Class C']={'Option 1':'BA','Option 2':'MA'} # adding a new dic inside a dic


#deleting dic from nested dic 

del d['Class C'] # menetion the name of inside dic 
del d['Class A']['option 1'] # mention key of inside dic 



print(d)

'''looping in nested des 
'''
for keys,value in d.items(): # will unpack outer dic
    print(keys,'----',value)
    for key in value: # unpacking inside dic 
        print(key,'-----',value[key])

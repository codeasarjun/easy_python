d={
    'name':'raj',
    'class':2020,
    'place':'Earth',
    'code in':'python'
    
}

print(d['name'])  # by using key 

print(d.get('name')) # using get function to call key value 

print(d.keys()) # print all the keys 

print(d.values()) # print values of the dict

print(d.items())  #print key value pairs in tuple
####################
#####################
#####################



for key,item in d.items(): # this will unpack the dic
    print(key,"----",item)

    ''

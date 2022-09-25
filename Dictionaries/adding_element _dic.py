d={
    'name':'raj',
    'class':2020,
    'place':'Earth',
    'code in':'python'
    
}

d['DBSM']='sql' # simple add key value pair 
d['class']=2021 # will update the value 

d.update({  # using update, it will only add if value is not in dict
        'view':2045,
        'name':'raj' # its already in the dict hence no change 
    })
print(d)

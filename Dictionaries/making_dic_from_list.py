l=['name','raj','clas',2020]
step = iter(l) # will make it iter
d=dict(zip(step,step)) # zip value inside step 
print(d)

# dic comprhension 
### imp 
dic={l[i]: l[i+1] for i in range(0,len(l),2)}
print(dic)



# using two list

dummy_keys=['name','class']
dummy_values=['OOO',2021]

dic1={dummy_keys[i]:dummy_values[i] for i in range(len(dummy_keys))}
print(dic1)


dic2=dict(zip(dummy_keys,dummy_values))
print(dic2)

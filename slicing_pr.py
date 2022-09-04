'''
In this program will try to use slicing 

'''

class strin_g:

    def slice(self, x):
        return x[2:]


d=strin_g()
txt="My Name Is"
print('Sliced with pos+ Index',d.slice(txt))

# slicing from -1 indes 
d='arjun'
print(d[-3:-2])
print(d.upper()) # convert in upper case 
print(d.strip()) # remove any whitespace in start and in end 

d=100.500505
print(f"Arjun {d:.2f}")  # format 


print("My name is \"Arjun\"")

print("{0:.2f}".format(d))



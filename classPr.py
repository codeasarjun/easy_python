# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 13:37:09 2022

@author: arjun
"""

class student:
    '''This class will help to identify somethinng 
    '''
    def __init__(self,rol):
        self.rolnumber=rol
    def showData(self):
        print(f"student roll number is {self.rolnumber}")


class sDetails(student):
    def __init__(self, name):
        self.name=name
    def pdata(self):
       
        print(self.name)
    

a=student(123)
b=sDetails('anu')
b.pdata()
print(a.__doc__)
a.showData()



class student:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return f"Name of the student {self.name}"
s=student('anuj')
print(s)





class student:
    def __init__(self,name):
        self.name=name
    def p(self):
        return f"Name of the student {self.name} and rol {self.r}"
class lab(student):
    def __init__(self,name,roll):
        super().__init__(name)
        self.r=roll
    def p(self):
        return f"Name {self.name} and roll {self.r}"
s=lab('anuj',123)
print(s.p())


class student:
    session=2021
    def __init__(self,name):
        self.name=name
    def show(self):
        return f"Name of the student : {self.name}"
class MCA(student):
    def __init__(self,name,city):
        super().__init__(name)
        self.city=city
    def show(self):
     super().show()
        return f"student belongs from {self.city} and name is {self.name} and session {self.session}"
s=MCA('Arjun','Delhi')
print(s.show())



x={'name': 'arjun',
'class':'MCA'
}
x.update({"session":2020})
print(x)



class  toosmallvalue(Exception):
    pass
x=3
try:
    if x<5:
        raise toosmallvalue
except toosmallvalue:
    print("value is two small")
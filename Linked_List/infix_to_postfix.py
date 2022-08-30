# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 08:15:47 2022

@author: arjun

infix to postfix conversion   // improvement is needed

"""

operators=['+','-','/','*','(',')','^']

priority={'+':1,'-':1,'/':2,'*':2,'^':3}

def infxtopostfix(exp):
    stack=[]
    output=''
    
    for char in exp:
        
        
        if char not in operators:
            output+=char
            
        elif char=='(':
            stack.append('(')
            
            
        elif char==')':
            
            
            
            while stack and stack[-1] !='(':
                output+=stack.pop()
                
                
                
            stack.pop()
            
        else:
            while stack and stack[-1]!='(' and priority[char]<=priority[stack[-1]]:
                output+=stack.pop()
            stack.append(char)
        while stack:
            output+=stack.pop()
        return output 
    
    
exp="2+5"

print(infxtopostfix(exp))
            
       
        
        
    


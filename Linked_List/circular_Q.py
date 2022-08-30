# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 15:30:08 2022

@author: arjun


"""

class circularQ:
    
    def __init__(self,size):
        self.size=size
        self.head=self.tail=-1
        
    def enQ(self,data):
        
        if (self.tail+1)%self.size==self.head:
            print("q is full")
        
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 08:14:06 2022

@author: arjun

insert at the end
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self,nodes=None):
        self.head=None
        if nodes is not None:
            node=Node(data=nodes.pop(0))
            self.head=node
        for el in nodes:
            node.next=Node(data=el)
            node=node.next
    def printL(self):
        node=self.head
        while node is not None:
            print(node.data,"-->>",end="")
            node=node.next
        print('null')
        
    def insertE(self,new_data):
        new_node=Node(new_data)
        c_node=self.head
        if c_node is None:
            c_node=new_node
            return 
        last=c_node
        while last.next:
            last=last.next
        last.next=new_node
        
l=[1,2]
ll=linkedlist(l)
print('before insertion ')
ll.printL()
ll.insertE(67)
print("\n\n\nafter insertion")
ll.printL()

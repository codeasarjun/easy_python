# -*- coding: utf-8 -*-
"""///
Created on Sun Jul 17 08:06:40 2022

@author: arjun

insert at the front  of the list 
"""
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
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
            print(node.data,'-->>',end='')
            node=node.next
    
    # function to insert the node at front 
    
    def insertF(self,new_data):
        new_nod=Node(new_data)
        new_nod.next=self.head
        self.head=new_nod
        
l=[1,2]

ll=LinkedList(l)
print("before insertion")
ll.printL()
ll.insertF(4590)
print("\n\n\nafter insertion")
ll.printL()


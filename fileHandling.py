# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 13:31:25 2022

@author: arjun

The tell() method returns the current file position in a file stream.


The seek() method sets the current file position in a file stream.



Change the current file position to 4, and return the rest of the line:

f = open("demofile.txt", "r")
f.seek(4)
print(f.readline())


"""
import os
if os.path.exists('1.txt'):
    os.remove('1.txt')
    print("file removed")
else:
    print("file not found")

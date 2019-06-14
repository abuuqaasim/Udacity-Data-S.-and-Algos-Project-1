#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 19 17:27:46 2019

@author: joscelynec
"""

## Locally save and call this file ex.py ##

# Code to demonstrate the use of some of the OS modules in python

import os

# Let us print the files in the directory in which you are running this script
print (os.listdir("."))

# Let us check if this file is indeed a file!
print (os.path.isfile("./ex.py"))

# Does the file end with .py?
print ("./ex.py".endswith(".py"))

print(os.getcwd()) 


print(os.path.isdir("/Users/joscelynec/Desktop/Udacity Data & Algo/testdir"))

print(os.path.isfile("/Users/joscelynec/Desktop/Udacity Data & Algo/testdir"))

print(os.listdir("/Users/joscelynec/Desktop/Udacity Data & Algo/testdir"))

print(os.path.join("/Users//","/Users/joscelynec/Desktop/Udacity Data & Algo/testdir/subtestdir"))
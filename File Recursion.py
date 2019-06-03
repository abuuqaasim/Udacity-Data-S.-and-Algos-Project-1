#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 19 17:24:57 2019

@author: joscelynec
"""
import os


"""
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
       
       
    Use recursion while iterating over list
"""

def find_files(suffix, path):
    # create a list of file and sub directories 
    # names in the given directory 
    if path == None:
        return None
    file_list = []
    dir_list= os.listdir(path)  
    # Iterate over all the entries
    for item in dir_list:
        #build path
        temp_path = os.path.join(path, item)
        #recursion base case
        if os.path.isfile(temp_path) and temp_path.endswith(suffix):
            file_list.append(temp_path)
        #if directory, then concatenate current list with all 
        #to be qualified files then recurse 
        elif os.path.isdir(temp_path):
            file_list+=find_files(suffix,temp_path)
                
    return file_list 

print("****Empty test directory****")        
print(find_files(".c", "/Users/joscelynec/Desktop/Udacity Data & Algo/P1/emptydir/"))
print("****No files ending in .c test no_c_dir****")        
print(find_files(".c", "/Users/joscelynec/Desktop/Udacity Data & Algo/P1/no_c_dir/"))
print("****Single file ending in .c test c_dir****")        
print(find_files(".c", "/Users/joscelynec/Desktop/Udacity Data & Algo/P1/c_dir/"))
print()
print("****Udacity supplied test directory****")        
print(find_files(".c", "/Users/joscelynec/Desktop/Udacity Data & Algo/P1/testdir/"))

               
               
"""
Adapted tutorial on Python's walk function
https://www.pythoncentral.io/how-to-traverse-a-directory-tree-in-python-guide-to-os-walk/
"""

def find_files_walk(suffix, path = None):
    path_list = []
    for dirpath, dirnames, files in os.walk(path):
        for name in files:
            if name.endswith(suffix):
                path_list.append(os.path.join(dirpath, name))
    return path_list




#print(find_files_walk(".c", "/Users/joscelynec/Desktop/Udacity Data & Algo/testdir/"))          
            
"""
**************  End of Program  *****************
""" 
"""
****Empty test directory****
[]
****No files ending in .c test no_c_dir****
[]
****Single file ending in .c test c_dir****
['/Users/joscelynec/Desktop/Udacity Data & Algo/P1/c_dir/t1.c']

****Udacity supplied test directory****
['/Users/joscelynec/Desktop/Udacity Data & Algo/P1/testdir/subdir1/a.c', 
'/Users/joscelynec/Desktop/Udacity Data & Algo/P1/testdir/subdir3/subsubdir1/b.c', 
'/Users/joscelynec/Desktop/Udacity Data & Algo/P1/testdir/subdir5/a.c', 
'/Users/joscelynec/Desktop/Udacity Data & Algo/P1/testdir/t1.c']
"""

  
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 13 01:25:32 2019

@author: joscelynec

Union and Intersection of Two Linked Lists
Your task for this problem is to fill out the union and intersection functions. 
The union of two sets A and B is the set of elements which are in A, in B, 
or in both A and B. The intersection of two sets A and B, denoted by A ∩ B, 
is the set of all objects that are members of both the sets A and B.

You will take in two linked lists and return a linked list that is 
composed of either the union or intersection, respectively. 
Once you have completed the problem you will create your own 
test cases and perform your own run time analysis on the code.
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size



#Use Python Set Union
  
    def Union(self, llist_1, llist_2):
      unions = LinkedList()
       #Return None if both linked lists are empty
      if llist_1.head is None and llist_2.head is None:
        return None
      set_1 = set()
      set_2 = set()
      current_1 = llist_1.head
      while (current_1 is not None):
        set_1.add(current_1.value)
        current_1 = current_1.next
  
      current_2 = llist_2.head 
      while(current_2 is not None):
        set_2.add(current_2.value)
        current_2 = current_2.next
        
        temp= set_1.union(set_2) 
     
  
      for item in temp:
        unions.append(item)
  
      return unions
      
#Use Python Set Intersection
      
    def intersect(self, llist_1, llist_2):
      
      inter_sec = LinkedList()
    #Return an empty linked list if either input linked list is empty
      if llist_1.head is None or llist_2.head is None:
        return None
    #Create two Python Sets, fill each from the two linked lists
    #perform ordinary set intersection and recreate a linked list 
    #to return.
      set_1 = set()
      set_2 = set()
      current_1 = llist_1.head
      while (current_1 is not None):
        set_1.add(current_1.value)
        current_1 = current_1.next
  
        current_2 = llist_2.head 
      while(current_2 is not None):
        set_2.add(current_2.value)
        current_2 = current_2.next
        
        temp= set_1.intersection(set_2) 
        if len(temp) == 0:
            return None
      for item in temp:
        inter_sec.append(item)
  
      return inter_sec
"""
**************  End of Program  *****************
"""    
    
#Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)
print("***Linked Lists Case #1***")
print(linked_list_1)
print(linked_list_2)
print("***Union***")
print (linked_list_1.Union(linked_list_1,linked_list_2))
print("***Intersection***")
print (linked_list_1.intersect(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)
print("***Linked Lists Case #2***")
print(linked_list_3)
print(linked_list_4)
print("***Union***")
print (linked_list_3.Union(linked_list_3,linked_list_4))
print("***Intersection***")
print (linked_list_3.intersect(linked_list_3,linked_list_4))

# Test case 3

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = []
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)
print("***Linked Lists Case #3***")
print("Empty List")
print(linked_list_6)
print("***Union***")
print (linked_list_5.Union(linked_list_5,linked_list_6))
print("***Intersection***")
print (linked_list_5.intersect(linked_list_5,linked_list_6))
"""
***Linked Lists Case #1***
3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 6 -> 4 -> 3 -> 21 -> 
6 -> 32 -> 4 -> 9 -> 6 -> 1 -> 11 -> 21 -> 1 -> 
***Union***
32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 -> 
***Intersection***
4 -> 21 -> 6 -> 
***Linked Lists Case #2***
3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 6 -> 4 -> 3 -> 23 -> 
1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 1 -> 
***Union***
65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 -> 
***Intersection***
None
***Linked Lists Case #3***
Empty List
1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 1 -> 
***Union***
1 -> 21 -> 7 -> 8 -> 9 -> 11 -> 
***Intersection***
None
"""
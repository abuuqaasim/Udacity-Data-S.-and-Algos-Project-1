#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 12 14:12:44 2019

@author: joscelynec

Ideas used below come from: https://medium.com/@krishankantsinghal/my-first-blog-on-medium-583159139237
Used deque from collections for the doubly linked list
"""

from collections import deque
class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.cache = {} #create empty cache using a Python Dictionary
        self.cache_access_history = deque() #deque for doubly linked list
        self.cap = capacity #set initial capacity


    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if self.cap == 0:
          return None
        if key in self.cache.keys():
            temp = self.cache[key]
            del self.cache[key]
            #update last used key in cache history
            self.cache_access_history.appendleft(key) #push most recent key
            if len(self.cache_access_history) > self.cap:
              self.cache_access_history.pop() #delete oldest key from history
            return temp
        else:
            return -1
            
    #code for testing LRU Cache
    def get_history(self):
      if self.cap == 0:
        return None
      return self.cache_access_history 

    def set(self, key, value):
      if self.cap == 0:
          return None
      if  key in self.cache.keys():
        #only need to update last used key in cache history
        self.cache_access_history.appendleft(key) #push most recent key
        if len(self.cache_access_history) > self.cap:
          self.cache_access_history.pop() #delete oldest key from history
        
        
        # Set the value if the key is not present in the cache. 
        #If the cache is at capacity remove the oldest item. 
      elif  key not in self.cache.keys() and len(self.cache)< self.cap:
        self.cache[key] = value #add key, value pair to cache
        #update last used
        self.cache_access_history.appendleft(key)
        if len(self.cache_access_history) > self.cap:
          self.cache_access_history.pop() #delete oldest key from history
            
      elif key not in self.cache.keys() and len(self.cache)==self.cap:
        old = self.cache_access_history.pop() #delete oldest key from history
        self.cache.pop(old) #delete oldest item from cache
        self.cache[key] = value #add key, value pair to cache
        self.cache_access_history.appendleft(key) #update last key used
        if len(self.cache_access_history) > self.cap:
          self.cache_access_history.pop() #delete oldest key from history
               
            
"""
**************  End of Program  *****************
"""            
              
#Test code
print("***Empty Cache Test***")
empty_cache = LRU_Cache(0)
print("Contents of Cache:",empty_cache.cache)
print("Cache History:",empty_cache.get_history())
print("Add (1,1) to Cache")
empty_cache.set(1,1)
print("Contents of Cache:",empty_cache.cache)
print("Get value at key 1:",empty_cache.get(1))
print("Cache History:",empty_cache.get_history())

print("***Cache with Capacity 1 Test***")
one_cache = LRU_Cache(1)
print("Contents of Cache:",one_cache.cache)
print("Cache History:",one_cache.get_history())
print("Add (1,1) to Cache")
one_cache.set(1,1)
print("Contents of Cache:",one_cache.cache)
print("Get value at key 1:",one_cache.get(1))
print("Cache History:",one_cache.get_history())
one_cache.set(2,2)
print("Contents of Cache:",one_cache.cache)
print("Get value at key 1:",one_cache.get(1))
print("Cache History:",one_cache.get_history())
print("Get value at key 2:",one_cache.get(2))
print("Cache History:",one_cache.get_history())

print("***Cache with Capacity 4 Test***")
four_cache = LRU_Cache(4)
print("Contents of Cache:",four_cache.cache)
print("Cache History:",four_cache.get_history())
print("Add (1,1) to Cache")
print("Add (2,2) to Cache")
print("Add (3,4) to Cache")
print("Add (4,4) to Cache")
four_cache.set(1,1)
four_cache.set(2,2)
four_cache.set(3,3)
four_cache.set(4,4)
print("Contents of Cache:",four_cache.cache)
print("Cache History:",four_cache.get_history())
print("Add (5,5) to Cache")
four_cache.set(5,5)
print("Contents of Cache:",four_cache.cache)
print("Cache History:",four_cache.get_history())
print("Add (7,7) to Cache")
four_cache.set(7,7)
print("Contents of Cache:",four_cache.cache)
print("Cache History:",four_cache.get_history())
print("Get value at key 3:",four_cache.get(3))
print("Contents of Cache:",four_cache.cache)
print("Cache History:",four_cache.get_history())
print("Add (2,2) to Cache")
four_cache.set(2,2)
print("Contents of Cache:",four_cache.cache)
print("Cache History:",four_cache.get_history())
print("Add (5,5) to Cache")
four_cache.set(5,5)
print("Contents of Cache:",four_cache.cache)
print("Cache History:",four_cache.get_history())
print("Get value at key 6:",four_cache.get(6))
print("Contents of Cache:",four_cache.cache)
print("Cache History:",four_cache.get_history())
print("Add (6,6) to Cache")
four_cache.set(6,6)
print("Contents of Cache:",four_cache.cache)
print("Cache History:",four_cache.get_history())
print("Get value at key 2:",four_cache.get(2))
print("Contents of Cache:",four_cache.cache)
print("Cache History:",four_cache.get_history())
print("Get value at key 5:",four_cache.get(5))
print("Contents of Cache:",four_cache.cache)
print("Cache History:",four_cache.get_history())
print("Get value at key 1:",four_cache.get(1))
print("Contents of Cache:",four_cache.cache)
print("Cache History:",four_cache.get_history())

"""
***Empty Cache Test***
Contents of Cache: {}
Cache History: None
Add (1,1) to Cache
Contents of Cache: {}
Get value at key 1: None
Cache History: None
***Cache with Capacity 1 Test***
Contents of Cache: {}
Cache History: deque([])
Add (1,1) to Cache
Contents of Cache: {1: 1}
Get value at key 1: 1
Cache History: deque([1])
Contents of Cache: {2: 2}
Get value at key 1: -1
Cache History: deque([2])
Get value at key 2: 2
Cache History: deque([2])
***Cache with Capacity 4 Test***
Contents of Cache: {}
Cache History: deque([])
Add (1,1) to Cache
Add (2,2) to Cache
Add (3,4) to Cache
Add (4,4) to Cache
Contents of Cache: {1: 1, 2: 2, 3: 3, 4: 4}
Cache History: deque([4, 3, 2, 1])
Add (5,5) to Cache
Contents of Cache: {2: 2, 3: 3, 4: 4, 5: 5}
Cache History: deque([5, 4, 3, 2])
Add (7,7) to Cache
Contents of Cache: {3: 3, 4: 4, 5: 5, 7: 7}
Cache History: deque([7, 5, 4, 3])
Get value at key 3: 3
Contents of Cache: {4: 4, 5: 5, 7: 7}
Cache History: deque([3, 7, 5, 4])
Add (2,2) to Cache
Contents of Cache: {4: 4, 5: 5, 7: 7, 2: 2}
Cache History: deque([2, 3, 7, 5])
Add (5,5) to Cache
Contents of Cache: {4: 4, 5: 5, 7: 7, 2: 2}
Cache History: deque([5, 2, 3, 7])
Get value at key 6: -1
Contents of Cache: {4: 4, 5: 5, 7: 7, 2: 2}
Cache History: deque([5, 2, 3, 7])
Add (6,6) to Cache
Contents of Cache: {4: 4, 5: 5, 2: 2, 6: 6}
Cache History: deque([6, 5, 2, 3])
Get value at key 2: 2
Contents of Cache: {4: 4, 5: 5, 6: 6}
Cache History: deque([2, 6, 5, 2])
Get value at key 5: 5
Contents of Cache: {4: 4, 6: 6}
Cache History: deque([5, 2, 6, 5])
Get value at key 1: -1
Contents of Cache: {4: 4, 6: 6}
Cache History: deque([5, 2, 6, 5])
"""




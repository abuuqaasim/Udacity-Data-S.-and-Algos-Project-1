#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 17 17:05:22 2019

@author: joscelynec
"""


import hashlib
import datetime 
utc = datetime.datetime.utcnow()
"""
Udacity supplied stub code
"""
def calc_hash(data):
    sha = hashlib.sha256()
    hash_str = data.encode('utf-8')
    sha.update(hash_str)
    return sha.hexdigest()

"""
Expanded Node class
""" 

class Block:

    def __init__(self, data, previous_hash):

      utc = datetime.datetime.utcnow()

      self.timestamp = utc

      self.data = data

      self.previous_hash = previous_hash

      self.previous_block = None

      self.hash = calc_hash(str(data))
    
    #to String method for testing
    def __str__(self):
        

        return str(self.timestamp)+" "+str(self.data)+" "+str( self.previous_hash)+" "+str( self.hash)
"""
BlockChain class
"""

class BlockChain:

    def __init__(self):

        self.head = None


    def append(self, data,previous_hash):

        #Append a block to the end of the chain

     
        if self.head is None:

          self.head = Block(data,0)

          return

        new_head = Block(data,self.head.hash)

        new_head.previous_block = self.head

      
        self.head = new_head
       
    def size(self):
    #return the number of blocks in the chain

      size = 0

      block = self.head

      while block:
          size += 1
          block = block.previous_block
      return size


    def to_list(self):
    #return a list of blocks

      out = []

      block = self.head

      while block:

        out.append(block)

        block = block.previous_block

      return out
  
"""
**************  End of Program  *****************
"""    


#Testing code
"""
Test Case 1
"""
print("Test Case 1 Empty BlockChain")
A = BlockChain()
print("size",A.size())
print(A.head)
print()


"""
Test Case 2
"""
print("Test Case 2 One item BlockChain")
B = BlockChain()
B.append("Genesis",0)
print("size",B.size())
for item in B.to_list():
    print(item)
print()

"""
Test Case 3
"""
print("Test Case 3 Two item BlockChain")
C = BlockChain()
C.append("Genesis",0)
C.append("Exodus",calc_hash("Genesis"))


print("size",C.size())
for item in C.to_list():
    print(item)

print()
"""
Test Case 4
"""
print("Test Case 4 Five item BlockChain")
D = BlockChain()
D.append("Genesis",0)
D.append("Exodus",calc_hash("Genesis"))
D.append("Leviticus",calc_hash("Exodus"))
D.append("Numbers",calc_hash("Leviticus"))
D.append("Deuteronomy",calc_hash("Numbers"))

print("size",D.size())
for item in D.to_list():
    print(item)
"""  
Test Case 1 Empty BlockChain
size 0
None

Test Case 2 One item BlockChain
size 1
2019-05-28 21:09:56.996735 Genesis 0 81ddc8d248b2dccdd3fdd5e84f0cad62b08f2d10b57f9a831c13451e5c5c80a5

Test Case 3 Two item BlockChain
size 2
2019-05-28 21:09:56.998314 Exodus 81ddc8d248b2dccdd3fdd5e84f0cad62b08f2d10b57f9a831c13451e5c5c80a5 8bcdca3051ab63ed9da538d764b009269b47622a3499960d2eb04ec43c2bd546
2019-05-28 21:09:56.998243 Genesis 0 81ddc8d248b2dccdd3fdd5e84f0cad62b08f2d10b57f9a831c13451e5c5c80a5

Test Case 4 Five item BlockChain
size 5
2019-05-28 21:09:56.999291 Deuteronomy b0640f0fc46040e7139bbbc43e0a75dc914c6cab74f344cee2c597f1d6b476df 5d82330b0c002054b66ec4317fc305eb62310d7c88b8902490513d8634ed2a57
2019-05-28 21:09:56.999283 Numbers 8fbea01a5a9b8e474b6871523aaf0c63451858c694da7f8f6aa5751a8e055bdc b0640f0fc46040e7139bbbc43e0a75dc914c6cab74f344cee2c597f1d6b476df
2019-05-28 21:09:56.999274 Leviticus 8bcdca3051ab63ed9da538d764b009269b47622a3499960d2eb04ec43c2bd546 8fbea01a5a9b8e474b6871523aaf0c63451858c694da7f8f6aa5751a8e055bdc
2019-05-28 21:09:56.999264 Exodus 81ddc8d248b2dccdd3fdd5e84f0cad62b08f2d10b57f9a831c13451e5c5c80a5 8bcdca3051ab63ed9da538d764b009269b47622a3499960d2eb04ec43c2bd546
2019-05-28 21:09:56.999200 Genesis 0 81ddc8d248b2dccdd3fdd5e84f0cad62b08f2d10b57f9a831c13451e5c5c80a5
"""
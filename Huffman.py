#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 15:24:16 2019

@author: joscelynec
"""

import sys

import heapq
"""
Adapted from Tree Node class, each Node contains a value and an additional weight = wt, 
along with the usual links right/left.
"""
class Huff_Node:
    def __init__(self,value, wt):
        """Create node for given symbol and probability."""
        self.left = None
        self.right = None
        self.value = value
        self.wt = wt        
        
    #Python method redefined to compare two Huff_Nodes
    def __lt__(self, other):
        return self.wt < other.wt
    
    #return a string version of Huff_Node, used for testing
    def __str__(self):
        return str(self.value)+" "+str(self.wt)
    
"""
Return ascending list of Huff Nodes
"""
def get_frequecies(data):
  freq = {}
  #build a dictionary of frequencies
  for item in data:
    if item not in freq:
      freq[item] = 1
    else:
      freq[item] +=1
  #create a sorted list key, freq tuple pairs
  freq_sorted = sorted(zip(freq.values(), freq.keys()))
  #print(freq_sorted) test code
  #in place replace sorted tuples by Huff_N\odes
  for i in range(len(freq_sorted)):
     value = freq_sorted[i][1] #second item is value
     freq = freq_sorted[i][0] #first item is frequency
     
     freq_sorted[i] = Huff_Node(value, freq)
      
  return freq_sorted  


"""
Huffman Algorithm
Adapted from
https://riptutorial.com/algorithm/example/23995/huffman-coding
Procedure Huffman(C):     // C is the set of n characters and related information
n = C.size
Q = priority_queue()
for i = 1 to n
    n = node(C[i])
    Q.push(n)
end for
while Q.size() is not equal to 1
    Z = new node()
    Z.left = x = Q.pop
    Z.right = y = Q.pop
    Z.frequency = x.frequency + y.frequency
    Q.push(Z)
end while
Return Q
"""     
def huffman_tree(data):
    heap = get_frequecies(data)#get sorted list of Huff Nodes
    heapq.heapify(heap)#Create heap
    while len(heap) != 1:
        Z = Huff_Node(None,None)
        lft = heapq.heappop(heap)
        Z.left  = lft
        rgt = heapq.heappop(heap)
        Z.right  = rgt
        Z.wt = lft.wt + rgt.wt
        heapq.heappush(heap, Z)
    return heap #a list containing the root node of the heap

"""
Recursive helper function to create a code table
Adapted from CMU 15-112: Fundamentals of Programming and Computer Science
Class Notes: Data Compression with Huffman Encoding
"""
def create_Huffcode_table(root):
    code = {}
    # a left edge represents a 0 bit, a right edge represents a 1 bit
    #traverse the Huff Tree to build the code table
    def getCode(hNode, currentCode=""):
        if (hNode == None): 
            return
        if (hNode.left == None and hNode.right == None):
            code[hNode.value] = currentCode
        getCode(hNode.left, currentCode + "0")
        getCode(hNode.right, currentCode + "1")
    getCode(root[0])
    return code

"""
Helper fucntion to return a Huffman endoded string of 0s and 1s
"""
def huff_encode(data):
   
    if(len(get_frequecies(data))) == 1:
      return "0"*len(data)
    huff_code = "" 
    root = huffman_tree(data)#heap/list containing the Huffman root node
    table = create_Huffcode_table(root)#Huffman code dictionary
    for item in data:
       huff_code += table[item]
    return huff_code
"""
Key Huffman Decoding Algorithm, adapted from
https://riptutorial.com/algorithm/example/23995/huffman-coding
Procedure HuffmanDecompression(root, S):   // root represents the root of Huffman Tree
n := S.length                              // S refers to bit-stream to be decompressed
for i := 1 to n
    current = root
    while current.left != NULL and current.right != NULL
        if S[i] is equal to '0'
            current := current.left
        else
            current := current.right
        endif
        i := i+1
    endwhile
    print current.symbol
endfor
"""    
    
def huffman_decode(bit_string,root):#bit string and root a heap containg the Huffman Tree Root
    
    if(len(get_frequecies(bit_string))) == 1:
      return len(bit_string)*str(root.value)
    decode = ""
    n = len(bit_string)
    count = 0
    while count < n:
        current = root[0]
        while current.left != None and current.right != None:
            if bit_string[count] == "0":
                current = current.left
            else:
                current = current.right
            count+=1
        decode+=current.value
    return decode

#returns encoded data and root of huffman tree
def huffman_encoding(data):
  
  return huff_encode(data), huffman_tree(data)
  
#returns decoded Huffman code
def huffman_decoding(data,tree):
 
  return huffman_decode(data,tree)

"""
Test harnesss code, special cases are for data =: None, "", and single frequency data
eg. "a", "aa", "aaa", etc.
"""
def test_Huffman(data):
  if data == None:
    print("***************************************************************")
    print(None)
  elif data == "":
    print("***************************************************************")
    print("Empty String")
  #single frequency data
  
  elif len(get_frequecies(data)) == 1:
    print("***************************************************************")
    code = "0"*len(data)
    print ("The size of the data is: {}\n".format(sys.getsizeof(data)))
    print ("The content of the data is: {}\n".format(data))
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(code, base=2))))
    print ("The content of the encoded data is: {}\n".format(code))
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(data)))
  else:
    print("***************************************************************")
    print ("The size of the data is: {}\n".format(sys.getsizeof(data)))
    print ("The content of the data is: {}\n".format(data))
    encoded_data, tree = huffman_encoding(data)
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    decoded_data = huffman_decoding(encoded_data, tree)
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))


test_Huffman(None)
test_Huffman("")
test_Huffman("a")
test_Huffman("aa")
test_Huffman("aaa")
test_Huffman("aaaa")
test_Huffman("ab")
test_Huffman("abbb")
test_Huffman("abc")
test_Huffman("udacity")
test_Huffman("huffman")
test_Huffman("mississipi")
test_Huffman("The bird is the word")
test_Huffman("""When in the course of human events it becomes necessary 
for one people to dissolve the political bands which have connected
them with another and to assume among the powers of the earth, 
the separate and equal station to which the Laws of Nature and 
of Nature's God entitle them, a decent respect to the opinions 
of mankind requires that they should declare the causes which impel 
them to the separation.""")

"""
***************************************************************
None
***************************************************************
Empty String
***************************************************************
The size of the data is: 58

The content of the data is: a

The size of the encoded data is: 24

The content of the encoded data is: 0

The size of the decoded data is: 58

***************************************************************
The size of the data is: 51

The content of the data is: aa

The size of the encoded data is: 24

The content of the encoded data is: 00

The size of the decoded data is: 51

***************************************************************
The size of the data is: 52

The content of the data is: aaa

The size of the encoded data is: 24

The content of the encoded data is: 000

The size of the decoded data is: 52

***************************************************************
The size of the data is: 53

The content of the data is: aaaa

The size of the encoded data is: 24

The content of the encoded data is: 0000

The size of the decoded data is: 53

***************************************************************
The size of the data is: 51

The content of the data is: ab

The size of the encoded data is: 28

The content of the encoded data is: 10

The size of the decoded data is: 51

The content of the encoded data is: ab

***************************************************************
The size of the data is: 53

The content of the data is: abbb

The size of the encoded data is: 28

The content of the encoded data is: 0111

The size of the decoded data is: 53

The content of the encoded data is: abbb

***************************************************************
The size of the data is: 52

The content of the data is: abc

The size of the encoded data is: 28

The content of the encoded data is: 01110

The size of the decoded data is: 52

The content of the encoded data is: abc

***************************************************************
The size of the data is: 56

The content of the data is: udacity

The size of the encoded data is: 28

The content of the encoded data is: 10001110100111110010

The size of the decoded data is: 56

The content of the encoded data is: udacity

***************************************************************
The size of the data is: 56

The content of the data is: huffman

The size of the encoded data is: 28

The content of the encoded data is: 001100101100101111

The size of the decoded data is: 56

The content of the encoded data is: huffman

***************************************************************
The size of the data is: 59

The content of the data is: mississipi

The size of the encoded data is: 28

The content of the encoded data is: 101110011001110011

The size of the decoded data is: 59

The content of the encoded data is: mississipi

***************************************************************
The size of the data is: 69

The content of the data is: The bird is the word

The size of the encoded data is: 36

The content of the encoded data is: 0000001111011010101111011010110111110111100001001111011010001001011010

The size of the decoded data is: 69

The content of the encoded data is: The bird is the word

***************************************************************
The size of the data is: 458

The content of the data is: When in the course of human events it becomes necessary 
for one people to dissolve the political bands which have connected
them with another and to assume among the powers of the earth, 
the separate and equal station to which the Laws of Nature and 
of Nature's God entitle them, a decent respect to the opinions 
of mankind requires that they should declare the causes which impel 
them to the separation.

The size of the encoded data is: 252

The content of the encoded data is: 11001011010100110101111110100101111000101001111110001101111011011000010001111110110011011111010110110001001001010111101111001000110101000010011111010000111110011000111000110110010001101001110101011100010110100010010011100011001110111100000001101101111000111101101010111111101110111011110111001010111110001011111001111101001000100101100101110010001111100010100111111101111011001011101000011010100011001001011111100110010010101001110100111100001101011010100011010111101010011100100011111100011011010101010111000100001100111100000000101001100100111100001110100001010111100101011011000101001111000111100101010011111100010111111001010001001101100010001111110010010010110101110010101111000101001111111011110111000010111100001001111011001101111000101001111101110011100000010100011000111100000000101001111101000111101111001110001001000011111100101010011111101111001111110110100100101111010000010010001101010110101111000101111110000110101101010001101011100010100111110011001010011000010100111101100110111111001101100100011011011000011111100101010011111110000010110011011111100110110010001101101100001111001010001001110011001111011001111110110101000110100000010101111100010100110010000110001111001111001110111000101101010001111100001101001101110111000100011100010111110001010011111101111011111010010111010101101010100111100000101100110111100100100101010011001101101001010011111111000011110011111101101101011000011010011100010101001000111000101001111001110111010010101011110110001010011111100111011100010010110011100001111100010100111111000110011101100100011010011110000110101101010001101011111010001001101110110010111110000000010100110010011100010111110001010011111010001111011110011100010010001101010110101110010111

The size of the decoded data is: 458

The content of the encoded data is: When in the course of human events it becomes necessary 
for one people to dissolve the political bands which have connected
them with another and to assume among the powers of the earth, 
the separate and equal station to which the Laws of Nature and 
of Nature's God entitle them, a decent respect to the opinions 
of mankind requires that they should declare the causes which impel 
them to the separation.
"""
## Huffman Coding

A Huffman code is a type of optimal prefix code that is used for compressing data. The Huffman encoding and decoding schema is also lossless, meaning that when compressing the data to make it smaller, there is no loss of information.

The Huffman algorithm works by assigning codes that correspond to the relative frequency of each character for each character. The Huffman code can be of any length and does not require a prefix; therefore, this binary code can be visualized on a binary tree with each encoded character being stored in the leaves.

As, little background was supplied in the Udacity Huffman Coding Project, I followed the classical algorithm(s) for Huffman Coding. References are supplied in the code where needed. The idea I used was to use a priority queue using Python’s `heapq` module to build the Huffman Tree. This seemed to be the idea overwhelming suggested in the literature I read. This also reduced the amount of code needed. 

The time complexity of the Huffman algorithm is `O(nlogn)`. By using a heap to store the weight of each tree, each iteration requires `O(log n)` time to place in the priority queue, and there are `O(n)` iterations, one for each item. The space complexity in building the Huffman Tree is `O(#of distinct symbols in the data)`. 

For testing, a test function harness is defined, which examines the input data to filter out the edge cases: None, empty string, and single frequency strings -> “a”, “aa”, “aaa”, etc. Single frequency strings are directly translated into “0”, “00”, “000” since the full strength of the Huffman Coding is not required for these single frequency entries.
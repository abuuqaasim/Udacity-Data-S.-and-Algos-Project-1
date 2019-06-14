## Union and Intersection of Two Linked Lists

The task for this problem is to fill out the union and intersection functions. The union of two sets A and B is the set of elements which are in A, in B, or in both A and B. The intersection of two sets A and B, denoted by A ∩ B, is the set of all objects that are members of both the sets A and B.

Input: two linked lists are and return a linked list that is composed of either the union or intersection, respectively.

Both intersection and union functions use Python’s set collection. These provide both reliable and efficient means to compute set union and set intersection. The idea for both functions is to traverse the linked the lists filling two sets. Python’s union and intersections methods are then used. A linked list is regenerated and returned in each case. The time and space complexity is `O(max length of the two linked lists)`.






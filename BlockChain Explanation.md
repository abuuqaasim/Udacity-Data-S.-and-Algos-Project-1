## Blockchain
A Blockchain is a sequential chain of records, similar to a linked list. Each block contains some information and how it is connected related to the other blocks in the chain. Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data. For our blockchain we will be using a `SHA-256` hash, the Greenwich Mean Time when the block was created, and text strings as the data.

Blockchain uses an extended node class, which stores: a real-time timestamp, a data field, a previous hash code, a reference to the previous block, and a `SHA-256` hash code of the data field. These are the required fields to full fill the 

Block methods implemented are:

 `def __str__(self):` for testing

Aside from the constructor, the class BlockChain implements: `append()`, `size()`, and `to _list()` methods. These were adapted from Udacity’s LinkList class, as the project noted a  BlockChain is similar to a linked list. These seemed like the minimal methods needed to build a basic BlockChain. The time and space complexities are `O(n)` for `size()` and `to_list()`, while `append()` is `O(1)`.




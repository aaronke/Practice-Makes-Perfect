# Easy Issues

## [Power of Two](https://leetcode.com/problems/power-of-two/)  
### Description
Given an integer, write a function to determine if it is a power of two.
### Python Code
~~~python
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        while (n%2 == 0) and (n > 0):
            n = n/2
            if n == 1:
                return True
        return False
~~~

## 2. [Delete Node in a Linked List ](https://leetcode.com/problems/delete-node-in-a-linked-list/)  
### Description
Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Supposed the linked list is `1 -> 2 -> 3 -> 4` and you are given the third node with value 3, the linked list should become `1 -> 2 -> 4` after calling your function.
### Python Code
~~~python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node.next:
            node.val = node.next.val
            node.next = node.next.next
~~~



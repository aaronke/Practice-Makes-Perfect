# [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)

## Description
Given a singly linked list, determine if it is a palindrome.
**Follow up:** Could you do it in O(n) time and O(1) space?
## Analysis
Method 1 -- Convert into list and compare reversed list:
This method is the simple. The only thing should be careful is that `list` method should be added after `reversed(list)`. And also for None input, the default should return `True` (Need to clarify when interviewing).

* Time complexity: `O(n)` 
* Space complexity: `O(n)`

Method 2 -- To be Updated

## Python Code
~~~Python
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
import copy
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if (head == None) or (head.next == None):
            return True
        value = []
        while head:
            value.append(head.val)
            head =  head.next
        reverseValue = list(reversed(value))
        if value == reverseValue:
            return True
        return False
~~~
## Notes
1. How to get reversed the list  
[StackOverflow 1](http://stackoverflow.com/questions/7286365/print-a-list-in-reverse-order-with-range-in-python)  
[StackOverflow 2](http://stackoverflow.com/questions/3940128/how-can-i-reverse-a-list-in-python)
2. When should we use deepcopy and how? -- [Offical Docs](https://docs.python.org/2/library/copy.html)


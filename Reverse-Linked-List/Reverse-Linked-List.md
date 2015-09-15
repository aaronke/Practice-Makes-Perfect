# [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)
## Description
Reverse a singly linked list.
## Analysis
Basically, the most efficient method is to swich the connect between two nodes by one searching.

* Time complexity: `O(n)`
* Space complexity: `O(1)`

## Python Code
~~~python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Method 1 -- naive beat 26%
        # if head == None or head.next == None:
        #     return head
            
        # nextNode = None
        # while head.next:
        #     temp = head.next
        #     head.next = nextNode
        #     nextNode = head
        #     head = temp
            
        # #Last Node update
        # head.next = nextNode
        # return head 
        
        # Method 2 -- naive beat 53%
        # nextNode = None
        # while head:
        #     temp =  head.next
        #     head.next =  nextNode
        #     if temp == None:
        #         return head
        #     nextNode = head
        #     head = temp
        
        # Method 3 -- beat 86%
        pre = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre
~~~
## Notes
1. Try to incorporate the specail input into the while loop. It will save a lot of time when it comes to running test cases.
2. You could see the three methods which are refined step by step. Method 3 is very smart that taking advantage of two variables -- `pre` and `cur` and return `pre` as the results 
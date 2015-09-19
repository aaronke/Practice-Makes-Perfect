# [Remove Linked List Elements](https://leetcode.com/problems/remove-linked-list-elements/)

## Description
Remove all elements from a linked list of integers that have value val.

Example
Given: `1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6`, val = 6  
Return: `1 --> 2 --> 3 --> 4 --> 5`
## Analysis
Yes, it is easy problem by logic. However, it is still deserved to be careful! Firstly, think about creating a fake head node. Then think about previous node(`pre`), really understand when `pre` should be updated -- Only when checking the non-val node.

* Time Complexity: `O(n)`
* Space Complexity: `O(n)`

## Python Code
~~~
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        pre = ListNode(0)
        pre.next = head
        rs = pre
        while head:
            if head.val == val:
                # Be careful and change pre only when coming across non-val node
                pre.next = head.next
            else:
                pre = pre.next
            head = head.next
        return rs.next
        # if head == None:
        #     return None
        # if head.val == val:
        #     return self.removeElements(head.next, val)
        # else:
        #     head.next = self.removeElements(head.next, val)
        #     return head
~~~
## Test Cases
~~~
1. []       -> []
2. [1,1], 1 -> []
2. [1,2,1],1  -> [2]
3. [1,1,1,1,2], 2 -> [1,1,1,1]
4. [1,2,2], 1 -> [2,2]
~~~
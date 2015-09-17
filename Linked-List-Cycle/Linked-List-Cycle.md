# [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)

## Description
Given a linked list, determine if it has a cycle in it.

Follow up:Can you solve it without using extra space?
## Analysis
Method 1 -- Apply Hashtable to remember the visted Node. 

* Time Complexity -- `O(n)`
* Space Complexity -- `O(n)`

Method 2 -- Create a node which is used as the next node for those nodes that has been visited. But it still uses `O(1)` extra space.

* Time Complexity -- `O(n)`
* Space Complexity -- `O(1)`

Method 3 -- Imagine two people are running on a trail with different speeds, if it is circle, they must come across with each other at some points. So we use two pointers to move with different speeds. If they are at same node, it has circle and returns `True`.

* Time Complexity -- `O(n)`
* Space Complexity -- `O(0)`


## Python Code

## Notes


~~~
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Naive Method - hashtable --O(n) space
        # nodesMap = {}
        # # nodesMap = [] # Use List and get TLE
        # while head:
        #     if head not in nodesMap:
        #         nodesMap[head] = 1
        #         # nodesMap.append(head)
        #         head = head.next
        #     else:
        #         return True
        # return False
        
        # Visit a node then make it point to a designated node -- O(1) Space Method
        # visitedNode = ListNode(0)
        # while head:
        #     if head.next ==  visitedNode:
        #         return True
        #     else:
        #         temp = head.next
        #         head.next = visitedNode
        #         head = temp
        # return False
        
        # Method 3 -- Two pointers -- Without extra space and smart method
        
        fast, slow =  head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if (fast == slow):
                return True
        
        return False
~~~
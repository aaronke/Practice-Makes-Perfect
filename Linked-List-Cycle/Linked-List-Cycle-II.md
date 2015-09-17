# [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)

## Description
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up: Can you solve it without using extra space?
## Analysis
Those two methods share the same core idea with the solutions in [`Linked List Cycle I`](https://github.com/haoyuchen1992/Practice-Makes-Perfect/blob/master/Linked-List-Cycle/Linked-List-Cycle.md) . 

There are serveral differences. Firstly, it is not allowed to modify the list. Therefore, Method 2 in `Linked List Cycle I` is not validated. Secondly, it asks to return the start node in the circle. In hashtable solution, obviously, it is the first revisited node. 

However, for the two pointer method, it is not the node when two pointed nodes are equal. The equaled node could only depend on the length of circle. But there is simple math there. You can draw a graph below. So `(k1+k2) = (k2 + k3)` so `k3 = k1`. The equaled node is `C`. We need to move `k1` step to get B, which is the beginning node of circle. Therefore, we could use another two pointers(`A` node and `C` Node) to loop `k1` steps to get B and stop until A and B get the same node.
![Linked Circle Node Image](https://github.com/haoyuchen1992/Practice-Makes-Perfect/blob/master/Resources/node-circle.jpg)
## Python Code
~~~python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Method 1 -- HashMap
        # nodesMap = {}
        # while head:
        #     if head not in nodesMap:
        #         nodesMap[head] = 1
        #         head = head.next
        #     else:
        #         return head
        # return None
        
        # Method 2 -- Two Pointer -- Withou extra storage
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                while head and slow:
                    if head == slow:
                        return slow
                    head = head.next
                    slow = slow.next
        
        return None
~~~
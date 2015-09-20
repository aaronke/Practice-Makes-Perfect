# [Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)

## Description
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given `1->1->2`, return `1->2`.
Given `1->1->2->3->3`, return `1->2->3`.
## Analysis
Again, it is easy one, but still also easy to make mistake. 

1. Don't update head when deleting node. 

~~~
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
~~~
2. When check if head.next is `None` or not, please check head first. Otherwise, it will give error when head is `None`.
~~~
		 # Wrong: while head.next:
        while head and head.next:
~~~

And also it can use recursion to implement it easily. It is a problem where `Solution(n) = Solution (n-1) + O(1)`. See Method 2 below.

* Time Complexity: `O(n)`
* Space Complexity: `O(1)`

## Python Code
~~~
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        rs = head
        while head and head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        return rs
        # # Method 2 -- Recursion
        # if head == None or head.next == None:
        #     return head
        # newHead = self.deleteDuplicates(head.next)
        # head.next = newHead
        # return newHead if head.val == newHead.val else head
~~~
## Test Cases
~~~
1. None -> None
2. 1 -> 1
3. 1-2-2-3 -> 1-2-3
4. 2-2-3-3 -> 2-3
4. 1-1-1 -> 1
~~~
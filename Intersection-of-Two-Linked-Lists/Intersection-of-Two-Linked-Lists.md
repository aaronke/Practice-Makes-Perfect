# [Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/)

## Description
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

~~~
A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
~~~
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return `null`.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in `O(n)` time and use only `O(1)` memory.

## Analysis
**Method 1** Use hashTable to index list A and then loop the nodes in list B from head. If find a node is already in hashTable, then return it. HashTable is realy fast and beat 99% of solutions.

* Time Complexity: `O(n)`
* Space Complexity: `O(n)`

**Method 2** In order to use constant space. The first thing in my mind for the list problem is two-pointers. How can I run two pointers? Then I found the intersection couldn't happen within the beginning part for the longer list(offset). After that, we could check the nodes in pair respectively from list A and list B. 

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
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # mapNodes = {}
        
        # while headA:
        #     if headA not in mapNodes:
        #         mapNodes[headA] = 1
        #         headA = headA.next
        
        # while headB:
        #     if headB in mapNodes:
        #         return headB
        #     headB = headB.next
        
        # return None
        
        pointA = headA
        pointB = headB
        lenA = self.getListLen(pointA)
        lenB = self.getListLen(pointB)
            
        if lenA > lenB:
            offSet = lenA - lenB
            headA = self.getNewHead(offSet, headA)
        else:
            offSet = lenB - lenA
            headB = self.getNewHead(offSet, headB)
        
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        
        return None

    def getListLen(self, head):
            lenList = 0
            while head:
                lenList += 1
                head = head.next
            return lenList
    def getNewHead(self, offSet, head):
            count = 0
            while count < offSet:
                if head == None:
                    return None
                count += 1
                head = head.next

            return head
~~~

## Test Cases
~~~
1. None -> None
2. List A: 1-2-3-4
   List B: 6-2-3-4    -> 2
3. List A: 1-2-3-4
   List B: 6-5-5-4    -> 4
4. List A: 1-2-3-4-5-6
   List B: 6          -> 6     
~~~   

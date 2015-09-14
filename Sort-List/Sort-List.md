# [Sort List](https://leetcode.com/problems/sort-list/)

## Description
Sort a linked list in O(n log n) time using constant space complexity.
## Analysis
Honestly, I didn't figure out the problem at the beginning. So please spend more time on it! Because it is VERY IMPORTATN! 

**Method 1 --** It is to take advantage of sorting methd in python. It costs more than `O(1)` space, but `O(n)`. But the running time is very impressive(beat 99% of the rest) and the code is very simple. So it is still deserved to mentioned.

**Method 2--** Considering about multiple solutions online, here are the useful links.
1.https://leetcode.com/discuss/9731/merge-sort-solution-in-java  
2. http://fisherlei.blogspot.com/2013/12/leetcode-sort-list-solution.html  
3. http://fmarss.blogspot.com/2014/08/leetcode-solution-sort-list.html  
Since they are kind of long, I will save them to next day!! To be updated!

## Python Code
~~~python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Method 1 -- Naive method with sorting from python (beats 99%)
        # if head == None:
        #     return head
        
        # listNode = []
        # while head:
        #     listNode.append(head)
        #     head = head.next
        # listNode = sorted(listNode, key=lambda node: node.val)
        # for i in range(len(listNode)-1):
        #     listNode[i].next = listNode[i+1]
        
        # # Don't forget the ending None!!
        # listNode[len(listNode)-1].next = None
        # return listNode[0]
        
        # Method 2 -- To be updated!
        
~~~
## Notes

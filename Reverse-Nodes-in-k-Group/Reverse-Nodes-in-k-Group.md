# [Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/)

## Description
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: `1->2->3->4->5`

For `k = 2`, you should return: `2->1->4->3->5`

For `k = 3`, you should return: 3`->2->1->4->5`

## Analysis
### Clarifications
1. What kind of linked node? Single Linked or double linked?
2. Run a example -- When `k=4`, the input linked list is `1-2-3-4-5-6`, is  `4-3-2-1-5-6` correct return linked list?
3. What do you mean by nodes itself may be changed? Does it mean that node value can't be changed but node's next node could be changed?

### Method
Firstly, we could think of using two pointer to find the sublists that need to be reversed and then reversed it in a method. When it comes to reverse a sublist, we need four inputs: `lastEnd`, `start`, `endNode`, and `nextStart`. So how can we iterate and get four nodes for each sub-list?  Just count it when going thourgh the whole list. 

* Time Complexity: `O(n)`
* Space Complexity: `O(1)`

### Be careful in implementations!!!
1. when you reverse one sublist, be clear about what's your four node-- it changes!!! Therefore, we can't always get the new `head` by `head = head.next`

~~~
			 # Wrong Code
		    if count == k:
		        end = head
		        nextStart = head.next
		        self.reverseList(preEnd, start, end, nextStart)
		        preEnd = start
		        start = nextStart
		        count = 0
		    head = head.next
~~~
~~~ 
		    # Correct Code
		    if count == k:
		        end = head
		        nextStart = head.next
		        self.reverseList(preEnd, start, end, nextStart)
		        preEnd = start
		        start = nextStart
		        count = 0
		        head = nextStart
		    else:
		        head = head.next
~~~

2. The design of the while loop is also very critical. The mistake I made is to set the conditional statement of while as `start != nextStart`. Why wrong? Because nextStart is always change!!. I also tried to change it as `start != end`, why it doesn't work? `end` doesn't change next!!It's a big miss! So take advantage of varible --`stop` to remember `nextStart`at the very beginning!!

~~~
    def reverseList(self, preEnd, start, end, nextStart):
        # How to set the stop --Key point
        stop = nextStart
        while start != stop:
            temp = start.next
            start.next = nextStart
            nextStart = start
            start = temp
        preEnd.next = end
~~~

## Python Code
~~~Python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        if k == 0 or k == 1:
            return head
        count = 0
        preEnd = ListNode(0)
        preEnd.next = head
        rsNode = preEnd
        start = head
        while head:
		    count += 1
		    if count == k:
		        # Don't use original head, head.next into reverseList
		      end = head
		      nextStart = head.next
		      #  self.reverseList(preEnd, start, end, nextStart)
		        preEnd = start
		        start = nextStart
		        count = 0
		        head = nextStart
		    else:
		        head = head.next
        return rsNode.next
    def reverseList(self, preEnd, start, end, nextStart):
        # How to set the stop --Key point
        stop = nextStart
        while start != stop:
            temp = start.next
            start.next = nextStart
            nextStart = start
            start = temp
        preEnd.next = end
        
~~~

## Test Cases
1. One or zero node in the list
2. anything, k=0 or 1 => return original head
2. 1-2, 2  => 2-1
3. 1-2-3, 2 => 2-1-3
4. 1-2-3-4, 2 => 2-1-4-3
5. 1-2-3-4-5, 5 => return original head


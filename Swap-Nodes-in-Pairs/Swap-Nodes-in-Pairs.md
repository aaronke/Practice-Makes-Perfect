# [Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)

## Description
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given `1->2->3->4`, you should return the list as `2->1->4->3`.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
## Analysis
So similar as most of linked list issues, the most important part is careful about how to rotate the nodes. In this issues, the only thing we need to do is to swap two nodes in pair. 

**Method 1 --** This is my first try. It lets me understand that there are three connections should be changed. 
Before Change:`UpNode -> FirstNode -> SecondNode -> LowerNode`  
After Change:`UpNode -> SecondNode -> FirstNode -> LowerNode`
Remember to record the upNode in each iteration. And be CAREFUL about the sequence of assignment. 

**Method 2 --** It is very simple and smart to use recursion! However space complexity is `O(n)`. No meet requirement but still good to know!

**Method 3 --** It's a refined version for Method 1. Firstly, it creates a new head and therefore there is no need to put the first pair out of while loop(Method 1 did that!) And another improvement is to choose the correct temp variable.


Method 1 -- Switch two nodes and choose `nextNode.next.next` as temp variable

             upNode.next = nextNode.next
             upNode = nextNode
             temp = nextNode.next.next
             nextNode.next.next = nextNode
             nextNode.next = temp
             nextNode = temp

However it may be better to like method 3. It will reduce one dot operation. And see the refined code as follow.

            temp = nextNode.next
            upNode.next = temp
            nextNode.next = temp.next
            upNode = nextNode
            temp.next = nextNode
            nextNode = nextNode.next


## Python Code
~~~python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Method 1 -- My first shot
        # if not (head and head.next):
        #     return head
        
        # nextNode = head.next.next
        # head.next.next = head
        # newHead = head.next
        # head.next = nextNode
        
        # upNode = head
        # while nextNode and nextNode.next:
        #     # Update UpNode
        #     upNode.next = nextNode.next
        #     upNode = nextNode
            
        #     # Switch two Node
        #     temp = nextNode.next.next
        #     nextNode.next.next = nextNode
        #     nextNode.next = temp
        #     nextNode = temp
            
        # return newHead
        
        # Method 2 -- recursion
        # if not (head and head.next):
        #     return head
        # temp =  head.next
        # head.next =  self.swapPairs(temp.next)
        # temp.next = head
        # return temp
        
        # Method 3 -- Refined Iteration
        newHead = ListNode(0)
        newHead.next = head
        upNode = newHead
        while (head and head.next):
            temp = head.next
            head.next = temp.next
            
            temp.next = head
            upNode.next = temp
            
            ## If I swtch the two lines of code below, the code will run forever.
            upNode = head
            head = head.next
        
        return newHead.next
~~~

## Notes

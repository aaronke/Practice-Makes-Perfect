
# [Reorder List](https://leetcode.com/problems/reorder-list/)

## Description
Given a singly linked list L: L0→L1→…→Ln-1→Ln,  
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,
Given `{1,2,3,4}`, reorder it to `{1,4,2,3}`.
## Analysis
Method 1 -- Similar as another single linked problem -- [Palindrome Linked List](https://github.com/haoyuchen1992/Practice-Makes-Perfect/blob/master/Palindrome-Linked-List/Palindrome-Linked-List.md). We can choose to change the direction of the second-half single linked list. And then merge these two linked list. A blended one will be given.

However, there are a lot of details that should be careful.  
#### 1. how to get into the middle of the list:  
**Wrong Code:** 

~~~
while slow.next and  fast.next.next:
            slow = slow.next
            fast = fast.next.next

~~~
**Correct Code:** Because if `fast.next` is none, `fast.next.next` will be illigal. `fast.next` is not `None` and `slow.next` will definitely not `None` also. Therefore, we could get the correct version below.

~~~
while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
~~~


#### 2. Even and odd number nodes
Be careful about the even and odd number of nodes. In the method below, we distinguish it. It makes thing become too much complicated. Althought it works and also beats rest of 87%, a better solution will be updated soon!

## Python Code
~~~python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        fast = head
        slow = head
        
        ## Why fast.next and fast.next.next? Because if fast.next is none, we can't directly test fast.next.next
        while slow.next and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        ## if lenght is even, do slow.next. If not, do slow
        medium = slow
        if(fast.next):
            medium = slow.next
        nextP = None
        
        # Get the medium 1->2->3->4->5  =>  1->2-> 3  None <- 4 <- 5
        while medium.next:
            nextMedium = medium.next 
            medium.next = nextP
            nextP = medium
            medium = nextMedium
            if medium.next == None:
                medium.next = nextP
                break
        # Combine(merge) two single linked list  (1->2-> 3  None <- 4 <- 5) => (1->5->2->4->3)
        while head.next and medium.next:
            temp1 = head.next
            temp2 = medium.next
            head.next = medium
            head = temp1
            medium.next = head
            medium = temp2
            
~~~
## Notes
# [Rotate List](https://leetcode.com/problems/rotate-list/)

## Description
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given `1->2->3->4->5->NULL` and `k = 2`,  
return `4->5->1->2->3->NULL`.
## Analysis
At the beginning, I was trying to break the linked list into two parts and then connected together. However, it can't solve the situation where `k` is larger than the length of linked list. Therefore, it would be better to use circle linked list. In that case, we can use mode to get the correct offset, no matter how big `k` is.

* Time complexity: `O(n)`
* Space Complexity: `O(1)`

## Python Code
~~~Python
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # Use circle linked list
        if head == None or head.next == None or k == 0:
            return head

        listLen = 1
        end = head
        # Get the length of list and the tail node
        while end.next:
            listLen += 1
            end =  end.next

        # Circle the list    
        end.next = head
        # Get the offset
        offset = abs(listLen - (k%listLen))

        count = 0
        changeNode = end
        # Find the break node
        while count < offset:
            changeNode = changeNode.next
            count += 1

        # Assign None to break node's next and get a result list
        newHead = changeNode.next
        changeNode.next =  None

        return newHead
~~~

## Notes
1. Please manully check the variable names before running the code. It is trival but very important！
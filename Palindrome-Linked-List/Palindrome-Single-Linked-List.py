# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if (head == None) or (head.next == None):
            return True
        slow = fast = head
        ## Get the middle
        while fast.next and fast.next.next:
            slow =  slow.next
            fast =  fast.next.next
        nextNode = None
        middle = slow.next
        while middle:
            aNode = middle
            middle = middle.next
            aNode.next = nextNode
            nextNode = aNode
        
        while aNode and head:
            if aNode.val != head.val:
                return False
            aNode = aNode.next
            head = head.next
        
        return True 

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(2)
l4 = ListNode(1)

l1.next = l2
l2.next = l3
l3.next = l4



s = Solution()
print s.isPalindrome(l1)

        
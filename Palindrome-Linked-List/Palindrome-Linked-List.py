# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
import copy
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if (head == None) or (head.next == None):
            return True
        value = []
        while head:
            value.append(head.val)
            head =  head.next
        reverseValue = list(reversed(value))
        # reverseValue = copy.deepcopy(value)
        print value
        print reverseValue
        if value == reverseValue:
            return True
        return False
s = Solution()
l1 = ListNode(1)
l2 = ListNode(2)
l1.next = l2
print s.isPalindrome(l1)
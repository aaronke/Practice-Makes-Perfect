# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
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
                if nextStart:
                    print nextStart
                else:
                    print None
                # preEnd = start
                # start = nextStart
                count = 0
                # head = nextStart 
            else:
                head = head.next 
                # else:
                #     head = head.next
        return rsNode.next
    def reverseList(self, preEnd, start, end, nextStart):
        # How to set the stop --Key point
        # stop = nextStart
        # while start != stop: 
        #     temp = start.next
        #     start.next = nextStart
        #     nextStart = start
        #     start = temp
        # preEnd.next = end

s = Solution()
head = ListNode(0)
print s.reverseKGroup(head, 1)

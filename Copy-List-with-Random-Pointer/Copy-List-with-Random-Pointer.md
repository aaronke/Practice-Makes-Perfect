# [Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/)

## Description
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
## Analysis
This is a hard issue. 

1. Copy all the relationship (all the pointer - backward and forward)
2. And also the ramdom pointer would create circle and how to make sure don't lead to dead circle in looping

In my native BFS method, I try to use list with lenght of 3 to remeber the Node A, A's random, A's next. In order to avoid going to dead circle, I create a variable -- uniqueNodes and to make sure no replicate node.

* Time Complexity -- `O(n)`
* Space Complexity -- `O(n)`

However, the idea is clear, but the implementation just drives me crazy. So many traps are there.    TO Be Updated!!

BTW: The first time wrote code on Google docs, I should change the line height in the future. Not so readable.
 

## Python Code
~~~python
# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
    #     if (head == None):
    #         return None
    #     newHead = RandomListNode(head.label)
    #     newHead.random = head.random
    #     newHead.next = head.next
    #     untouchedNodes = []
    #     uniqueNodes = []
    #     touchedNodes = [newHead]
    #     untouchedNodes = self.addUntouchedNodes(newHead, untouchedNodes, touchedNodes, uniqueNodes)
    #     while (untouchedNodes):
    #         newuntouchedNodes = []
    #         for nodes in untouchedNodes:
    #             nodes[0]= self.deepCopyNode(nodes)
    #             newuntouchedNodes = self.addUntouchedNodes(nodes[0], newuntouchedNodes, touchedNodes, uniqueNodes)
            
    #         untouchedNodes = newuntouchedNodes

    #     return newHead
        
    # def deepCopyNode(self, nodes):
    #     newNode =  RandomListNode(nodes[0].label)
    #     if nodes[1]:
    #         nodes[1].random = newNode
    #     if nodes[2]:
    #         nodes[2].next = newNode
    #     return newNode 
    # def addUntouchedNodes(self, checkNode, untouchedNodes, touchedNodes, uniqueNodes):
    #     if (checkNode.next and ([checkNode.next, None, checkNode] not in touchedNodes) and self.notExist(checkNode, uniqueNodes)):
    #         # [checkNode.next(untouchedNode), randomParent, nextParent]
    #         untouchedNodes.append([checkNode.next, None, checkNode])
    #     if (checkNode.random and ([checkNode.random, checkNode, None] not in touchedNodes) and self.notExist(checkNode, uniqueNodes)):
    #         untouchedNodes.append([checkNode.random, checkNode, None])
    #     return untouchedNodes
    
    # def notExist(self, checkNode, uniqueNodes):
    #     for node in uniqueNodes:
    #         if checkNode.label == node.label and checkNode.random == node.random and checkNode.next == node.next:
    #             return False
    #     return True
~~~
## Notes



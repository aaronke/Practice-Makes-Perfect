# [Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/)

## Description
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

## Analysis
### Clarifications
1. Does it mean I need to check every subtree1? Yes 

### Method
So use BFS and check the sub-tree of every node. There are three level of implemenations.

1. Find all the nodes
2. Compare the deepth of the left and right sub-tree
3. Get the deepth of a sub-tree

* Time Complexity: `O(nlogn)`
* Space Complexity: `O(n)`

## Python Code
~~~
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        check = [root]
        while check:
            node = check.pop()
            if not self.isNodeBalanced(node):
                return False
            if node.left:
                check.append(node.left)
            if node.right:
                check.append(node.right)
        return True
    
    
    def isNodeBalanced(self, node):
        if not node:
            return True
    
        leftL = self.getDeepth(node.left)
        rightL = self.getDeepth(node.right)
        
        return True if abs(leftL - rightL) < 2 else False 
    def getDeepth(self, node):
        if not node:
            return 0
        nodes = [node]
        count = 0
        while nodes:
            newNodes = []
            for node in nodes:
                if node.left:
                    newNodes.append(node.left)
                if node.right:
                    newNodes.append(node.right)
            nodes = newNodes
            count += 1
        return count
~~~
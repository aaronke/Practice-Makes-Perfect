# [Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/)

## Description
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

For example:
Given the following binary tree,

~~~
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
~~~  
You should return `[1, 3, 4]`.

## Analysis
At the beginning, it is easy to make mistake and think the right node will always be result. But we should also think about there case, when the right node is none and then left node could be the result. Therfore, the safest way to do this is to use BFS and get all the nodes in the same level and then only use the last node (right most one) as our result.

* Time Complexity: `O(n)`
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
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        rs  = []
        if root:
            nodes = [root]
        else:
            return rs
        while nodes:
            rs.append(nodes[-1].val)
            newNodes = []
            for node in nodes:
                if node.left:
                    newNodes.append(node.left)
                if node.right:
                    newNodes.append(node.right)
            nodes = newNodes
        return rs
~~~

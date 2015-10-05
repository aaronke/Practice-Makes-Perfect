
# [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)

## Description
Invert a binary tree.

~~~

     4
   /   \
  2     7
 / \   / \
1   3 6   9
~~~
to

~~~
     4
   /   \
  7     2
 / \   / \
9   6 3   1
~~~
## Analysis
Just find all the nodes and exchange the left and right node.

* Time Complexity: `O(n)`
* Space Complexity: `O(1)`

## Python Code
~~~
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        check = [root]
        while check:
            swith = check.pop() 
            temp = swith.left
            swith.left = swith.right
            swith.right = temp
            
            if swith.left:
                check.append(swith.left)
            if swith.right:
                check.append(swith.right)
        
        return root
~~~
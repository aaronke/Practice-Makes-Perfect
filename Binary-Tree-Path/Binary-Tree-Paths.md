# [Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/)

## Description
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

~~~
   1
 /   \
2     3
 \
  5
~~~  
All root-to-leaf paths are:

~~~
["1->2->5", "1->3"]
~~~
## Analysis
Method One -- It is easy to figure it out and we should use Deep First Search (DFS) algorithm. In that case, we can see that each iteration, two directions(Left and Right) should be checked until getting None object.

## Python Code
~~~
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []

        if root and not root.right and not root.left:
            return [str(root.val)]  # Remeber to return array not number
            
        rsLeft = self.binaryTreePaths(root.left)
        for i in range(len(rsLeft)):
            rsLeft[i] = str(root.val) + "->" + rsLeft[i] 
            
        rsRight = self.binaryTreePaths(root.right)
        for i in range(len(rsRight)):
            rsRight[i] = str(root.val) + "->" + rsRight[i] 
        
        return rsRight + rsLeft     
~~~        
## Notes
1 . python tutor visualization help me again for debugging and find the return type should be array, not string. Be careful!
http://www.pythontutor.com/visualize.html
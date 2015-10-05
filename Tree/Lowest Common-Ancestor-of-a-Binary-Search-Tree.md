# [Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)

## Description
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

~~~

        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5
~~~
For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another example is LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
## Analysis
Find the parents list for both two nodes and then search from top to bottom. Once finding the different node, then return the last same node as the LCA.

* Time Complexity: `O(n)`
* Space Complexity: `O()`

## Python Code

~~~
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        pA = self.findNode(root, p)
        qA = self.findNode(root, q)
        pre = root
        for i in range(min(len(pA),len(qA))):
            if self.isSame(pA[i], qA[i]):
                pre = pA[i]
            else:
                return pre
        return pre
            
    
    
    def findNode(self, root, f):
        rs = []
        while root:
            rs.append(root)
            if self.isSame(f, root):
                return rs
            if f.val > root.val:
                root = root.right
            elif f.val < root.val:
                root = root.left
        
        return rs
                
    def isSame(self, A, B):
        return True if A.val == B.val and A.left == B.left and A.right == B.right else False
~~~

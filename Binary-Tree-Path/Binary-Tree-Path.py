# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []

        if root and not root.right and not root.left:
            return [str(root.val)] 
            
        rsLeft = self.binaryTreePaths(root.left)
        for i in range(len(rsLeft)):
            rsLeft[i] = str(root.val) + "->" + rsLeft[i] 
            
        rsRight = self.binaryTreePaths(root.right)
        for i in range(len(rsRight)):
            rsRight[i] = str(root.val) + "->" + rsRight[i] 
        
        return rsRight + rsLeft

treeNode1 = TreeNode(1)
treeNode2 = TreeNode(2)
treeNode3 = TreeNode(3)

treeNode1.left = treeNode2
treeNode1.right = treeNode3

s = Solution()
print s.binaryTreePaths(treeNode1)

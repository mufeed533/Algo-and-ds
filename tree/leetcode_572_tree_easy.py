"https://leetcode.com/problems/subtree-of-another-tree/description/"

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSametree(self, root, subRoot):
        if (not root and not subRoot):
            return True
        if  (root and subRoot and root.val == subRoot.val):
             return (self.isSametree(root.left, subRoot.left) and 
             self.isSametree(root.right, subRoot.right))

        return False

    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if not root:
            return False
        if not subRoot:
            return True        

        if self.isSametree(root, subRoot):
            return True

        return (self.isSubtree(root.left, subRoot) or
             self.isSubtree(root.right, subRoot))
            


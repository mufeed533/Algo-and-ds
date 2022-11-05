"https://leetcode.com/problems/delete-node-in-a-bst/submissions/837299450/"

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = 

class Solution(object):
    def find_minimum(self, root):
        while root and root.left:
            root = root.left
        return root

    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return None

        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            min_val = self.find_minimum(root.right)
            root.val = min_val.val
            root.right = self.deleteNode(root.right, min_val.val)

        return root

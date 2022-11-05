"https://leetcode.com/problems/kth-smallest-element-in-a-bst/submissions/837308908/"

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sort_tree(self, root):
        if not root:
            return []
        return self.sort_tree(root.left) + [root.val] + self.sort_tree(root.right)

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        sorted_arr = self.sort_tree(root)
        return sorted_arr[k-1]
        
        

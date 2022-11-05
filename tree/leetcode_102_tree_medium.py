"https://leetcode.com/problems/binary-tree-level-order-traversal/description/"
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        queue = [root]
        results = []

        while queue:
            level = []

            for i in range(len(queue)):
                curr = queue.pop(0)
                if curr:
                    level.append(curr.val)
                    queue.append(curr.left)
                    queue.append(curr.right)
            if level:
                results.append(level)
        return results

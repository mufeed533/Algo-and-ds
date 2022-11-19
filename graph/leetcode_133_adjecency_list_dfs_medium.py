"https://leetcode.com/problems/clone-graph/description/"

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        hash_map = {}

        def clone(node):
            if node in hash_map:
                return hash_map[node]
            copy = Node(node.val)
            hash_map[node] = copy
            for neighbor in node.neighbors:
                hash_map[node].neighbors.append(clone(neighbor))
            return copy
        
        return clone(node) if node else None




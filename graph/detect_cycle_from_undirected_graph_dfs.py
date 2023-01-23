"""
Write a python function to detect cycle from undirected graph using DFS
"""

visited = set()


def dfs(adj_list: dict, node: int, parent: int) -> bool:
    visited.add(node)

    for child_node in adj_list.get(node, []):
        if child_node in visited:
            if child_node != parent:
                return True
        else:
            if dfs(adj_list, child_node, node):
                return True
    return False


def detect_cycle(adj_list: dict) -> bool:
    for node in adj_list:
        if node not in visited:
            if dfs(adj_list, node, -1):
                return True
    return False


adjacency_list = {
    1: [2, 7],
    2: [1, 3],
    3: [2, 4],
    4: [3, 5],
    5: [4, 8],
    8: [5],
    6: [7],
    7: [6, 1],
    9: [10, 11],
    10: [9, 11]
}
print(detect_cycle(adjacency_list))

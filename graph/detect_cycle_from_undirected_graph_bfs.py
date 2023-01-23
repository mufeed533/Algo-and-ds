"""
Write a python function to detect cycle from undirected graph using BFS
"""

from collections import deque


def detect_cycle_using_bfs(adj_list: dict, start_node: int) -> bool:
    visited = set()
    visited.add(start_node)
    queue = deque()
    queue.append((start_node, -1))

    while queue:
        node, parent = queue.popleft()

        for child_node in adj_list.get(node, []):
            if child_node in visited:
                if child_node == parent:
                    continue
                else:
                    return True
            else:
                visited.add(child_node)
                queue.append((child_node, node))

    return False


adjacency_list = {
    1: [2, 7],
    2: [1, 3],
    3: [2, 4],
    4: [3, 5],
    5: [4, 8],
    8: [5],
    6: [7],
    7: [6, 1]
}
print(detect_cycle_using_bfs(adjacency_list, 1))

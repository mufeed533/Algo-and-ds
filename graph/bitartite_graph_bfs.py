"""
Write a python function to check if a graph is bipartite.
Bipartite graphs are those, in which each node can be colores with either of given two colors, but with the condition that
any two adjacent nodes will not have same colors

Solve using BFS
"""

from collections import deque


def check_bipartite(ad_list: dict, st_node: int) -> bool:
    queue = deque()
    colored = {}

    queue.append(st_node)
    colored[st_node] = 1

    while queue:
        node = queue.popleft()
        parent_color = colored[node]
        for child_node in ad_list.get(node, []):
            if child_node in colored:
                if colored[child_node] == parent_color:
                    return False
            else:
                colored[child_node] = 0 if parent_color == 1 else 1
                queue.append(child_node)
    return True


adjacency_list = {
    1: [2],
    2: [1, 3, 7],
    3: [2, 4],
    4: [3, 5],
    5: [4, 6, 8, 9],
    6: [7, 5, 9],
    7: [2, 6],
    8: [5],
    9: [5, 6]
}

print(check_bipartite(adjacency_list, 1))

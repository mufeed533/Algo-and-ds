"""
Write a python function to check if a graph is bipartite.
Bipartite graphs are those, in which each node can be colores with either of given two colors, but with the condition that
any two adjacent nodes will not have same colors

Solve using DFS
"""

colored = {}


def dfs(ad_list: dict, node: int, parent_color: int) -> bool:
    for child_node in ad_list[node]:
        if child_node in colored:
            if colored[child_node] == parent_color:
                return False
        else:
            colored[child_node] = 1 if parent_color == 0 else 0
            if not dfs(ad_list, child_node, colored[child_node]):
                return False
    return True


def check_bipartite(ad_list: dict, st_node: int) -> bool:
    colored[st_node] = 1
    if not dfs(ad_list, st_node, colored[st_node]):
        return False
    return True


adjacency_list = {
    1: [2],
    2: [1, 3, 7],
    3: [2, 4],
    4: [3, 5],
    5: [4, 6, 8],
    6: [7, 5],
    7: [2, 6],
    8: [5],
    # 9: [5, 6]
}

print(check_bipartite(adjacency_list, 1))

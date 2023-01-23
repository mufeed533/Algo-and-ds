"""
Detect a cycle from directed graph
We can not use the same DFS algorithm here as it might lead us to wrong output
We need to ensure a cycle exists in the same path, hence we need to store the path also into a set
"""
visited = set()
path = set()


def dfs(adjacency_list: dict, node: int) -> bool:
    visited.add(node)
    path.add(node)

    for child_node in adjacency_list[node]:
        if child_node not in visited:
            if dfs(adjacency_list, child_node):
                return True
        elif child_node in path:
            return True

    path.remove(node)
    return False


def detect_cycle(adjacency_list: dict) -> bool:
    for node in adjacency_list:
        if node not in visited:
            if dfs(adj_list, node):
                return True

    return False


adj_list = {
    1: [2],
    2: [3],
    3: [4],
    4: [5],
    5: [6],
    7: [4],
    6: [7, 9],
    9: []
}

print(detect_cycle(adj_list))

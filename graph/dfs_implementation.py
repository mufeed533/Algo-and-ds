"""
DFS : Depth first search

You go deeper than on breadth level
Since we are going deeper, obviously we have to use recursion here for traversal

Algo:
adjacency_list = {...}
Visited[node] = True
dfs.append(Node)

for i in adjacency_list[node]:
    if i not in visited:
        dfs(i)

"""


def dfs(adj_list: dict, visited: set, node: int):
    visited.add(node)

    for child_node in adj_list.get(node, []):
        if child_node not in visited:
            print(child_node)
            dfs(adj_list, visited, child_node)


def dfs_implementation(adj_list: dict, node: int):
    visited = set()
    print(node)
    dfs(adj_list, visited, node)


adjacency_list = {
    1: [2, 7],
    2: [1, 3],
    3: [2, 4],
    4: [3, 5],
    5: [4, 8, 6],
    8: [5],
    6: [7, 5],
    7: [6, 1]
}
print(dfs_implementation(adjacency_list, 1))

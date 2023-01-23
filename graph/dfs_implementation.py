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
"""
DFS algorithm for graph

Graphs are directed or undirected, graphs can have weights as well.
Path :  a path from node a to b is possible if there is continuous edge between a and b and no node is repeating
degree :  edges in and out of any node
total degrees = 2 * Edges

Graphs representations:
1) Adjacency matrix
   Using matrix representation for graph, it is costly in terms of space complexity
2) Adjacency list
   Using dictionary we can represent graph, key will be node and values will be neighbouring nodes
   Better in terms of space complexity

BFS Algorithm:
Always have visited set, adjacency list and a queue.
Queue is required because we need to cover level order

Algorithm:
Add initial node into queue.
visited = set(first node)
adj = {...}
while queue:
    val = queue.pop()
    for i in adj[val]:
        if i not in visited:
            print(i)
            queue.append(i)
            visited.add(i)
"""

from collections import deque


def bfs(adj_list: dict, st) -> None:
    queue = deque()
    queue.append(st)
    visited = set()
    visited.add(st)

    while queue:
        ele = queue.popleft()
        print(ele)
        for i in adj_list.get(ele, []):
            if i not in visited:
                queue.append(i)
                visited.add(i)


adj = {
    1: [2, 3],
    2: [1, 4],
    3: [4, 5],
    4: [2, 3],
    5: [2]
}

bfs(adj, 1)

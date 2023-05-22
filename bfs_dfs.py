# implementing BFS USING QUEUE
from collections import deque
graph = {0:[1,2], 1:[0,2], 2:[0,3], 3:[3]}
def bfs(graph, root):
    visited = set()
    queue = deque([root])

    while queue:
         vertex = queue.popleft()
         visited.add(vertex)
         print(vertex, end = " ")
         for i in graph[vertex]:
             if i not in visited:      
                 queue.append(i)           
bfs(graph, 2)
print("\n")

#implementing DFS USING STACK
def dfs(graph, root):
    visited = set()
    stack = [root]

    while stack:
            vertex = stack.pop() 
            visited.add(vertex)
            print(vertex, end = " ")
            for i in graph[vertex]:
             if i not in visited:      
                 stack.append(i) 
dfs(graph, 2)

#OUTPUT1
# graph = {0:[1,2], 1:[0,2], 2:[0,3], 3:[3]}
# 2 0 3 1 
# 2 3 0 1

#OUTPUT2
# graph = {0:[1,2,4], 1:[2], 2:[0,3], 3:[3], 4:[0]}
# 2 0 3 1 4 
# 2 3 0 4 1
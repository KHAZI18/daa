queue = []
visited = []

graph = [[0,1,1,1],[0,0,1,1],[0,0,0,1],[0,0,0,0]]
n = len(graph)

def bfs(u):
    count = 0
    queue.append(u)
    visited[u]=1
    while queue:
        u = queue.pop(0)
        count+=1
        print(u)
        for v in range(n):
            if visited[v] == 0 and graph[u][v] ==1:
                queue.append(v)
                visited[v]=1

def main():
    source = 0
    for i in range(n):
        visited.append(0)
    print("Adjacency Matrix")
    for row in graph:
        print(row)
    print("BFS Order")
    bfs(source)

main()

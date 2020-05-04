from collections import defaultdict
class Graph:
    def __init__(self, n):
        self.n = n
        self.adj = defaultdict(list)
    
    def connect(self, x, y):
        self.adj[x].append(y) if y not in self.adj[x] else None
        self.adj[y].append(x) if x not in self.adj[y] else None
        
    def find_all_distances(self, s):
        visited = [False for _ in range(self.n)]
        queue = []
        level = [-1 for _ in range(self.n)]
        dist = [-1 for _ in range(self.n)]

        queue.append(s)
        level[s] = 0
        dist[s] = 0
        while queue:
            t = queue.pop(0)
            if visited[t] == False:
                visited[t] = True
                for n in self.adj[t]:
                    if visited[n] == False:
                        queue.append(n)
                        if level[n] == -1:
                            level[n] = level[t] + 6
                        if dist[n] == -1:
                            dist[n] = level[n]
                
        print(*(dist[:s] + dist[s+1:]))
    

t = int(input())
for i in range(t):
    n,m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph.connect(x-1,y-1) 
    s = int(input())
    graph.find_all_distances(s-1)
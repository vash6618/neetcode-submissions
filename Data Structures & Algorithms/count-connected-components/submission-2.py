class Solution:
    def bfs(self, node, graph, vis):
        queue = deque()
        queue.append(node)
        vis[node] = True
        while queue:
            node = queue.popleft()
            for neigh in graph[node]:
                if not vis[neigh]:
                    vis[neigh] = True
                    queue.append(neigh)

        
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = [[] for _ in range(n)]
        for n1, n2 in edges:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)
        vis = [False for _ in range(n)]
        comp = 0
        for i in range(n):
            if not vis[i]:
                comp += 1
                self.bfs(i, adj_list, vis)
        return comp
            
        
class Solution:
    def dfs(self, graph, vis, node):
        if vis[node]:
            return False
        tree, vis[node] = True, True
        for neigh in graph[node]:
            if not vis[neigh]:
                tree = tree and self.dfs(graph, vis, neigh)
        return tree
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        adj_list = [[] for i in range(n)]
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
        st = 0
        vis = [False] * n
        ans = self.dfs(adj_list, vis, st)
        return ans if all(vis) else False

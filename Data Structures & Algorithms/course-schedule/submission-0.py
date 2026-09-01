class Solution:
    def dfs(self, graph, vis, node):
        vis[node] = 1
        cycle = False
        for neigh in graph[node]:
            if vis[neigh] == 0:
                cycle = cycle or self.dfs(graph, vis, neigh)
            elif vis[neigh] == 1:
                return True
        vis[node] = -1
        return cycle


    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = [[] for _ in range(numCourses)]
        for edge in prerequisites:
            adj_list[edge[1]].append(edge[0])
        vis = [0] * numCourses
        for i in range(numCourses):
            if vis[i] == 0:
                if self.dfs(adj_list, vis, i):
                    return False
        return True
        
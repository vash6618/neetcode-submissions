class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) < n-1:
            return False
        adj_list = [[] for i in range(n)]
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
        st = 0
        vis = [0 for i in range(n)]
        queue = deque()
        queue.append(st)
        while(queue):
            node = queue.popleft()
            if vis[node] == 1:
                return False
            vis[node] = 1
            for neigh in adj_list[node]:
                if vis[neigh] == 0:
                    queue.append(neigh)
        return True if all(node == 1 for node in vis) else False

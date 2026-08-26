class Solution:
    
    def dfs(self, adj_list, vis, node, parent):
        vis[node] = True
        for neigh in adj_list[node]:
            if not vis[neigh]:
                if self.dfs(adj_list, vis, neigh, node):
                    return True
            else:
                if neigh != parent: # cycle
                    return True
        return False

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj_list = [set() for i in range(len(edges) + 1)]
        len
        for edge in edges:
            adj_list[edge[0]].add(edge[1])
            adj_list[edge[1]].add(edge[0])
        st = 0
        result = []
        
        for edge in edges:
            vis = [False] * (len(edges) + 1)
            vis[0] = True
            adj_list[edge[0]].remove(edge[1])
            adj_list[edge[1]].remove(edge[0])
            ans = self.dfs(adj_list, vis, edge[0], None)
            if not ans and all(vis):    
                result = edge
            adj_list[edge[0]].add(edge[1])
            adj_list[edge[1]].add(edge[0])
        return result

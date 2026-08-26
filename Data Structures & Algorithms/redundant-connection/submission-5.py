class Solution:
    
    def dfs(self, adj_list, vis, node, parent, cycle_nodes):
        vis[node] = True
        cycle_nodes.append(node)
        for neigh in adj_list[node]:
            if not vis[neigh]:
                cycle = self.dfs(adj_list, vis, neigh, node, cycle_nodes)
                if cycle:
                    return cycle
            else:
                if neigh != parent: # cycle
                    return list(cycle_nodes[cycle_nodes.index(neigh):])
        cycle_nodes.pop()
        return None
        
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj_list = [set() for i in range(len(edges) + 1)]
        for edge in edges:
            adj_list[edge[0]].add(edge[1])
            adj_list[edge[1]].add(edge[0])
        vis = [False] * (len(edges) + 1)
        vis[0] = True
        running_cycle = []
        final_cycle = set(self.dfs(adj_list, vis, 1, None, running_cycle))
        for node1, node2 in edges:
            if node1 in final_cycle and node2 in final_cycle:
                result = [node1, node2]
        return result

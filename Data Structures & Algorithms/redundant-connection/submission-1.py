class Solution:
    
    def dfs(self, adj_list, vis, node, parent, cycle_nodes, final_cycle):
        vis[node] = True
        cycle_nodes.append(node)
        for neigh in adj_list[node]:
            if not vis[neigh]:
                if self.dfs(adj_list, vis, neigh, node, cycle_nodes, final_cycle):
                    return True
            else:
                if neigh != parent: # cycle
                    final_cycle.extend(cycle_nodes[cycle_nodes.index(neigh):])
                    return True
        cycle_nodes.pop()
        return False
        




    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj_list = [set() for i in range(len(edges) + 1)]
        len
        for edge in edges:
            adj_list[edge[0]].add(edge[1])
            adj_list[edge[1]].add(edge[0])
        st = 0
        result = []
        vis = [False] * (len(edges) + 1)
        vis[0] = True
        running_cycle = []
        final_cycle = []
        self.dfs(adj_list, vis, 1, None, running_cycle, final_cycle)
        final_cycle = set(final_cycle)
        for edge in edges:
            if edge[0] in final_cycle and edge[1] in final_cycle:
                result = edge
        return result

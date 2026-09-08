class Solution:
    def dfs(self, graph, vis, node, course_order):
        vis[node] = 1
        cycle = False
        for neigh in graph[node]:
            if vis[neigh] == 0:
                cycle = cycle or self.dfs(graph, vis, neigh, course_order)
            elif vis[neigh] == 1:
                return True
        vis[node] = -1
        course_order.append(node)
        return cycle


    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = [[] for _ in range(numCourses)]
        for edge in prerequisites:
            adj_list[edge[1]].append(edge[0])
        vis = [0] * numCourses
        courses = []
        for i in range(numCourses):
            course_order = []
            if vis[i] == 0:
                if self.dfs(adj_list, vis, i, course_order):
                    return []
                courses += course_order
        courses.reverse()
        return courses
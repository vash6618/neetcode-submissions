class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]
        for edge in prerequisites:
            adj_list[edge[1]].append(edge[0])
            indegree[edge[0]] += 1
        queue = deque()
        for ind, deg in enumerate(indegree):
            if deg == 0:
                queue.append(ind)
        while queue:
            node = queue.popleft()
            for neigh in adj_list[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    queue.append(neigh)
        return True if not any(indegree) else False
        
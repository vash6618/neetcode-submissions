class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indeg = [0 for _ in range(numCourses)]
        for course1, course2 in prerequisites:
            graph[course2].append(course1)
            indeg[course1] += 1
        queue = deque(i for i in range(numCourses) if indeg[i] == 0)
        top_sort = []
        taken = 0
        while queue:
            course = queue.popleft()
            taken += 1
            top_sort.append(course)
            for neigh in graph[course]:
                indeg[neigh] -= 1
                if indeg[neigh] == 0:
                    queue.append(neigh)
        return top_sort if taken == numCourses else []
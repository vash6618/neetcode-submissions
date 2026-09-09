class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m = {key: i for i, key in enumerate(nums)}
        graph = [[] for _ in range(len(nums))]
        for key in m:
            if key + 1 in m:
                graph[m[key]].append(m[key + 1])
                graph[m[key + 1]].append(m[key])
        vis = [False for _ in range(len(nums))]
        ans = 0
        for i in range(len(nums)):
            if vis[i] == False:
                queue = deque()
                queue.append(i)
                comp = 0
                vis[i] = True
                while(queue):
                    node = queue.popleft()
                    comp += 1
                    for neigh in graph[node]:
                        if vis[neigh] == False:
                            queue.append(neigh)
                            vis[neigh] = True
                ans = max(ans, comp)
        return ans
        
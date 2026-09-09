class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = defaultdict(int)
        for key in nums:
            m[key] += 1
        h = []
        for key in m:
            heapq.heappush(h, (-m[key], key))
        ans = []
        for i in range(k):
            _, val = heapq.heappop(h)
            ans.append(val)
        return ans

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = defaultdict(int)
        for key in nums:
            m[key] += 1
        h = []
        for key in m:
            if len(h) < k:
                heapq.heappush(h, (m[key], key))
            else:
                if m[key] > h[0][0]:
                    heapq.heappop(h)
                    heapq.heappush(h, (m[key], key))
        ans = [key for _, key in h]
        return ans

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = defaultdict(int)
        for key in nums:
            m[key] += 1
        h = []
        for key, cnt in m.items():
            if len(h) < k:
                heapq.heappush(h, (cnt, key))
            else:
                if cnt > h[0][0]:
                    heapq.heappop(h)
                    heapq.heappush(h, (cnt, key))
        ans = [key for _, key in h]
        return ans

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
                freq, val = heapq.heappop(h)
                if m[key] > freq:
                    heapq.heappush(h, (m[key], key))
                else:
                    heapq.heappush(h, (freq, val))
        ans = [key for _, key in h]
        return ans

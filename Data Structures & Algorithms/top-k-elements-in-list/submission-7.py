from itertools import islice

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = defaultdict(int)
        for key in nums:
            m[key] += 1
        buckets = defaultdict(list)
        ans, largest_key = [], 0
        for key, cnt in m.items():
            buckets[cnt].append(key)
            largest_key = max(largest_key, cnt)
        for i in range(largest_key, -1, -1):
            if k <= 0:
                break
            sliced_set = buckets.get(i, [])[:k]
            ans += sliced_set
            k -= len(sliced_set)
        return ans

from itertools import islice

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = defaultdict(int)
        for key in nums:
            m[key] += 1
        buckets = defaultdict(set)
        ans, largest_key = [], 0
        for key, cnt in m.items():
            buckets[cnt].add(key)
            largest_key = max(largest_key, cnt)
        for i in range(largest_key, -1, -1):
            if k <= 0:
                break
            sliced_set = list(islice(buckets.get(i, set()), k))
            ans += sliced_set
            k -= len(sliced_set)
        return ans

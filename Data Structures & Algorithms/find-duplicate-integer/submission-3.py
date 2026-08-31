class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        low, high = 1, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            cnt_less = 0
            for val in nums:
                if val <= mid:
                    cnt_less += 1
            if cnt_less > mid:
                high = mid
            else:
                low = mid + 1
        return low
        
            
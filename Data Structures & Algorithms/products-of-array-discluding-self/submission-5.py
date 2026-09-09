class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [key for key in nums]
        right = [key for key in nums]
        for i, key in enumerate(nums):
            left[i] = left[i-1] * key if i > 0 else key
        for i in range(len(nums)-1, -1, -1):
            right[i] = right[i+1] * nums[i] if i + 1 < len(nums) else nums[i]
        ans = []
        for i in range(len(nums)):
            prod = 1
            prod *= left[i-1] if i > 0 else 1
            prod *= right[i+1] if i + 1 < len(nums) else 1
            ans.append(prod)
        return ans

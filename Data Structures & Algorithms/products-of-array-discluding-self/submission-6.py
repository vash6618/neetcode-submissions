class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        left = 1
        for i, key in enumerate(nums):
            ans.append(left)
            left = left * key
        right = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= right
            right *= nums[i]
        return ans

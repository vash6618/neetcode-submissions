import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_run_sum, max_sum = nums[0], nums[0]
        for i in range(1, len(nums)):
            curr_run_sum = max(curr_run_sum + nums[i], nums[i])
            max_sum = max(max_sum, curr_run_sum)
        return max_sum
        
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            index = abs(nums[i])
            if nums[index - 1] < 0:
                return index
            else:
                nums[index - 1] *= -1
            
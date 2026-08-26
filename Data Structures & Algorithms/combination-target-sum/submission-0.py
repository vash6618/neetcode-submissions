class Solution:
    def get_lists(self, nums, target, ind, arr, int_arr):
        if ind == len(nums) or target < 0:
            return
        if target == 0:
            arr.append(list(int_arr))
            return 
        int_arr.append(nums[ind])
        self.get_lists(nums, target - nums[ind], ind, arr, int_arr)
        int_arr.pop()
        self.get_lists(nums, target, ind + 1, arr, int_arr)
        
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        arr, int_arr = [], []
        self.get_lists(nums, target, 0, arr, int_arr)
        return arr
        
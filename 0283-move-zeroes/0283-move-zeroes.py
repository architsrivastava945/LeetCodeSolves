class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        n = len(nums)
        for i in range(n,0,-1):
            if nums[i-1] == 0:
                count += 1
                nums.pop(i-1)
        zero = [0] * count
        nums = nums.extend(zero)
        
        
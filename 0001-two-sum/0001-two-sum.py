class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for i in range(length):
            secNum = target - nums[i]
            try:
                secIdx = nums.index(secNum)
                if i != secIdx:
                    return [i, secIdx]
            except:
                continue
        
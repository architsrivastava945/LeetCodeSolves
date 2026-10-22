class Solution:
    def check(self, nums: List[int]) -> bool:
        dip = False
        n = len(nums)
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                if dip:
                    return False
                else:
                    dip = True
        if dip:
            if nums[0] < nums[n-1]:
                return False
            else:
                return True
        else:
            return True

            
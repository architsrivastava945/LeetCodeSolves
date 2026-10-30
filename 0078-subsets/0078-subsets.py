class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        l = len(nums)
        sscount = 2 ** l
        for bit in range(sscount):
            sbnum = []
            for i in range(l):
                if (1 << i) & bit:
                    sbnum.append(nums[i])
            res.append(sbnum)
        return res
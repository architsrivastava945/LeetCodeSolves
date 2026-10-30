class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        def fn(i, sbnum):
            if i == len(nums):
                res.append(sbnum.copy())
                return
            sbnum.append(nums[i])
            fn(i+1, sbnum)
            sbnum.pop()
            fn(i+1, sbnum)
        fn(0,[])
        return res
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        adds = 0
        ans = 0
        for i in nums:
            adds += i
            if prefix[adds-k]:
                ans += prefix[adds-k]
            prefix[adds] += 1
        return ans


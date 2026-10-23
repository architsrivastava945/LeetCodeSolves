from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        lenghtDict = defaultdict(int)
        maxSize = 0
        for i in nums:
            if lenghtDict[i]:
                continue
            lenghtDict[i] = lenghtDict[i-1] + 1 + lenghtDict[i+1]
            maxSize = max(maxSize, lenghtDict[i])
            startnode = i-1 - lenghtDict[i-1] + 1
            lenghtDict[startnode] = lenghtDict[i]
            endnode = i+1 + lenghtDict[i+1] - 1
            lenghtDict[endnode] = lenghtDict[i]
        return maxSize
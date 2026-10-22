from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = Counter(nums)
        sortFreq = sorted(freq.items(), reverse=True, key=lambda x: x[1])
        return [x[0] for x in sortFreq[:k]]
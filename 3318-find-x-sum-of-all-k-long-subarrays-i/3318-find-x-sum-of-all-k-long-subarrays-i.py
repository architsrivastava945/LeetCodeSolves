class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        Answer = []
        for i in range(len(nums)-k+1):
            frequency = {}
            for j in nums[i:k+i]:
                if j in frequency:
                    frequency[j] += 1
                else :
                    frequency[j] = 1
            frequency = dict(sorted(frequency.items(), key=lambda item: item[0], reverse = True))
            frequency = sorted(frequency.items(), key=lambda item: item[1], reverse = True)
            Answer.append(sum([i[0]*i[1] for i in frequency[:x]]))
        return Answer
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        nums[-1:-(k+1):-1] = nums[-1:-(k+1):-1][::-1]
        nums[:n-k] = nums[:n-k][::-1]
        nums.reverse()


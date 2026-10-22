class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n

        i = 1
        j = 2

        for _ in range(3, n):
            temp = j
            j = i + j
            i = temp
        
        return i+j
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        m = abs(n)
        if m%2 == 0:
            ans = self.myPow(x,m//2)
            ans = ans * ans
        else:
            ans = x * self.myPow(x,m-1)
        
        if n < 0:
            return 1/ans
        return ans
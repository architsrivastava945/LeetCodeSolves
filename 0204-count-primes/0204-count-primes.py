import math
class Solution:
    def countPrimes(self, n: int) -> int:
        prime_no = 0
        is_prime = [False] * (n-2)
        for i in range(2, n):
            if not is_prime[i-2]:
                prime_no += 1
                for j in range(i-2, n-2, i):
                    is_prime[j] = True
        
        return prime_no
                    
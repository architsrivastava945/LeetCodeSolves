class Solution:
    def isPalindrome(self, x: int) -> bool:
        a,b = list(str(x)), list(str(x))
        b.reverse()
        if a == b:
            return True
        else:
            return False
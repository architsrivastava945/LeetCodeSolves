class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        if n != len(t):
            return False
        alpha = [0] * 26
        a = ord('a')
        for i in range(n):
            alpha[ord(s[i])-a] += 1
            alpha[ord(t[i])-a] -= 1
        for i in alpha:
            if i != 0:
                return False
        return True
        
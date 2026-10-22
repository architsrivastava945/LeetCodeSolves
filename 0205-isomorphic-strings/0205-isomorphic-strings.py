class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        if n != len(t):
            return False
        
        replace = {}

        for i in range(n):
            if s[i] in replace:
                if t[i] != replace[s[i]]:
                    return False
            else:
                if t[i] in replace.values():
                    return False
                else:
                    replace[s[i]] = t[i]

        return True
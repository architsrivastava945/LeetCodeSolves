class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        if n == 0:
            return []
        res = []
        n -= 1
        def solve(O,C,s):
            if O == 0 and C == 0:
                res.append(s + ')')
                return
            if O > 0:
                solve(O-1, C, s+'(')
            if C >= O:
                solve(O,C-1,s+')')
            
        solve(n,n,'(')
        return res

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(curr,stack,openn,close):
            if len(curr) == 2*n:
                if not stack:
                    res.append("".join(curr))
                return
            if openn < n:
                curr.append('(')
                stack.append('(')
                backtrack(curr,stack,openn+1,close)
                stack.pop()
                curr.pop()
            
            if close < n and stack:
                curr.append(')')
                stack.pop()
                backtrack(curr,stack,openn,close+1)
                stack.append('(')
                curr.pop()
        backtrack([],[],0,0)
        return res
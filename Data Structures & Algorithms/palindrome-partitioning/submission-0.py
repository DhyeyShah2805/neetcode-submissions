class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        curr = []
        def dfs(start):
            if start == len(s):
                result.append(curr[:])
                return
            for end in range(start, len(s)):
                substring = s[start: end+1]
                if substring == substring[::-1]:
                    curr.append(substring)

                    dfs(end + 1)
                    curr.pop()
        dfs(0)
        return result
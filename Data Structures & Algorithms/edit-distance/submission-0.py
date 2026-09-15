class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # recursion O(3^m+n)
        m,n = len(word1), len(word2)
        memo = {}
        # if n > m:
        #     return 0
        # def dfs(i,j):
        #     if i == m:
        #         return n - j
        #     if j == n:
        #         return m - i
        #     if word1[i] == word2[j]:
        #         return dfs(i+1, j+1)
        #     res = min(dfs(i+1,j), dfs(i,j+1))
        #     res = min(res, dfs(i+1,j+1))
        #     return res + 1
        # return dfs(0,0)
        def dfs(i,j):
            if i == m:
                return n - j
            if j == n:
                return m - i
            if (i,j) in memo:
                return memo[(i,j)]
            if word1[i] == word2[j]:
                memo[(i,j)] = dfs(i+1,j+1)
            else:
                res = min(dfs(i+1,j), dfs(i,j+1))
                res = min(res, dfs(i+1,j+1))
                memo[(i,j)] = res + 1
            return memo[(i,j)]
        return dfs(0,0)





            
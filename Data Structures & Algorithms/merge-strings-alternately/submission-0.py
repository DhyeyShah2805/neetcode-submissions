class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        left = 0
        right = 0
        res = []
        while left < len(word1) or right < len(word2):
            if left < len(word1):
                res.append(word1[left])
            if right < len(word2):
                res.append(word2[right])
            left += 1
            right += 1
        return "".join(res)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # T.C. = O(n * klogk), S.C. O(k) where n = len(s2), k = len(s1)
        sortS1 = sorted(s1)
        windowSize = len(s1)
        for i in range(len(s2) - windowSize + 1):
            substring = s2[i : i + windowSize]
            if sorted(substring) == sortS1:
                return True
        return False

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # T.C. O(n*m), S.C = O(n)
        # res = 0
        # for i in range(len(s)):
        #     char_set = set()
        #     for j in range(i,len(s)):
        #         if s[j] in char_set:
        #             break
        #         char_set.add(s[j])
        #     res = max(res, len(char_set))
        
        # return res

        char_set = set()
        left = 0
        length = 0
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            length = max(length, right - left + 1)
        return length
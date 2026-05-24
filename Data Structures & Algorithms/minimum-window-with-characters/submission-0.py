class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        if not t or not s:
            return ""
        dict_t = Counter(t)
        required_t = len(dict_t)
        l,r = 0,0
        # formed is used to keep track of how many unique characters in t are present in the current window in its desired frequency.
        formed = 0
        window = {}
        ans = float("inf"), None, None
        while r < len(s):
            char = s[r]
            window[char] = window.get(char,0) + 1
            if(char in dict_t and window[char] == dict_t[char]):
                formed += 1
            while l<=r and formed == required_t:
                char = s[l]
                if r - l + 1 < ans[0]:
                    ans = (r-l+1,l,r)
                window[char] -= 1
                if(char in dict_t and window[char] < dict_t[char]):
                    formed -= 1
                l += 1
            r += 1
        return "" if ans[0] == float('inf') else s[ans[1] : ans[2] + 1]
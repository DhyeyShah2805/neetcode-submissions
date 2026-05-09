class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for ch in nums:
            counter[ch] = counter.get(ch,0) + 1
        res = []
        for ch, cnt in counter.items():
            res.append([cnt,ch])
        res.sort()

        ans = []
        while len(ans) < k:
            ans.append(res.pop()[1])
        return ans

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # T.c. O(nlogn), SC O(n)
        # counter = {}
        # for ch in nums:
        #     counter[ch] = counter.get(ch,0) + 1
        # res = []
        # for ch, cnt in counter.items():
        #     res.append([cnt,ch])
        # res.sort()

        # ans = []
        # while len(ans) < k:
        #     ans.append(res.pop()[1])
        # return ans

        freq_map = {}
        for ch in nums:
            freq_map[ch] = freq_map.get(ch,0) + 1
        
        max_heap = []
        for ch,freq in freq_map.items():
            heapq.heappush(max_heap,(-freq,ch))
        
        result = []
        for _ in range(k):
            freq,ch = heapq.heappop(max_heap)
            result.append(ch)
        return result
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maping = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            maping[key].append(s)
        return list(maping.values())
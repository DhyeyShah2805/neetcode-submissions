class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # T.C. = O(m * nlogn)
        # s.c. = O(m*n)
        # maping = defaultdict(list)
        # for s in strs:
        #     key = ''.join(sorted(s))
        #     maping[key].append(s)
        # return list(maping.values())


        # T.C. = O(m*n)
        # S.C. = O(m*n)
        anagramMap = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for char in word:
                index = ord(char) - ord('a')
                count[index] += 1
            
            key = tuple(count)
            anagramMap[key].append(word)
        
        return list(anagramMap.values())
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0
        L = len(beginWord)
        # Build pattern buccket 
        patterns = defaultdict(list)
        for w in words:
            for i in range(L):
                patterns[w[:i] + '*' + w[i+1:]].append(w)
        visited = {beginWord}
        q = deque([(beginWord, 1)])
        while q:
            word, steps = q.popleft()
            if word == endWord:
                return steps
            for i in range(L):
                p = word[:i] + '*' + word[i+1:]
                for nei in patterns[p]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append((nei, steps+1))
                patterns[p] = []
       
        return 0

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = [[] for _ in range(numCourses)]
        indeg = [0] * numCourses
        for a,b in prerequisites:
            g[b].append(a)
            indeg[a] += 1
        q = deque()
        for n in range(numCourses):
            if indeg[n] == 0:
                q.append(n)
        finish = 0
        result = []
        while q:
            node = q.popleft()
            result.append(node)
            finish += 1
            for nei in g[node]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)
        if finish != numCourses:
            return []
        return result
        


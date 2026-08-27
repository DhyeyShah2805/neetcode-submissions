class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = [[] for _ in range(numCourses)]
        indeg = [0] * numCourses
        for a,b in prerequisites:
            g[b].append(a)
            indeg[a] += 1
        
        q = deque(c for c in range(numCourses) if indeg[c] == 0)
        taken = 0
        while q:
            u = q.popleft()
            taken += 1
            for next in g[u]:
                indeg[next] -= 1
                if indeg[next] == 0:
                    q.append(next)
        return taken == numCourses
        
        
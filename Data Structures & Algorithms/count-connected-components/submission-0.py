class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = set()
        count = 0
        for node in range(n):
            if node not in visited:
                count += 1
                q = deque([node])
                visited.add(node)
                while q:
                    curr = q.popleft()
                    for nei in adj[curr]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)
        return count
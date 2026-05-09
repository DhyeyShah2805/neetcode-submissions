class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_area = 0
        def bfs(r,c):
            queue = deque([(r,c)])
            grid[r][c] = 0
            area = 1
            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            while queue:
                x,y = queue.popleft()
                for dx,dy in directions:
                    nx,ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 0
                        queue.append((nx,ny))
                        area += 1
            return area
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area,bfs(r,c))
        return max_area
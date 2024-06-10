class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows,cols=len(grid),len(grid[0])
        visited=set()

        def dfs(i,j):
            if i<0 or i>=rows or j<0 or j>=cols or grid[i][j]==0 or (i,j) in visited:
                return 0
            visited.add((i,j))
            return 1+dfs(i+1,j)+dfs(i-1,j)+dfs(i,j+1)+dfs(i,j-1)
            
        area=0
        for i in range(rows):
            for j in range(cols):
                area=max(area,dfs(i,j))
        return area
                
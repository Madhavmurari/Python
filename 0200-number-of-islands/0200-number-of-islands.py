class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        num_island=0
        row,col=len(grid),len(grid[0])

        def dfs(i,j):
            if i<0 or i>=row or j<0 or j>=col or grid[i][j]!='1':
                return
            grid[i][j]='0' #mark as visited
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)

        for i in range(row):
            for j in range(col):
                if grid[i][j]=="1":
                    dfs(i,j)
                    num_island+=1
        return num_island
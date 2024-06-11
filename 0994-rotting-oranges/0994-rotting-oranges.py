class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=collections.deque()
        rows,cols=len(grid),len(grid[0])

        fresh,time=0,0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    fresh+=1
                if grid[r][c]==2:
                    q.append([r,c])

        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        while q and fresh>0:

            for i in range(len(q)):
                r,c=q.popleft()
                for dr,dc in directions:
                    row,col=r+dr,c+dc
                    if row in range(rows) and col in range(cols) and grid[row][col]==1:
                        grid[row][col]=2
                        q.append([row,col])
                        fresh-=1
            time+=1
        return time if fresh==0 else -1

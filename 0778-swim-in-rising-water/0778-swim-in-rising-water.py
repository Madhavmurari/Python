class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N=len(grid)
        visit=set()
        adjacent=[[0,1],[1,0],[-1,0],[0,-1]]
        minH=[[grid[0][0],0,0]]  #(time/height,row,col)
        visit.add((0,0))

        while minH:
            t,r,c=heapq.heappop(minH)
            if r==N-1 and c==N-1:
                return t
            for dr,dc in adjacent:
                neiR,neiC=r+dr,c+dc
                if (neiR<0 or neiR>=N or neiC<0 or neiC>=N or (neiR,neiC)in visit):
                    continue
                visit.add((neiR,neiC))
                heapq.heappush(minH,[max(t,grid[neiR][neiC]),neiR,neiC])

        
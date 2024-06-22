class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row=len(matrix)
        col=len(matrix[0])

        dp={}

        def dfs(i,j,preval):
            if i<0 or i==row or j<0 or j==col or matrix[i][j]<=preval:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]

            res=1
            res=max(res,1 + dfs(i+1,j,matrix[i][j]))
            res=max(res,1 + dfs(i-1,j,matrix[i][j]))
            res=max(res,1 + dfs(i,j+1,matrix[i][j]))
            res=max(res,1 + dfs(i,j-1,matrix[i][j]))
            dp[(i,j)]=res
            return res

        for r in range(row):
            for c in range(col):
                dfs(r,c,-1)
        return max(dp.values())

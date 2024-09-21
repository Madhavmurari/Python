# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         row=[1]*n

#         for i in range(m-1):
#             nrow=[1]*n
#             for j in range(n-2,-1,-1):
#                 nrow[j]=nrow[j+1]+row[j]
#             row=nrow
#         return row[0]


# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         dp = [[1]*n for _ in range(m)]
#         for i in range (1,m):
#             for j in range (1,n):
#                 dp[i][j] = dp[i-1][j] + dp[i][j-1]
#         return dp[m-1][n-1]

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Total number of movements required
        p=m+n-2
        q=min(m-1,n-1)

        res=1
        for i in range(q):
            res*=(p-i)
            res//=i+1
        return res
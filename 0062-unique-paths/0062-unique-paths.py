class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row=[1]*n

        for i in range(m-1):
            nrow=[1]*n
            for j in range(n-2,-1,-1):
                nrow[j]=nrow[j+1]+row[j]
            row=nrow
        return row[0]
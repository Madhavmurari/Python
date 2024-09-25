class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)

        # Initialize dp matrix with the same shape as the triangle
        dp = [[0] * (i + 1) for i in range(n)]
        dp[0][0] = triangle[0][0]

        # Fill the 0th column
        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] + triangle[i][0]

        # Fill the remaining elements in dp
        for i in range(1, n):
            for j in range(1, i + 1):
                if j == i:
                    dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]  # Diagonal elements
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]

        return min(dp[n - 1])  # The minimum path sum in the last row

        
class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # If the start or end is blocked, return 0
        if grid[0][0] == 1 or grid[m-1][n-1] == 1:
            return 0

        # Initialize dp array
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1  # Start position

        # Fill the dp table
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:  # If there's an obstacle
                    dp[i][j] = 0
                else:
                    if i > 0:
                        dp[i][j] += dp[i-1][j]  # Paths from above
                    if j > 0:
                        dp[i][j] += dp[i][j-1]  # Paths from the left

        return dp[m-1][n-1]  # Return the number of unique paths to the bottom-right corner

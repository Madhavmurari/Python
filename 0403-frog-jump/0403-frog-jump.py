class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False  # The frog must make a jump of exactly 1 to start.

        # Initialize a dictionary where each stone points to a set of possible jump lengths
        dp = {stone: set() for stone in stones}
        dp[0].add(0)  # The first stone can be reached with a jump of 0 units.

        for stone in stones:
            for k in dp[stone]:  # For each possible jump length k that can reach this stone
                # Try jumping k-1, k, k+1 units to the next stones
                for step in [k - 1, k, k + 1]:
                    if step > 0 and (stone + step) in dp:  # Ensure positive step and valid stone
                        dp[stone + step].add(step)

        # Check if there are any valid jump lengths that can reach the last stone
        return len(dp[stones[-1]]) > 0

     
        
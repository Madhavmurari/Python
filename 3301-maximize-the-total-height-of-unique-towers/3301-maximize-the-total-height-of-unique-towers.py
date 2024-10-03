class Solution:
    def maximumTotalSum(self, nums: List[int]) -> int:
        nums.sort()  
        maxH = nums[-1]  
        n = len(nums)
        total_sum = maxH  # Add the largest height to the sum
        
        # If the number of towers is greater than the max possible height, it's impossible
        if n > maxH:
            return -1
        
        # Loop through from the second-to-last tower down to the first
        for i in range(n-2, -1, -1):
            # Assign the next smaller height to the current tower
            maxH = min(maxH - 1, nums[i])
            
            # If we can't assign a valid height, return -1
            if maxH <= 0:
                return -1
            
            total_sum += maxH  # Add the valid height to the total sum
            
        return total_sum

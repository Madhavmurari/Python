class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n  # In case k is larger than the length of nums
    
        nums[:] = nums[-k:]+ nums[:-k]  # Reassign in-place
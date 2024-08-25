class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        
        def argmin(array):
            min=array[0]
            index=0
            for i in range(1,len(array)):
                if min>array[i]:
                    min=array[i]
                    index=i
            return index

        for i in range(k):
            i=argmin(nums)
            nums[i]=nums[i]*multiplier
        return nums

        
        
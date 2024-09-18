class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
      
        mapp={}
        for num in nums:
            mapp[num]=1+mapp.get(num,0)

        idx=0
        
        for i in range(3):
            freq=mapp.get(i,0)
            nums[idx:idx+freq]=[i]*freq
            idx+=freq
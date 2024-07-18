class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

         
        def maxHeappop(heap):
            return -heapq.heappop(heap) 

        nums=[-i for i in nums]
        heapq.heapify(nums)

        res=0
        for i in range(k):
            res=maxHeappop(nums)
        return res
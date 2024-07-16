class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        def maxHeappush(heap,val):
            heapq.heappush(heap,-val)

        def maxHeappop(heap):
            return -heapq.heappop(heap)
        

        maxheap=[-num for num in stones]
        heapq.heapify(maxheap)

        while len(maxheap)>1:
            x=maxHeappop(maxheap)
            y=maxHeappop(maxheap)

            if x!=y:
                
                maxHeappush(maxheap,x-y)
                   
        return maxHeappop(maxheap) if maxheap else 0

            




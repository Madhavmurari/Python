# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         mapp={}
#         freq=[[] for i in range(len(nums)+1)]

#         for n in nums:
#             mapp[n]=1+mapp.get(n,0)

#         for n,c in mapp.items():
#             freq[c].append(n)
        
#         res=[]

#         for i in range(len(nums),0,-1):
#             for n in freq[i]:
#                 res.append(n)
#                 if len(res)==k:
#                     return res

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter={}
        heap=[]

        for n in nums:
            counter[n]=1+counter.get(n,0)

        for key,val in counter.items():
            heapq.heappush(heap,(-val,key))
        
        res=[]
        while len(res)<k:
            res.append(heapq.heappop(heap)[1])
        return res


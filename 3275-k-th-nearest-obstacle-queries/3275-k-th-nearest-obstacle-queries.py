class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        import heapq
        res=[]
        H=[]    #Heap

        for x,y in queries:
            heapq.heappush(H,-(abs(x)+abs(y)))

            while len(H)>k:
                heapq.heappop(H)
            if len(H)<k:
                res.append(-1)
            else:
                res.append(-H[0])
        return res


        
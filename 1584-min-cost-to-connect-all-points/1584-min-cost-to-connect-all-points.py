class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)

        adj={i:[] for i in range(n)}  #[cost,node/point]
        for i in range(n):
            x1,y1=points[i]
            for j in range(n):
                x2,y2=points[j]
                dist=abs(x1-x2)+abs(y1-y2)
                adj[i].append([dist,j])
                adj[j].append([dist,i])
        #prims

        res=0
        visit=set()
        minH=[[0,0]]  #[Cost,point/node]

        while len(visit)<n:
            cost,i=heapq.heappop(minH)
            if i in visit:
                continue
            res+=cost
            visit.add(i)
            for neiCost,nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minH,[neiCost,nei])
        return res
        
from sortedcontainers import SortedList
class Solution:
    def EMN(self,s,l,r):  #Erage Middle node
        start=s.bisect_left(l)
        end=s.bisect_right(r)
        del s[start:end]

    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        s=SortedList(range(n))
        res=[]
        for x,y in queries:
            self.EMN(s,x+1,y-1)
            res.append(len(s)-1)
        return res



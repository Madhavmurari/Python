class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        
        mapp={i:[] for i in range(n)}
        
        for u in range(n-1):
            mapp[u].append(u+1)

        res=[]
        for u,v in queries:
            mapp[u].append(v)
            visit=set()
            visit.add(0)
            q=deque()
            q.append((0,0))

            while q:
                node,dst=q.popleft()
                if node==n-1:
                    res.append(dst)

                for v in mapp[node]:
                    if v not in visit:
                        q.append((v,dst+1))
                        visit.add(v)
        return res

# from collections import deque
# from typing import List

# class Solution:
#     def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        
#         mapp = {i: [] for i in range(n)}
        
#         for u in range(n-1):
#             mapp[u].append(u + 1)
        
#         results = []
        
#         def bfs() -> int:
#             visit = set()
#             q = deque([(0, 0)])  # (current node, distance from start)
#             while q:
#                 node, dst = q.popleft()
#                 if node == n - 1:
#                     return dst
#                 for v in mapp[node]:
#                     if v not in visit:
#                         visit.add(v)
#                         q.append((v, dst + 1))
#             return -1  # Return -1 if there's no path to n-1
        
#         for u, v in queries:
#             mapp[u].append(v)
#             shortest_path_length = bfs()
#             results.append(shortest_path_length)
        
#         return results





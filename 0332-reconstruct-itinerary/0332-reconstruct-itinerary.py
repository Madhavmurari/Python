class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        adj=defaultdict(deque)
        for src,dist in sorted(tickets):
            adj[src].append(dist)

        res=[]
        def dfs(src):
            while adj[src]:
                next_dist=adj[src].popleft()
                dfs(next_dist)
            res.append(src)
        dfs("JFK")
        return res[::-1]

        
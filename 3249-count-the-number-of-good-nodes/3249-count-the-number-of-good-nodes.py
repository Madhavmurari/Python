class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        ans=0
        adj_list=collections.defaultdict(list)

        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        def go(node,parent):
            total=1
            s=set()
            for v in adj_list[node]:
                if v!=parent:
                    c=go(v,node)
                    total+=c
                    s.add(c)
            if len(s)==1 or len(s)==0:
                nonlocal ans
                ans+=1
            return total
        go(0,-1)
        return ans
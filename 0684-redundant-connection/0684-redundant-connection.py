class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        p=[]
        for i in range(len(edges)+1):
            p.append(i)
        def find(src):
            if p[src]==src:
                return src
            return find(p[src])
        
        for u,v in edges:
            pu=find(u)
            pv=find(v)
            if pu==pv:
                return [u,v]
            p[pu]=pv
        
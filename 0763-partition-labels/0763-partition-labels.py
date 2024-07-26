class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        start,end = 0,0
        indexMap = defaultdict(int)

        for i,c in enumerate(s):
            indexMap[c]=i

        for i,c in enumerate(s):
            end = max(end,indexMap[c])
            if i==end:
                res.append(end-start+1)
                start=end+1
        return res
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda x:x[1])
        n=len(intervals)
        count=0
        pre_node=float('-inf')

        for start,end in intervals:
            if start>=pre_node:
                pre_node=end
                
            else:
                count+=1
        return count
        
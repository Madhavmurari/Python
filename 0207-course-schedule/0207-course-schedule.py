class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mapp={i:[] for i in range(numCourses)}

        for dest,src in prerequisites:
            mapp[src].append(dest) 

        visit=set()

        def dfs(src):
            if src in visit:
                return False
            if mapp[src]==[]:
                return True 

            visit.add(src)

            for destination in mapp[src]:
                if not dfs(destination):
                    return False
            visit.remove(src)
            mapp[src]=[]
            return True
        
        for destination in range(numCourses):
            if not dfs(destination):
                return False
        return True

        
        
        

        


        
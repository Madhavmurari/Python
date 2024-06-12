class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        map={i:[] for i in range(numCourses)}

        for dest,src in prerequisites:
            map[src].append(dest) 
        
        status=[0]*numCourses

        def dfs(course):
            if status[course]==1:  # Found a cycle
                return False
            if status[course]==2:  # Already visited node, no cycle from this node
                return True 
            status[course]=1

            for neighbor in map[course]:
                if not dfs(neighbor):
                    return False
            status[course]=2  # Mark the course as completely visited
            return True

        for course in range(numCourses):  # Perform DFS for each course
            if not dfs(course):
                return False
        return True

        

        


        
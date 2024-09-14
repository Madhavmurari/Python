class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        if not grid or not grid[0]:
            return False
        m,n = len(grid), len(grid[0])

        health=health-grid[0][0]
        if health<0:
            return False
        
        direction=[(-1,0),(1,0),(0,-1),(0,1)]

        visited=[[-1 for _ in range(n)] for _ in range(m)]
        visited[0][0]=health

        queue=deque()
        queue.append((0,0,health))

        while queue:
            i,j,curr_health=queue.popleft()

            if i==m-1 and j==n-1:
                return True
            
            for dx,dy in direction:
                ni,nj=i+dx,j+dy

                if 0 <= ni < m and 0 <= nj < n:
                    # Calculate new health
                    new_health = curr_health - grid[ni][nj]

                    if new_health >=1 and new_health > visited[ni][nj]:
                        visited[ni][nj] = new_health
                        queue.append((ni, nj, new_health))
        return False


        

        

        
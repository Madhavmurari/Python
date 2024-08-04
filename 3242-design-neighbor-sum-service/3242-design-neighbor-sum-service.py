class neighborSum:

    def __init__(self, grid: List[List[int]]):
       self.grid=grid
       self.l=len(grid)
       self.position={grid[i][j]:(i,j) for i in range(self.l) for j in range(self.l)} 

    def adjacentSum(self, value: int) -> int:
        i,j=self.position[value]
        adjacent =[(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
        sum=0
        for a,b in adjacent:
            if 0<=a<self.l and 0<=b<self.l:
                sum+=self.grid[a][b]
        return sum

    def diagonalSum(self, value: int) -> int:
        if value not in self.position:
            return 0
        i,j=self.position[value]
        adjacent =[(i+1,j+1),(i-1,j+1),(i+1,j-1),(i-1,j-1)]
        sum=0
        for a,b in adjacent:
            if 0<=a<self.l and 0<=b<self.l:
                sum+=self.grid[a][b]
        return sum
        


# Your neighborSum object will be instantiated and called as such:
# obj = neighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)
class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:

        currP = [0, 0]
        mapp = {"UP": [-1,0], "DOWN": [1,0], "RIGHT": [0,1], "LEFT": [0,-1]}
        for command in commands:
            i, j = mapp[command]
            currP = [currP[0] + i, currP[1] + j]
        return currP[0] * n + currP[1]
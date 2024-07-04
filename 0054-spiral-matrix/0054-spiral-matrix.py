class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        # return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])

        res=[]
        left,right=0,len(matrix[0])
        top,bottom =0,len(matrix)

        while left < right and top < bottom:

            for i in range(left,right):
                res.append(matrix[top][i])
            top+=1

            for j in range(top,bottom):
                res.append(matrix[j][right-1])
            right-=1

            if not (left < right and top < bottom):
                break

            for i in range(right-1,left-1,-1):
                res.append(matrix[bottom-1][i])
            bottom-=1

            for j in range(bottom-1,top-1,-1):
                res.append(matrix[j][left])
            left+=1


        return res
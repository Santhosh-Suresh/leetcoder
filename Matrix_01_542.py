import numpy as np
from typing import List

class Solution:
    def updateMatrix(self , matrix: List[List[int]]) -> object:
        a = np.array(matrix)
        return (self.updateNumpyArray(a)).tolist()

    def updateNumpyArray(self , matrix: np.ndarray) -> np.ndarray:
        m = matrix.shape[0]
        if m == 0:
            return matrix
        matrix[0] = self.single_row(matrix[0])
        if m == 1:
            return matrix
        for i in range(1, m):
            row = self.single_row(matrix[i])
            new_upper = row + np.array(range(i,0,-1)).reshape(-1,1)
            matrix[0:i]=np.minimum(matrix[0:i], new_upper)
            matrix[i] = np.minimum(row, matrix[i-1]+1)

        return matrix

    def single_row(self , row: np.ndarray) -> np.ndarray:
        if (row > 0).all():
            return np.zeros( row.shape[0] ) + 10001
        latest_0= first_0 = np.where(row==0)[0][0]
        ans = row
        ans[:first_0] =  range(first_0,0,-1)
        for i in range(first_0+1,row.shape[0]):
            if row[i]==0:
                if latest_0 != (i-1):
                    ans[0:i] = np.minimum(ans[0:i],range(i,0,-1))
                latest_0 = i
            if row[i]==1:
                ans[i] = i - latest_0
        return ans

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        found_zero = []
        rows = len(matrix)
        cols = len(matrix[0]) 
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    found_zero.append([i,j])
                    
        for r , c in found_zero:
            for col in range(cols):
                matrix[r][col] = 0
            for row in range(rows):
                matrix[row][c] = 0
                            
        return f"elements found at postion :{found_zero}, matrix : {matrix}"
    
matrix = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

print(Solution().setZeroes(matrix))  # Output: [[1,0,1],[0,0,0],[1,0,1]]
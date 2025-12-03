class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        result = []
        rows = len(matrix)
        cols = len(matrix[0])
        
        # Step 1: Traverse top row
        for c in range(cols):
            result.append(matrix[0][c])

        # Step 2: Traverse right column (downwards)
        for r in range(1, rows):
            result.append(matrix[r][cols - 1])

        # Step 3: Traverse bottom row (right to left)
        for c in range(cols - 2, -1, -1):
            result.append(matrix[rows - 1][c])

        # Step 4: Traverse left column (bottom to top)
        for r in range(rows - 2, 0, -1):
            result.append(matrix[r][0])
        
        if rows > 2 and cols > 2:
            result.append(matrix[1][1])
        
        return result


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(Solution().spiralOrder(matrix))  

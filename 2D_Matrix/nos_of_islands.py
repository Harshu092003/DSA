class Solution:
    def nos_of_island(self, matrix: list[list[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        count = 0
        
        def dfs(r, c):
            # boundary or water or visited
            if r < 0 or r >= rows or c < 0 or c >= cols or matrix[r][c] != 'L':
                return
            
            matrix[r][c] = '#'  # mark visited
            
            # explore all 8 directions
            directions = [
                (1, 0), (-1, 0), (0, 1), (0, -1),  # up/down/left/right
                (1, 1), (-1, -1), (1, -1), (-1, 1) # diagonals
            ]
            
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 'L':
                    count += 1
                    dfs(i, j)
        
        return count


# Test
matrix = [
    ['L', 'L', 'W', 'W', 'W'],
    ['W', 'L', 'W', 'W', 'L'],
    ['L', 'W', 'W', 'L', 'L'],
    ['W', 'W', 'W', 'W', 'W'],
    ['L', 'W', 'L', 'L', 'W']
]

print(Solution().nos_of_island(matrix))

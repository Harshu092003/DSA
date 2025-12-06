class Solution:
    def replace_x_and_zero(self, matrix: list[list[str]]) -> list[list[str]]:
        rows = len(matrix)
        cols = len(matrix[0])
        
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or matrix[r][c] != 'O':
                return
            
            matrix[r][c] = 'T'  # mark visited safe O
            
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Step 1: Mark boundary connected 'O'
        for i in range(rows):
            if matrix[i][0] == 'O':
                dfs(i, 0)
            if matrix[i][cols - 1] == 'O':
                dfs(i, cols - 1)

        for j in range(cols):
            if matrix[0][j] == 'O':
                dfs(0, j)
            if matrix[rows - 1][j] == 'O':
                dfs(rows - 1, j)

        # Step 2: Convert remaining O → X and T → O
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 'O':
                    matrix[r][c] = 'X'  # surrounded so replace
                elif matrix[r][c] == 'T':
                    matrix[r][c] = 'O'  # safe, restore

        return matrix

matrix = [
    ['X', 'O', 'X', 'X', 'X', 'X'], 
    ['X', 'O', 'X', 'X', 'O', 'X'],
    ['X', 'X', 'X', 'O', 'O', 'X'],
    ['O', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'O', 'X', 'O'],
    ['O', 'O', 'X', 'O', 'O', 'O']
]

result = Solution().replace_x_and_zero(matrix)
for row in result:
    print(row)

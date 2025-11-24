class Solution:
    def diagonal_traverse(self, matrix: list[list[int]]) -> list[int]:
        if not matrix or not matrix[0]:
            return []

        result = []
        rows = len(matrix)
        cols = len(matrix[0])

        for d in range(rows + cols - 1):
            for i in range(rows):
                for j in range(cols):
                    if i+j == d:
                        result.append(matrix[i][j])

        return result

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(Solution().diagonal_traverse(matrix))
# Output: [1, 2, 4, 3, 5, 7, 6, 8, 9]
  
class Solution:
    def rectangles_of_O_and_X(self, m: int, n: int) -> list[list[str]]:
        matrix = []
        for i in range(m):
            row =[]
            for j in range(n):
                if i== 0 or j ==0 or i == m-1 or j== n-1:
                    row.append('X')
                elif i ==1 or j ==1 or i == m-2 or j == n-2 :
                    row.append('O')
                else :
                    row.append('X')
            matrix.append(row)

        return matrix
            

print(Solution().rectangles_of_O_and_X(6,7))

# Input:  m = 6, n = 7
# Output: Following matrix
# X X X X X X X
# X 0 0 0 0 0 X
# X 0 X X X 0 X
# X 0 X X X 0 X
# X 0 0 0 0 0 X
# X X X X X X X 


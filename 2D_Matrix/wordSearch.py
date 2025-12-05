class Solution:
    def word_search(self, board: list[list[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        
        def search(r, c, idx):
            if idx == len(word):  
                return True
            
            # Boundary or mismatch
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[idx]:
                return False
            
            temp = board[r][c]
            board[r][c] = '#'  # mark visited
            
            print(f"Visiting ({r},{c}) -> matched '{temp}'")

            # Explore 4 directions
            found = (
                search(r + 1, c, idx + 1) or
                search(r - 1, c, idx + 1) or
                search(r, c + 1, idx + 1) or
                search(r, c - 1, idx + 1)
            )
            
            board[r][c] = temp  # restore cell after search
            return found

        # Try starting DFS from each cell
        for i in range(rows):
            for j in range(cols):
                if search(i, j, 0):
                    return True
        
        return False


# Test
board = [
    ["A","B","C","E"],
    ["S","F","C","S"],
    ["A","D","E","E"]
]
word = "ABCCED"

print(Solution().word_search(board, word))

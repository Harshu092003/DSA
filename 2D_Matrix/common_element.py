class Solution:
    def common_element(self , matrix : list[list[int]]) -> int :
        rows  = len(matrix)
        cols = len(matrix[0])
        ele = set(matrix[0])
        my_list = list(ele)
        print(my_list[0])
        for i in my_list:
            for j in range(1, rows):
                if i not in matrix[j]:
                    break
            else:
                return i  # Found common element
                
        return 
    
matrix = [
    [1, 2, 5, 2],
    [2, 3, 4, 5],
    [3, 4, 5, 6],
    [4, 5, 6, 7]
]

print(Solution().common_element(matrix))  # Output: 4
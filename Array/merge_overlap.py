class Solution:
    def merge_overlap(self, arr: list[list[int]]) -> list[list[int]]:
        arr.sort()
        result = []
        start, end = arr[0]

        for i in range(1, len(arr)):
            next_start, next_end = arr[i]

            if next_start <= end:  # overlap
                end = max(end, next_end)
            else:
                result.append([start, end])
                start, end = next_start, next_end

        result.append([start, end])  # add the last interval
        return result


arr = [[1, 3], [2, 4], [6, 8], [9, 10]]
print(Solution().merge_overlap(arr))

arr = [[7, 8], [1, 5], [2, 4], [4, 6]]
print(Solution().merge_overlap(arr))

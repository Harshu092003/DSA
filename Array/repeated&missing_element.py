class Solution:
    def repeated_missing(self, arr: list[int]) -> int:
        found = set()

        for index, element in enumerate(arr):
            if element in found:
                A = index
                print(f" duplicate {element} is at {A} position")
            else:
                found.add(element)

        arr.sort()  # [1,2,3,3,5]
        i = 0
        missing = 1
        while i < len(arr) - 1:
            if arr[i] != missing:
                mis = missing
                return print(f"{mis} is missing in given list")
            else:
                i += 1
            missing += 1


arr = [3, 1, 2, 5, 3]
Solution().repeated_missing(arr)

def combinations(arr, r, start=0, curr=[]):
    # Base case: if current combination size == r → print it
    if len(curr) == r:
        print(*curr)
        return
    
    # Recursive case: pick each element starting from 'start'
    for i in range(start, len(arr)):
        # Include arr[i] and move forward
        combinations(arr, r, i + 1, curr + [arr[i]])

# Example
arr = [1, 2, 3, 4,5]
r = 2
combinations(arr, r)


# recursion uses Call stack for performing the repetive calls ,that why 1 ,finishes its all combination ,then only i + 1 happen to 2 ,like this it goes forward.
# []
# ├── [1]
# │   ├── [1,2]
# │   ├── [1,3]
# │   ├── [1,4]
# │   └── [1,5]
# ├── [2]
# │   ├── [2,3]
# │   ├── [2,4]
# │   └── [2,5]
# ├── [3]
# │   ├── [3,4]
# │   └── [3,5]
# └── [4]
#     └── [4,5]

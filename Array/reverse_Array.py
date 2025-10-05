# Reverse an array using for loop

arr = [10, 20, 30, 40, 50]
n = len(arr)

print("Original array:", arr)
print("Reversed array:")

for i in range(0,n,-1):   # from last index to 0
    print(arr[i], end=" ")  # print the element at index i-1

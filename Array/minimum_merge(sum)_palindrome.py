class Solution():
    def min_merge(self,arr : list[int]) -> int :
        ans = 0
        i , j = 0 , len(arr) - 1
        while i <= j :
            if arr[i] == arr[j] :
                i += 1
                j -= 1
            elif arr[i] > arr[j]:
                j -= 1
                arr[j] += arr[j+1] 
                ans += 1
            else:
                i += 1
                arr[i] += arr[i-1]
                ans += 1
        return  ans


arr = [15,4,15]
print(Solution().min_merge(arr))
print(arr)

arr = [1,4,5,1]
print(Solution().min_merge(arr))
print(arr)


arr = [1, 4, 5, 9, 1]
print(Solution().min_merge(arr))
print(arr)


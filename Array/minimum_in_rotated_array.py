class Solution:
    def minRotated(self,arr : list[int]) -> int :
        left , right = 0, len(arr) - 1 
        while left < right :
            mid = (left + right) // 2
            if arr[mid] > arr[right] :
                left = mid + 1 
            else : 
                right = mid
        return arr[left]

arr = [4,5,6,1,2,3]
print(len(arr))
print(Solution().minRotated(arr))
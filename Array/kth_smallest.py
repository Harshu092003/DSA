class Solution:
    def Kth_largest(self, nums: list[int], k: int) -> int:
        nums.sort()  # [1,2,2,3,4,4,5]
        return nums[k]


nums = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
k = int(input("Enter element to search :"))
print(Solution().Kth_largest(nums, k))

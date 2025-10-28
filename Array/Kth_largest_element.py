class Solution:
    def Kth_largest(self, nums: list[int], k: int) -> int:
        nums.sort()  # [1,2,2,3,4,4,5]
        return nums[len(nums) - k]


nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = int(input("Enter element to search :"))
print(Solution().Kth_largest(nums, k))

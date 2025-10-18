from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            # Width between lines
            width = right - left
            # Height of container is min of both lines
            h = min(height[left], height[right])
            # Calculate area
            area = width * h
            max_area = max(max_area, area)

            # Move the smaller height pointer inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


# Example Runs
print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))  # Output: 49
print(Solution().maxArea([1,1]))                # Output: 1

class Solution(object):
    def maxArea(self, height):
        """
        Two Pointer Pattern (Opposite Direction)

        Problem:
        Given an array 'height', find two lines that together with the x-axis
        form a container that holds the maximum amount of water.

        Approach:
        - Use two pointers:
            left → start of array
            right → end of array

        - At each step:
            1. Calculate area:
               area = min(height[left], height[right]) * (right - left)

            2. Update maximum area

            3. Move the pointer with smaller height:
               → because water is limited by smaller height

        Key Idea:
        Move the smaller height pointer to try to find a bigger boundary

        Why?
        - Moving the taller one won't increase area
        - Only moving smaller one may increase height

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            # Calculate current area
            width = right - left
            h = min(height[left], height[right])
            area = width * h

            # Update max
            max_area = max(max_area, area)

            # Move the smaller height pointer
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


# Test
sol = Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7]))  # Output: 49
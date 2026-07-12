class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            # Calculate the current area
            # Area = width * min_height
            width = right - left
            current_height = min(height[left], height[right])
            current_area = width * current_height
            
            # Update max_area if current is larger
            max_area = max(max_area, current_area)
            
            # Move the pointer pointing to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_area

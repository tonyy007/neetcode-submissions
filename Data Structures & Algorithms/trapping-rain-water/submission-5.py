class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 1, len(height) - 2
        rain = 0
        maxLeft = height[left - 1]
        maxRight = height[right + 1]
        while left <= right:
            if maxLeft < maxRight:
                rain += max(0, maxLeft - height[left] )
                left += 1
                maxLeft = max(maxLeft, height[left - 1])
            elif maxRight <= maxLeft:
                rain += max(0, maxRight - height[right])
                right -= 1
                maxRight = max(maxRight, height[right + 1])
            #print(rain, left, maxLeft, right, maxRight)
        return rain
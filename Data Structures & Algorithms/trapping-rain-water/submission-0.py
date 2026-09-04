class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)

        minimum = [0] * len(height)

        for i in range(1, len(height)):
            maxLeft[i] = max(maxLeft[i - 1], height[i - 1])

        for j in range(len(height)- 2, -1, -1):
            maxRight[j] = max(maxRight[j + 1], height[j + 1])

        for i in range(0, len(minimum)):
            minimum[i] = min(maxLeft[i], maxRight[i])
        #print(maxRight)
        water = 0
        for i in range(len(height)):
            water += max(0, minimum[i] - height[i])
        return water
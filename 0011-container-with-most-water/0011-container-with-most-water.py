class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        maxArea = 0

        while i < j:
            h = min(height[i], height[j])
            w = j - i
            area = h * w

            maxArea = max(maxArea, area)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return maxArea
        
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        for i in range(len(heights)):
            for j in range(len(heights)-1,-1,-1):
                length = min(heights[i], heights[j])
                width = j - i
                area_found = length * width
                max_area = max(max_area, area_found)
        return max_area
            
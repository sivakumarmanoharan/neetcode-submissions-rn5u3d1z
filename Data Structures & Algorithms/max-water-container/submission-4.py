class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        max_area = 0
        while i < len(heights)-1:
            j = len(heights) - 1
            while j > i:
                length = min(heights[i], heights[j])
                width = j - i
                area_found = length * width
                max_area = max(max_area, area_found)
                j -= 1
            i += 1
        return max_area
            
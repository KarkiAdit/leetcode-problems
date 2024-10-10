# 11. Container With Most Water

# Unoptimized O(n^2) solution
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_possible = 0
        for j in range(len(height) - 1, -1, -1):
            jth_area = 0
            b = 1
            for k in range(j - 1, -1, -1):
                curr_max_area = min(height[k], height[j]) * b
                jth_area = max(curr_max_area, jth_area)
                b += 1
            max_possible = max(jth_area, max_possible)
        return max_possible
                

                

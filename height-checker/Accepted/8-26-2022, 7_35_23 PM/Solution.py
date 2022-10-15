// https://leetcode.com/problems/height-checker

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        z=sorted(heights)
        count=0
        for i in range (len(heights)):
            if (z[i]!=heights[i]):
                count=count+1
        return count
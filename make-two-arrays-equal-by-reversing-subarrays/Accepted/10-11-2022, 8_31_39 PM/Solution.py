// https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        for i in target:
            if i not in arr:
                return False
            
        target.sort()
        arr.sort()
        if target==arr:
            return True
        
        return False
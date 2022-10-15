// https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        value=arr[1]-arr[0]
        for i in range(len(arr)-1):
            
            if value!=arr[i+1]-arr[i]:
                return False
            
        return True
            
            
            
        
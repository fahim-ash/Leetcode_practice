// https://leetcode.com/problems/power-of-two

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==1:
            return True
        elif n<1:
            return False
        
        return isPowerOfTwo(n/2)
            
        
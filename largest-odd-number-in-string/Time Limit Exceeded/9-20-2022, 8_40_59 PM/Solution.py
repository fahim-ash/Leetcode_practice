// https://leetcode.com/problems/largest-odd-number-in-string

class Solution:
    def largestOddNumber(self, num: str) -> str:
        z=0
        for i in range(len(num)):
            i=i+1
            
            if (int(num[:i])>z) and int(num[:i])%2!=0:
                z=int(num[:i])
                
                
        if z==0:
            return ""
        else:
            return str(z)
            
            
        
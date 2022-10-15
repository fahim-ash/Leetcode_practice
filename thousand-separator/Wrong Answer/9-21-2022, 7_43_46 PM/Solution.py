// https://leetcode.com/problems/thousand-separator

class Solution:
    def thousandSeparator(self, n: int) -> str:
        
        if len(str(n))>3:
            n=n/1000
            
        return str(n)
        
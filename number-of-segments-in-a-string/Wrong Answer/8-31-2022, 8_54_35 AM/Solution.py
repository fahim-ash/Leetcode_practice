// https://leetcode.com/problems/number-of-segments-in-a-string

class Solution:
    def countSegments(self, s: str) -> int:
        s = s.strip()       
        length = 0
        for i in range(len(s)):
           
            if s[i] == " ":
                length = 0
            else:
                length += 1  
        return length
        
        
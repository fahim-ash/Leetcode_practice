// https://leetcode.com/problems/length-of-last-word

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        s = s.strip()   
        print(s)
        length = 0
        for i in range(len(s)):
            
            if s[i] == " ":
                length = 0
            else:
                length += 1   
        return length
        
        
// https://leetcode.com/problems/length-of-last-word

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        s = s.strip()   
        print(s)
        length = 0
        for i in range(len(s)-1,-1,-1):
            
            if s[i] == " ":
                break
            else:
                length += 1   
        return length
        
        
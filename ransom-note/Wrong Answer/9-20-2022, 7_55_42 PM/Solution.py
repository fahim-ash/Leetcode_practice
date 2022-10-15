// https://leetcode.com/problems/ransom-note

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in range(len(magazine)):
            print(magazine[:i],ransomNote)
            if ransomNote== magazine[:i]:
                return True
            
            
        
            
            
        
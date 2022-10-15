// https://leetcode.com/problems/ransom-note

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in range(len(magazine)):
            print(magazine[:i+1],ransomNote[::-1])
            if ransomNote== magazine[:i+1] or ransomNote[::-1]== magazine[:i+1]:
                return True
            
            
        
            
            
        
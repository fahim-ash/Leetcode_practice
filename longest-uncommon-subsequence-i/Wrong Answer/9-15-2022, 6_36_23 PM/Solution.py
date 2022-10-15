// https://leetcode.com/problems/longest-uncommon-subsequence-i

class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a==b:
            return -1
        count=0 
        for i in a:
            if i not in b:
                count+=1
                
        return count
        
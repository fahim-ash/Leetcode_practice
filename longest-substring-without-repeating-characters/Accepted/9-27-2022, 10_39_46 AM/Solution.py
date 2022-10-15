// https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        z=set()
        l=0
        res=0
        for i in range(len(s)):
            while s[i] in z:
                z.remove(s[l])
                l+=1
            z.add(s[i])
            res=max(res,i-l+1)
            
                
        return res
        
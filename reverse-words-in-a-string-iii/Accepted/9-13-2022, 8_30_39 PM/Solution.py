// https://leetcode.com/problems/reverse-words-in-a-string-iii

class Solution:
    def reverseWords(self, s: str) -> str:
        word=""
        m=s.split(" ")
        for i in m:
            k=i[::-1]
            word+=k+" "
        
        
        return (word[:-1])
        
            
        
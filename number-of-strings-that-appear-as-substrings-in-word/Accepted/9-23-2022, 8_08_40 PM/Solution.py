// https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        s={}
        for i in range(len(word)):
            for j in range(i+1,len(word)+1):
                
                    s[word[i:j]]=1
        count=0 
        
        for i in patterns:
            if i in s:
                count+=1
                
        return count
// https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        z=[]
        for i in range(len(word)):
            for j in range(i+1,len(word)+1):
                if word[i:j] not in z:
                    z.append(word[i:j])
        count=0 
        
        for i in patterns:
            if i in z:
                count+=1
                
        return count
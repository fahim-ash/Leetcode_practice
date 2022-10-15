// https://leetcode.com/problems/count-common-words-with-one-occurrence

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
  
        s={}
        m={}
        for i in range(len(words1)):
            count=1
            if words1[i] in s:
                count+=1
                
            s[words1[i]]=count
        for i in range(len(words2)):
            count=1
            if words2[i] in m:
                count+=1
                
            m[words2[i]]=count
        r=0   
        for i in s:
            if i in m:
                if s[i]==m[i]:
                    r+=1
                    
        return r
                    
                
        
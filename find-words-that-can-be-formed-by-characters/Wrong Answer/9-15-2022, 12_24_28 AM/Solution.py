// https://leetcode.com/problems/find-words-that-can-be-formed-by-characters

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count=0
        for i in range(len(words)):
            for j in words[i]:
                if j not in chars:
                    words[i]=0
            
                    
        for i in words:
            if i!=0:
                for j in i :
                    count+=1
                    
        return count
                    
        
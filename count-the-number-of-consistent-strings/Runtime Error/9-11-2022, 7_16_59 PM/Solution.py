// https://leetcode.com/problems/count-the-number-of-consistent-strings

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
       
        count=0
        while len(words)>count:
            for k in words:
                for m in k:
                    if m not in allowed:
                        words.remove(k)
            count+=1
                    
        print(words)
        return len(words)
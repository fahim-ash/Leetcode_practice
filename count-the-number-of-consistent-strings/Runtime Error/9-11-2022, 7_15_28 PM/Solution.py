// https://leetcode.com/problems/count-the-number-of-consistent-strings

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        k={}
        count=0
        for i in words:
            for k in words:
                for m in k:
                    if m not in allowed:
                        words.remove(k)
                    
        print(words)
        return len(words)
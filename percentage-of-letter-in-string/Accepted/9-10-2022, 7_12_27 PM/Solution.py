// https://leetcode.com/problems/percentage-of-letter-in-string

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        z=[]
        for i in s:
            z.append(i) 
        
        return (z.count(letter) * 100 )// len(z)
        
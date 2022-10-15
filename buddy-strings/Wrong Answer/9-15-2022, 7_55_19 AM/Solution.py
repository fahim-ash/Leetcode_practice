// https://leetcode.com/problems/buddy-strings

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
      
        return ( s[-1]+s[-2]==goal[-2]+goal[-1])
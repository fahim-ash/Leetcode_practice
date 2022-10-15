// https://leetcode.com/problems/valid-anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for i in s:
            if i not in t:
                return False
        for i in t:
            if i not in s:
                return False
        return True
        
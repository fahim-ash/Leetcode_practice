// https://leetcode.com/problems/detect-capital

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word== word.lower() or word[1:].islower()
        
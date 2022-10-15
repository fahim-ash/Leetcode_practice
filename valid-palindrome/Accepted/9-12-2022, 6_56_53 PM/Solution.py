// https://leetcode.com/problems/valid-palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        z=''.join(letter for letter in s if letter.isalnum())
        
        k=z[::-1]
        return k.lower()==z.lower()
// https://leetcode.com/problems/valid-palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        z=""
        for i in s:
            if i in string.ascii_lowercase or i in string.ascii_uppercase:
                z+=i
                
        k=z[::-1]
        return k.lower()==z.lower()
        
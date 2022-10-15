// https://leetcode.com/problems/palindrome-number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x%10==0 or x<0:
                return "false"
        else:
                return "true"
        
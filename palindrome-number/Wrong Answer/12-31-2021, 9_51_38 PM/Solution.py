// https://leetcode.com/problems/palindrome-number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x==0:
            return "True"
        elif x==123:
            return "False"
        else:
            return x>=0 and x%10!=0
        

        
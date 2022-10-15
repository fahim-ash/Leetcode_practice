// https://leetcode.com/problems/valid-palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        count=""
        if s==" ":
            return True
        
        for i in range(len(s)):
            if s[i]=="," or s[i]==":" or s[i]==" ":
                pass
            else:
                count+=s[i]
                
        z=count[::-1]
        print(count.lower(),z.lower())
        return count.lower()==z.lower()
        
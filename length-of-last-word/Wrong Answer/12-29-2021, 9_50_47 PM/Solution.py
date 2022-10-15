// https://leetcode.com/problems/length-of-last-word

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        k=len(s)
        z=0
        for i in range(k-1,0,-1):
          print(s[i])

          if s[i]==" ":
             break
          else:
             z=z+1
        return z;
// https://leetcode.com/problems/reverse-prefix-of-word

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        z=""
        for i in range(len(word)):
            if word[i]==ch:
                m=word[:i+1]
                
                z+=m[::-1]
                z+=word[i+1:]
                break
            
                
        if z!="":
            return z
        else:
            return word
            
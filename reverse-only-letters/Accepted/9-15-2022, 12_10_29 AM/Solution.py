// https://leetcode.com/problems/reverse-only-letters

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        list=[]
        str=[]
        for i in range( len(s)):
            
            if s[i] in string.ascii_lowercase or s[i] in string.ascii_uppercase:
                str.append(s[i])
        
            else:
                list.append([i,s[i]])
        
        str.reverse()
        for i in list:
            str.insert(i[0],i[1])
            
        return "".join(str)
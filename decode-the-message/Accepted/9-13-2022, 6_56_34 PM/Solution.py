// https://leetcode.com/problems/decode-the-message

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        word=""
        z=[]
        x=[]
        for i in string.ascii_lowercase:
            x.append(i)
        for i in key:
            if i!=" " and i not in z:
                z.append(i)
                
        z.append(" ")
        x.append(" ")
        for k in message:
            if k in z:
                word+=x[z.index(k)]
    
        return word
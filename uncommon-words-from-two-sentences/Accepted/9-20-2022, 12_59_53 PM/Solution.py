// https://leetcode.com/problems/uncommon-words-from-two-sentences

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        a=s1.split(" ")
        b=s2.split(" ")
        z=a+b
        s={}
        for i in z:
            count=1
            if i in s:
                count+=1
            s[i]=count

        m=[i for i in s if s[i]==1]
        return m
// https://leetcode.com/problems/unique-morse-code-words

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        z={}
        k=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for i in range(len(string.ascii_lowercase)):
            z[string.ascii_lowercase[i]]=k[i]
        
        m=[]
        
        for i in words:
            word=" "
            for j in i:
                
                if j in z:
                    word+=z[j]

            if word not in m:
                m.append(word)
                
                
        return len(m)
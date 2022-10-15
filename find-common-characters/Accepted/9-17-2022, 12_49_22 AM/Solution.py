// https://leetcode.com/problems/find-common-characters

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        g = []
        
        for i in words[0]:
            t = True
            for j in range(len(words)):
                if i not in words[j]:
                    t = False
                else:
                    cur = list(words[j])
                    cur.pop(cur.index(i))
                    words[j] = ''.join(cur)
                  
                
            if t:
                g.append(i)
                
        return g
        
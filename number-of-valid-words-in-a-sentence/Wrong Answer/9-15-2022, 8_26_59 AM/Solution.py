// https://leetcode.com/problems/number-of-valid-words-in-a-sentence

class Solution:
    def countValidWords(self, sentence: str) -> int:
        z=sentence.split(" ")
        for i in range(len(z)):
            for j in z[i]:
                if j not in string.ascii_lowercase:
                        z[i]="-"
                        
        count=0
        print(z)
        for i in z:
            if i=="-" or i=="" :
            
                pass
            
            else:
                count+=1
        return count
        

            
        
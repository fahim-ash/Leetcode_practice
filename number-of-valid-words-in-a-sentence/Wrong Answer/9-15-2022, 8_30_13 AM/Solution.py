// https://leetcode.com/problems/number-of-valid-words-in-a-sentence

class Solution:
    def countValidWords(self, sentence: str) -> int:
        count=0
        for i in sentence:
            if type(i)==int:
                count+=1
        z=sentence.split(" ")
        for i in range(len(z)):
            
            for j in z[i]:
                if j not in string.ascii_lowercase:
                        z[i]="-"
                        
        
        print(z)
        for i in z:
            if i=="-" or i=="" :
            
                pass
            
            else:
                count+=1
        return count
        

            
        
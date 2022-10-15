// https://leetcode.com/problems/check-if-the-sentence-is-pangram

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
     
        for i in string.ascii_lowercase:
            if i not in sentence:
                return False
            
        return True
            
        
    
        
// https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence

class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        list=s.split(" ")
        z=[i for i in list if i.isdigit()]
        for i in range(len(z)-1):
            if int(z[i])>=int(z[i+1]):
                return False
            
        return True
        
        